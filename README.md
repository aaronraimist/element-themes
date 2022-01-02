# Element Themes

A place to share themes for [Element Web/Desktop](https://github.com/vector-im/element-web). Themes are currently a beta or "Labs" feature, so you won't be able to use them with every instance of Element. [Read on](#How-to-use-themes) to learn how to use them.

To get help or discuss themes, join us in [#element-themes:raim.ist](https://matrix.to/#/#element-themes:raim.ist)


## How to use themes

There are several different ways to install these themes.


### Use an existing instance of Element which has Labs enabled

If you are using an instances of Element which has Labs features available then you can use these themes. Go to the Labs tab in Settings and turn on "Support adding custom themes". To add a theme, find one below that you would like to try. Then copy the URL to the JSON file that makes up the theme. Go to the Apperance tab in Settings and paste the URL into the "Custom theme URL" field and click "Add theme".

One example of an instance that has Labs enabled is https://develop.element.io however be aware this is a bleeding edge version of Element and you may run into bugs. Most stable instances of Element like https://app.element.io do not have Labs features enabled.


### Self host Element or use Element Desktop:

If you are self hosting your own instance of Element or you are using the Desktop app, you can use these themes by editing your `config.json` file. Put the themes you want inside of the `settingDefaults` section like this:

```json
{
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
    },
    "showLabsSettings": true
}
```

Once you do that, you will need to enable "Support adding custom themes" (`feature_custom_themes`) in the Labs section of Settings so that these themes appear in the Appearance section of Settings.

To use a custom `config.json` file with Element Desktop, see https://github.com/vector-im/element-desktop#user-specified-configjson


### If you use the matrix-docker-ansible-deploy project

You can enable all of these themes just by setting `matrix_client_element_themes_enabled: true` in your `vars.yml` file. See https://github.com/spantaleev/matrix-docker-ansible-deploy/blob/master/docs/configuring-playbook-client-element.md#themes for more details.


### Use my Element Web instance

Alternatively you can use [my Element Web instance](https://riot.raim.ist) which has all of these themes preinstalled so there is no configuration required.


# Themes

## [ThomCat Black](https://raw.githubusercontent.com/aaronraimist/element-themes/master/ThomCat/ThomCat-Black.json)

Made by `@me:thomcat.rocks`

![ThomCat Black Screenshot](ThomCat/ThomCat-Black.png)


## [Discord Dark Theme](https://raw.githubusercontent.com/aaronraimist/element-themes/master/Discord/Discord-Dark/Discord-Dark-Theme.json)

Made by [`@dylhack:newcircuit.io`](https://github.com/dylhack) and [`@Oha-you`](https://github.com/Oha-you)

![Discord Dark Theme Screenshot](Discord/Discord-Dark/Discord-Dark-Theme.png)


## [Luxury Dark Theme](https://raw.githubusercontent.com/aaronraimist/element-themes/master/Luxury/Luxury%20Dark/Luxury%20Dark.json)

Made by [`@dylhack:newcircuit.io`](https://github.com/dylhack)

![Luxury Dark Theme Screenshot](./Luxury/Luxury%20Dark/Luxury%20Dark.png)


## [Night Owl Dark Theme](https://raw.githubusercontent.com/aaronraimist/element-themes/master/Night%20Owl/Night%20Owl%20Dark/Nord%20Owl%20Dark.json

Made by [`@foxy:teapot.ovh`](https:github.com/foxyseta)

![Night Owl Dark Theme Screenshot](Night%20Owl/Night%20Owl%20Dark/Night%20Owl%20Dark.png)


## [Nord Dark Theme](https://raw.githubusercontent.com/aaronraimist/element-themes/master/Nord/Nord%20Dark/Nord%20Dark.json)

Made by [`@dylhack:newcircuit.io`](https://github.com/dylhack)

![Nord Dark Theme Screenshot](Nord/Nord%20Dark/Nord%20Dark.png)


## [Nord Light Theme](https://raw.githubusercontent.com/aaronraimist/element-themes/master/Nord/Nord%20Light/Nord%20Light.json)

Made by [`@dylhack:newcircuit.io`](https://github.com/dylhack)

![Nord Light Theme Screenshot](Nord/Nord%20Light/Nord%20Light.png)


## [Selenized Light Theme](https://raw.githubusercontent.com/aaronraimist/element-themes/master/Selenized/Selenized%20Light/Selenized%20Light.json)

Made by [`@dylhack:newcircuit.io`](https://github.com/dylhack)

![Selenized Light Theme Screenshot](Selenized/Selenized%20Light/Selenized%20Light.png)


## [Selenized Dark Theme](https://raw.githubusercontent.com/aaronraimist/element-themes/master/Selenized/Selenized%20Dark/Selenized%20Dark.json)

Made by [`@dylhack:newcircuit.io`](https://github.com/dylhack)

![Selenized Dark Theme Screenshot](Selenized/Selenized%20Dark/Selenized%20Dark.png)


## [Selenized Black Theme](https://raw.githubusercontent.com/aaronraimist/element-themes/master/Selenized/Selenized%20Black/Selenized%20Black.json)

Made by [`@dylhack:newcircuit.io`](https://github.com/dylhack) and `@david:vovo.id.au`

![Selenized Black Theme Screenshot](Selenized/Selenized%20Black/Selenized%20Black.png)


## [Solarized Dark Theme](https://raw.githubusercontent.com/aaronraimist/element-themes/master/Solarized/Solarized%20Dark/Solarized%20Dark.json)

Made by `@jasonic5:matrix.org`

![Solarized Dark Theme Screenshot](Solarized/Solarized%20Dark/Solarized%20Dark.png)


## [Geeko Dark Theme](https://raw.githubusercontent.com/aaronraimist/element-themes/master/Geeko%20Dark/Geeko%20Dark.json)

Made by `@swedneck:feneas.org`

![Geeko Dark Theme Screenshot](Geeko%20Dark/Geeko%20Dark.png)

## [Dracula Dark Theme](https://raw.githubusercontent.com/aaronraimist/element-themes/master/Dracula/Non-flat/Dracula.json)

Made by `@jakobr_107:utwente.io`

![Dracula Dark Theme Screenshot](Dracula/Non-flat/screenshot%20%2020-06-19%2014-09-11.png)

## [Dracula Flat Dark Theme](https://raw.githubusercontent.com/aaronraimist/element-themes/master/Dracula/Flat/DraculaFlat.json)

Made by `@jo:catgirl.party`

![Dracula Flat Dark Theme Screenshot](Dracula/Flat/screenshot%2020-06-16%2003-05-42.png)


# Advanced

The themes in this repository use Element's relatively basic theming system which can only change a limited number of colors. Element's [theming documentation](https://github.com/vector-im/element-web/blob/master/docs/theming.md) has more information on how these work. For more advanced themes where you want to customize things like fonts, button shapes, or all of the colors you'll need to use CSS which isn't supported by Element's theming system. To use CSS based themes you could use a browser extension like Stylus. https://github.com/dannycolin/riot-compact is an example of a more advanced theme.


## Workarounds

Element's theme implementation is fairly limited so custom themes might introduce some odd elements. For example, when using ThomCat Black, the selected reaction 'pill' is outlined in green since Element doesn't give us a variable to control the color that is used there.

![pill_before](images/Pill1.png)

To fix this, we have to edit the custom theme CSS file directly, in this case `theme-dark-custom.css`.  `cssbeautify-cli` is not necessary if your `sed`-fu is better than the author's is.

```
cssbeautify-cli -f theme-dark-custom.css > /tmp/theme-dark-custom-sed.css
sed '/.mx_ReactionsRowButton.mx_ReactionsRowButton_selected/!b;n;c\ \ \ \ background-color:var(--accent-color);' /tmp/theme-dark-custom-sed.css > /tmp/theme-dark-custom.css
sudo -u <nginx/apache_user> cp /tmp/theme-dark-custom.css /<element_directory>/bundles/<bundle_version>/
```
The results:

![pill_after](images/Pill2.png)


## build.py
There is a [build.py](./build.py) python file which takes all the themes and
outputs it to a file as an array of JSON. Simply execute it in this directory.
