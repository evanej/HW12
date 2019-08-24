{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: selenium in c:\\users\\evanj\\anaconda3\\envs\\pythondata\\lib\\site-packages (3.141.0)\n",
      "Requirement already satisfied: urllib3 in c:\\users\\evanj\\anaconda3\\envs\\pythondata\\lib\\site-packages (from selenium) (1.24.1)\n",
      "Requirement already satisfied: splinter in c:\\users\\evanj\\anaconda3\\envs\\pythondata\\lib\\site-packages (0.11.0)\n",
      "Requirement already satisfied: six in c:\\users\\evanj\\anaconda3\\envs\\pythondata\\lib\\site-packages (from splinter) (1.12.0)\n",
      "Requirement already satisfied: selenium>=3.141.0 in c:\\users\\evanj\\anaconda3\\envs\\pythondata\\lib\\site-packages (from splinter) (3.141.0)\n",
      "Requirement already satisfied: urllib3 in c:\\users\\evanj\\anaconda3\\envs\\pythondata\\lib\\site-packages (from selenium>=3.141.0->splinter) (1.24.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install selenium\n",
    "!pip install splinter\n",
    "\n",
    "from bs4 import BeautifulSoup as bs\n",
    "from splinter import Browser\n",
    "import os\n",
    "import pandas as pd\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Choose the executable path \n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit web page\n",
    "url = \"https://mars.nasa.gov/news/\"\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "soup = bs(html,\"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Title: What's Mars Solar Conjunction, and Why Does It Matter?\n",
      "Para: NASA spacecraft at Mars are going to be on their own for a few weeks when the Sun comes between Mars and Earth, interrupting communications.\n"
     ]
    }
   ],
   "source": [
    "news_title = soup.find(\"div\",class_=\"content_title\").text\n",
    "news_paragraph = soup.find(\"div\", class_=\"article_teaser_body\").text\n",
    "print(f\"Title: {news_title}\")\n",
    "print(f\"Para: {news_paragraph}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "### MARS IMAGES"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "url_image = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "browser.visit(url_image)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.gov/\n"
     ]
    }
   ],
   "source": [
    "from urllib.parse import urlsplit\n",
    "base_url = \"{0.scheme}://{0.netloc}/\".format(urlsplit(url_image))\n",
    "print(base_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# grab image\n",
    "xpath = \"//*[@id=\\\"page\\\"]/section[3]/div/ul/li[1]/a/div/div[2]/img\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Use splinter to click on the mars featured image\n",
    "#to bring the full resolution image\n",
    "results = browser.find_by_xpath(xpath)\n",
    "img = results[0]\n",
    "img.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "#get image url using BeautifulSoup\n",
    "image_url = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "browser.visit(image_url)\n",
    "html = browser.html\n",
    "soup = bs(html, \"html.parser\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA23345-640x350.jpg\n"
     ]
    }
   ],
   "source": [
    "image = soup.find(\"img\", class_=\"thumb\")[\"src\"]\n",
    "featured_image_url = \"https://www.jpl.nasa.gov\" + image\n",
    "print(featured_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "##Weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "url_weather = \"https://twitter.com/marswxreport?lang=en\"\n",
    "browser.visit(url_weather)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "InSight sol 261 (2019-08-21) low -102.4ºC (-152.4ºF) high -26.6ºC (-15.8ºF)\n",
      "winds from the SSE at 4.9 m/s (11.0 mph) gusting to 16.0 m/s (35.8 mph)\n",
      "pressure at 7.70 hPapic.twitter.com/MhPPOHJg3m\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<div class=\"tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content original-tweet js-original-tweet has-cards has-content\" data-conversation-id=\"1164580812664332289\" data-disclosure-type=\"\" data-follows-you=\"false\" data-has-cards=\"true\" data-item-id=\"1164580812664332289\" data-name=\"Mars Weather\" data-permalink-path=\"/MarsWxReport/status/1164580812664332289\" data-reply-to-users-json='[{\"id_str\":\"786939553\",\"screen_name\":\"MarsWxReport\",\"name\":\"Mars Weather\",\"emojified_name\":{\"text\":\"Mars Weather\",\"emojified_text_as_html\":\"Mars Weather\"}}]' data-screen-name=\"MarsWxReport\" data-tweet-id=\"1164580812664332289\" data-tweet-nonce=\"1164580812664332289-402d549f-d1fc-4706-b513-cacccb2fcba8\" data-tweet-stat-initialized=\"true\" data-user-id=\"786939553\" data-you-block=\"false\" data-you-follow=\"false\">\n",
       "<div class=\"context\">\n",
       "</div>\n",
       "<div class=\"content\">\n",
       "<div class=\"stream-item-header\">\n",
       "<a class=\"account-group js-account-group js-action-profile js-user-profile-link js-nav\" data-user-id=\"786939553\" href=\"/MarsWxReport\">\n",
       "<img alt=\"\" class=\"avatar js-action-profile-avatar\" src=\"https://pbs.twimg.com/profile_images/2552209293/220px-Mars_atmosphere_bigger.jpg\"/>\n",
       "<span class=\"FullNameGroup\">\n",
       "<strong class=\"fullname show-popup-with-id u-textTruncate\" data-aria-label-part=\"\">Mars Weather</strong><span>‏</span><span class=\"UserBadges\"></span><span class=\"UserNameBreak\"> </span></span><span class=\"username u-dir u-textTruncate\" data-aria-label-part=\"\" dir=\"ltr\">@<b>MarsWxReport</b></span></a>\n",
       "<small class=\"time\">\n",
       "<a class=\"tweet-timestamp js-permalink js-nav js-tooltip\" data-conversation-id=\"1164580812664332289\" href=\"/MarsWxReport/status/1164580812664332289\" title=\"9:51 AM - 22 Aug 2019\"><span class=\"_timestamp js-short-timestamp\" data-aria-label-part=\"last\" data-long-form=\"true\" data-time=\"1566492677\" data-time-ms=\"1566492677000\">Aug 22</span></a>\n",
       "</small>\n",
       "<div class=\"ProfileTweet-action ProfileTweet-action--more js-more-ProfileTweet-actions\">\n",
       "<div class=\"dropdown\">\n",
       "<button aria-haspopup=\"true\" class=\"ProfileTweet-actionButton u-textUserColorHover dropdown-toggle js-dropdown-toggle\" type=\"button\">\n",
       "<div class=\"IconContainer js-tooltip\" title=\"More\">\n",
       "<span class=\"Icon Icon--caretDownLight Icon--small\"></span>\n",
       "<span class=\"u-hiddenVisually\">More</span>\n",
       "</div>\n",
       "</button>\n",
       "<div class=\"dropdown-menu is-autoCentered\">\n",
       "<div class=\"dropdown-caret\">\n",
       "<div class=\"caret-outer\"></div>\n",
       "<div class=\"caret-inner\"></div>\n",
       "</div>\n",
       "<ul>\n",
       "<li class=\"copy-link-to-tweet js-actionCopyLinkToTweet\">\n",
       "<button class=\"dropdown-link\" type=\"button\">Copy link to Tweet</button>\n",
       "</li>\n",
       "<li class=\"embed-link js-actionEmbedTweet\" data-nav=\"embed_tweet\">\n",
       "<button class=\"dropdown-link\" type=\"button\">Embed Tweet</button>\n",
       "</li>\n",
       "</ul>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "<div class=\"js-tweet-text-container\">\n",
       "<p class=\"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text\" data-aria-label-part=\"0\" lang=\"en\">InSight sol 261 (2019-08-21) low -102.4ºC (-152.4ºF) high -26.6ºC (-15.8ºF)\n",
       "winds from the SSE at 4.9 m/s (11.0 mph) gusting to 16.0 m/s (35.8 mph)\n",
       "pressure at 7.70 hPa<a class=\"twitter-timeline-link u-hidden\" data-pre-embedded=\"true\" dir=\"ltr\" href=\"https://t.co/MhPPOHJg3m\">pic.twitter.com/MhPPOHJg3m</a></p>\n",
       "</div>\n",
       "<div class=\"AdaptiveMediaOuterContainer\">\n",
       "<div class=\"AdaptiveMedia is-square\">\n",
       "<div class=\"AdaptiveMedia-container\">\n",
       "<div class=\"AdaptiveMedia-singlePhoto\" style=\"padding-top: calc(0.5625 * 100% - 0.5px);\">\n",
       "<div class=\"AdaptiveMedia-photoContainer js-adaptive-photo\" data-dominant-color=\"[51,52,64]\" data-element-context=\"platform_photo_card\" data-image-url=\"https://pbs.twimg.com/media/EClsE4iXUAA8LZB.jpg\" style=\"background-color:rgba(51,52,64,1.0);\">\n",
       "<img alt=\"\" data-aria-label-part=\"\" src=\"https://pbs.twimg.com/media/EClsE4iXUAA8LZB.jpg\" style=\"width: 100%; top: -0px;\"/>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "<div class=\"stream-item-footer\">\n",
       "<div class=\"ProfileTweet-actionCountList u-hiddenVisually\">\n",
       "<span class=\"ProfileTweet-action--reply u-hiddenVisually\">\n",
       "<span aria-hidden=\"true\" class=\"ProfileTweet-actionCount\" data-tweet-stat-count=\"0\">\n",
       "<span class=\"ProfileTweet-actionCountForAria\" id=\"profile-tweet-action-reply-count-aria-1164580812664332289\">0 replies</span>\n",
       "</span>\n",
       "</span>\n",
       "<span class=\"ProfileTweet-action--retweet u-hiddenVisually\">\n",
       "<span class=\"ProfileTweet-actionCount\" data-tweet-stat-count=\"5\">\n",
       "<span class=\"ProfileTweet-actionCountForAria\" data-aria-label-part=\"\" id=\"profile-tweet-action-retweet-count-aria-1164580812664332289\">5 retweets</span>\n",
       "</span>\n",
       "</span>\n",
       "<span class=\"ProfileTweet-action--favorite u-hiddenVisually\">\n",
       "<span class=\"ProfileTweet-actionCount\" data-tweet-stat-count=\"18\">\n",
       "<span class=\"ProfileTweet-actionCountForAria\" data-aria-label-part=\"\" id=\"profile-tweet-action-favorite-count-aria-1164580812664332289\">18 likes</span>\n",
       "</span>\n",
       "</span>\n",
       "</div>\n",
       "<div aria-label=\"Tweet actions\" class=\"ProfileTweet-actionList js-actions\" role=\"group\">\n",
       "<div class=\"ProfileTweet-action ProfileTweet-action--reply\">\n",
       "<button aria-describedby=\"profile-tweet-action-reply-count-aria-1164580812664332289\" class=\"ProfileTweet-actionButton js-actionButton js-actionReply\" data-modal=\"ProfileTweet-reply\" type=\"button\">\n",
       "<div class=\"IconContainer js-tooltip\" title=\"Reply\">\n",
       "<span class=\"Icon Icon--medium Icon--reply\"></span>\n",
       "<span class=\"u-hiddenVisually\">Reply</span>\n",
       "</div>\n",
       "<span class=\"ProfileTweet-actionCount ProfileTweet-actionCount--isZero\">\n",
       "<span aria-hidden=\"true\" class=\"ProfileTweet-actionCountForPresentation\"></span>\n",
       "</span>\n",
       "</button>\n",
       "</div>\n",
       "<div class=\"ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt\">\n",
       "<button aria-describedby=\"profile-tweet-action-retweet-count-aria-1164580812664332289\" class=\"ProfileTweet-actionButton js-actionButton js-actionRetweet\" data-modal=\"ProfileTweet-retweet\" type=\"button\">\n",
       "<div class=\"IconContainer js-tooltip\" title=\"Retweet\">\n",
       "<span class=\"Icon Icon--medium Icon--retweet\"></span>\n",
       "<span class=\"u-hiddenVisually\">Retweet</span>\n",
       "</div>\n",
       "<span class=\"ProfileTweet-actionCount\">\n",
       "<span aria-hidden=\"true\" class=\"ProfileTweet-actionCountForPresentation\">5</span>\n",
       "</span>\n",
       "</button><button class=\"ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet\" data-modal=\"ProfileTweet-retweet\" type=\"button\">\n",
       "<div class=\"IconContainer js-tooltip\" title=\"Undo retweet\">\n",
       "<span class=\"Icon Icon--medium Icon--retweet\"></span>\n",
       "<span class=\"u-hiddenVisually\">Retweeted</span>\n",
       "</div>\n",
       "<span class=\"ProfileTweet-actionCount\">\n",
       "<span aria-hidden=\"true\" class=\"ProfileTweet-actionCountForPresentation\">5</span>\n",
       "</span>\n",
       "</button>\n",
       "</div>\n",
       "<div class=\"ProfileTweet-action ProfileTweet-action--favorite js-toggleState\">\n",
       "<button aria-describedby=\"profile-tweet-action-favorite-count-aria-1164580812664332289\" class=\"ProfileTweet-actionButton js-actionButton js-actionFavorite\" type=\"button\">\n",
       "<div class=\"IconContainer js-tooltip\" title=\"Like\">\n",
       "<span class=\"Icon Icon--heart Icon--medium\" role=\"presentation\"></span>\n",
       "<div class=\"HeartAnimation\"></div>\n",
       "<span class=\"u-hiddenVisually\">Like</span>\n",
       "</div>\n",
       "<span class=\"ProfileTweet-actionCount\">\n",
       "<span aria-hidden=\"true\" class=\"ProfileTweet-actionCountForPresentation\">18</span>\n",
       "</span>\n",
       "</button><button class=\"ProfileTweet-actionButtonUndo ProfileTweet-action--unfavorite u-linkClean js-actionButton js-actionFavorite\" type=\"button\">\n",
       "<div class=\"IconContainer js-tooltip\" title=\"Undo like\">\n",
       "<span class=\"Icon Icon--heart Icon--medium\" role=\"presentation\"></span>\n",
       "<div class=\"HeartAnimation\"></div>\n",
       "<span class=\"u-hiddenVisually\">Liked</span>\n",
       "</div>\n",
       "<span class=\"ProfileTweet-actionCount\">\n",
       "<span aria-hidden=\"true\" class=\"ProfileTweet-actionCountForPresentation\">18</span>\n",
       "</span>\n",
       "</button>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>\n",
       "</div>"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "html_weather = browser.html\n",
    "soup = bs(html_weather, \"html.parser\")\n",
    "temp = soup.find('div', attrs={\"class\": \"tweet\", \"data-name\": \"Mars Weather\"})\n",
    "mars_weather = soup.find(\"p\", class_=\"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text\").text\n",
    "print(mars_weather)\n",
    "temp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "url_Marsfacts = \"https://space-facts.com/mars/\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Diameter:</td>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Distance from Sun:</td>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Length of Year:</td>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Temperature:</td>\n",
       "      <td>-153 to 20 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Mars - Earth Comparison             Mars            Earth\n",
       "0               Diameter:         6,779 km        12,742 km\n",
       "1                   Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "2                  Moons:                2                1\n",
       "3      Distance from Sun:   227,943,824 km   149,598,262 km\n",
       "4         Length of Year:   687 Earth days      365.24 days\n",
       "5            Temperature:    -153 to 20 °C      -88 to 58°C"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "table = pd.read_html(url_Marsfacts)\n",
    "table[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "url_hemisphere = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "browser.visit(url_hemisphere)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://astrogeology.usgs.gov/\n"
     ]
    }
   ],
   "source": [
    "#Getting the base url\n",
    "hemisphere_base_url = \"{0.scheme}://{0.netloc}/\".format(urlsplit(url_hemisphere))\n",
    "print(hemisphere_base_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "import time \n",
    "hemispheres_url = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "browser.visit(hemispheres_url)\n",
    "html = browser.html\n",
    "soup = bs(html, \"html.parser\")\n",
    "mars_hemisphere = []\n",
    "\n",
    "products = soup.find(\"div\", class_ = \"result-list\" )\n",
    "hemispheres = products.find_all(\"div\", class_=\"item\")\n",
    "\n",
    "for hemisphere in hemispheres:\n",
    "    title = hemisphere.find(\"h3\").text\n",
    "    title = title.replace(\"Enhanced\", \"\")\n",
    "    end_link = hemisphere.find(\"a\")[\"href\"]\n",
    "    image_link = \"https://astrogeology.usgs.gov/\" + end_link    \n",
    "    browser.visit(image_link)\n",
    "    html = browser.html\n",
    "    soup=bs(html, \"html.parser\")\n",
    "    downloads = soup.find(\"div\", class_=\"downloads\")\n",
    "    image_url = downloads.find(\"a\")[\"href\"]\n",
    "    mars_hemisphere.append({\"title\": title, \"img_url\": image_url})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere ',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere ',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere ',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere ',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mars_hemisphere\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
