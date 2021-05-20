# instafetch
Neofetch but with a random image from your favorite Instagram account! (also it's in Python)

## Requirements:
1. A working [neofetch](https://github.com/dylanaraps/neofetch/) installation
2. A functioning image backend for neofetch in your terminal of choice
3. This [instagram scraper](https://github.com/realsirjoe/instagram-scraper), written in Python

## Usage:
Clone this repository:

```git clone https://github.com/MasterMax13124/instafetch/```

and `cd` into it. Open `instafetch.py` in your favorite text editor and add the following values:

1. `backend` needs to be the name of your image backend for neofetch
2. `username` is the Instagram username that you want to pull the images from. It needs to be a public account!
3. `postlimit` limits how many posts the script looks at for the random selection, you can play around with this I guess

Once you're done with that, just run `python3 instafetch.py` and you should be good to go. Most errors are probably to do with the instagram scraper, look to their GitHub page for fixes.
