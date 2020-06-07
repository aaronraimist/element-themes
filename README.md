# Riot Web Themes
A place to share themes for [Riot Web](https://github.com/vector-im/riot-web). Riot's [theming documentation](https://github.com/vector-im/riot-web/blob/master/docs/theming.md) has more information on how these work.

These themes are using the relatively basic Riot themeing system which can only change a limited number of colors. For more advanced themes where you want to customize all the colors or things like fonts and button shapes you'll need to use custom CSS files. See https://github.com/dannycolin/riot-compact for an example of a more advanced theme.

#### Discussions
Join us in [#riot-web-themes:dhdf.dev](https://matrix.to/#/!pjCLhvJxLkGjNQFqcB:m.dhdf.dev?via=raim.ist&via=matrix.org&via=dhdf.dev)

### Table of Contents
- [How to use themes](#how-to-use-themes)
  * [If you self host Riot or use Riot Desktop](#if-you-self-host-riot-or-use-riot-desktop)
  * [If you use the matrix-docker-ansible-deploy project](#if-you-use-the-matrix-docker-ansible-deploy-project)
  * [If you are a Firefox user](#if-you-are-a-firefox-user)
  * [Or use my instance of Riot Web](#use-my-riot-web-instance)
- [Themes](#themes)
  * [Discord Dark Theme](#discord-dark-theme)
  * [Geeko Dark Theme](#geeko-dark-theme)
  * [Luxury Dark Theme](#luxury-dark-theme)
  * [Nord Dark Theme](#nord-dark-theme)
  * [Nord Light Theme](#nord-light-theme)
  * [Selenized Black Theme](#selenized-black-theme)
  * [Selenized Dark Theme](#selenized-dark-theme)
  * [Selenized Light Theme](#selenized-light-theme)
  * [ThomCat Black](#thomcat-black)
- [Advanced](#advanced)
  * [Workarounds](#workarounds)
  * [build.py](#build.py)


### How to use themes

There are several different ways to install these. For most users it will be easiest to enable the `feature_custom_themes` labs flag (currently only on https://riot.im/develop). This will allow you to install themes by pasting in the URL to the raw JSON of the theme. Hopefully in the future this interface will be polished up and enabled by default for all users.

Some other options for installing themes:

#### If you self host Riot or use Riot Desktop:
You can use these themes by editing your `config.json` file to include the theme inside of the `settingDefaults` section like this:

```json
"settingDefaults": {
    "custom_themes": [
        {
            "name": "Example theme",
            "colors": {
                "primary-color": "#9F8652"
            }
        },
        {
            "name": "Another theme",
            "colors": {
                "primary-color": "#526A9E"
            }
        }
    ]
}
```

To setup a `config.json` file with Riot Desktop, see https://github.com/vector-im/riot-web/blob/master/docs/config.md#desktop-app-configuration

#### If you use the matrix-docker-ansible-deploy project
You can enable all of these themes just by setting `matrix_riot_web_themes_enabled: true` in your `vars.yml` file. See https://github.com/spantaleev/matrix-docker-ansible-deploy/blob/master/docs/configuring-playbook-riot-web.md#themes for more details.

#### If you are a Firefox user
You can install Radical which is Riot web bundled as a Firefox add-on. You can edit the `config.json` file right in the add-on preferences. It works really well, you should check it out. https://addons.mozilla.org/en-US/firefox/addon/radical-web/

#### Use my Riot Web instance
Alternatively you can use [my Riot Web instance](https://riot.raim.ist) which has all of these themes preinstalled so there is no configuration required.


# Themes

## [ThomCat Black](https://raw.githubusercontent.com/aaronraimist/riot-web-themes/master/ThomCat/ThomCat-Black.json)

Made by `@me:thomcat.rocks`

![ThomCat Black Screenshot](ThomCat/ThomCat-Black.png)


## [Discord Dark Theme](https://raw.githubusercontent.com/aaronraimist/riot-web-themes/master/Discord/Discord-Dark/Discord-Dark-Theme.json)

Made by `@dhmf:dhdf.dev`

![Discord Dark Theme Screenshot](Discord/Discord-Dark/Discord-Dark-Theme.png)


## [Luxury Dark Theme](./Luxury/Luxury%20Dark/Luxury%20Dark.json)

Made by `@dhmf:dhdf.dev`

![Luxury Dark Theme Screenshot](./Luxury/Luxury%20Dark/Luxury%20Dark.png)

## [Nord Dark Theme](https://raw.githubusercontent.com/aaronraimist/riot-web-themes/master/Nord/Nord%20Dark/Nord%20Dark.json)

Made by `@dhmf:dhdf.dev`

![Nord Dark Theme Screenshot](Nord/Nord%20Dark/Nord%20Dark.png)


## [Nord Light Theme](https://raw.githubusercontent.com/aaronraimist/riot-web-themes/master/Nord/Nord%20Light/Nord%20Light.json)

Made by `@dhmf:dhdf.dev`

![Nord Light Theme Screenshot](Nord/Nord%20Light/Nord%20Light.png)


## [Selenized Light Theme](https://raw.githubusercontent.com/aaronraimist/riot-web-themes/master/Selenized/Selenized%20Light/Selenized%20Light.json)

Made by `@dhmf:dhdf.dev`

![Selenized Light Theme Screenshot](Selenized/Selenized%20Light/Selenized%20Light.png)


## [Selenized Dark Theme](https://raw.githubusercontent.com/aaronraimist/riot-web-themes/master/Selenized/Selenized%20Dark/Selenized%20Dark.json)

Made by `@dhmf:dhdf.dev`

![Selenized Dark Theme Screenshot](Selenized/Selenized%20Dark/Selenized%20Dark.png)


## [Selenized Black Theme](https://raw.githubusercontent.com/aaronraimist/riot-web-themes/master/Selenized/Selenized%20Black/Selenized%20Black.json)

Made by `@dhmf:dhdf.dev` and `@david:vovo.id.au`

![Selenized Black Theme Screenshot](Selenized/Selenized%20Black/Selenized%20Black.png)


## [Geeko Dark Theme](https://raw.githubusercontent.com/aaronraimist/riot-web-themes/master/Geeko%20Dark/Geeko%20Dark.json)

Made by `@swedneck:hielle.com`

![Geeko Dark Theme Screenshot](Geeko%20Dark/Geeko%20Dark.png)



# Advanced

## Workarounds

Riot's theme implementation is fairly limited so custom themes might introduce some odd elements. For example, when using ThomCat Black, the selected reaction 'pill' is outlined in green since Riot doesn't give us a variable to control the color that is used there.

![pill_before](images/Pill1.png)

To fix this, we have to edit the custom theme CSS file directly, in this case `theme-dark-custom.css`.  `cssbeautify-cli` is not necessary if your `sed`-fu is better than the author's is.

```
cssbeautify-cli -f theme-dark-custom.css > /tmp/theme-dark-custom-sed.css
sed '/.mx_ReactionsRowButton.mx_ReactionsRowButton_selected/!b;n;c\ \ \ \ background-color:var(--accent-color);' /tmp/theme-dark-custom-sed.css > /tmp/theme-dark-custom.css
sudo -u <nginx/apache_user> cp /tmp/theme-dark-custom.css /<riot_directory>/bundles/<bundle_version>/
```
The results:

![pill_after](images/Pill2.png)

## build.py
There is a [build.py](./build.py) python file which takes all the themes and 
outputs it to a file as an array of JSON. Simply execute it in this directory.
