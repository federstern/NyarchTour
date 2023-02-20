PAGES = [
	{
		"icon": "nyarch-logo",
		"title": "Welcome to Nyarch",
		"icon-size": 400,
		"body": "Nyarch Linux is an Arch Linux based Linux distribution to weeb weeb",
		"buttons": [
			{
				"label": "Open Website",
				"icon": None,
				"style": "suggested-action",
				"command": "xdg-open https://nyarchlinux.moe"
			}
		]
	},
	{
		"icon": "material_you_screenshot",
		"icon-size": 400,
		"title": "Material You",
		"body": "Choose any waifu as your wallpaper, the desktop and applications themes will automatically adapt their colors to make you feel at home. This is achieved through material you Gnome extension.",
		"buttons": [
			{
				"label": "Open Settings",
				"icon": None,
				"style": "suggested-action",
				"command": "gnome-control-center background "
			}
		]
	},
	{
		"icon": "tweaks-screenshots",
		"icon-size": 400,
		"title": "Need advanced customization?",
		"body": "You can customize your operating system more by editing configurations in Gnome Tweaks, and installing new extensions in Extension Manager.",
		"buttons": [
			{
				"label": "Open Tweaks",
				"icon": None,
				"style": "suggested-action",
				"command": "gnome-tweaks"
			},
			{
				"label": "Open Extension Manager",
				"icon": None,
				"style": "suggested-action",
				"command": "flatpak run com.mattjakeman.ExtensionManager"
			},
		]
	},
	{
		"icon": "nyarchcustomize-screenshots",
		"icon-size": 400,
		"title": "Nyarch Customize",
		"body": "Change your layout quickly and customize animations and appearance",
		"buttons": [
			{
				"label": "Open Nyarch Customize",
				"icon": None,
				"style": "suggested-action",
				"command": "flatpak run moe.nyarchlinux.customize "
			}
		]
	},
	{
		"icon": "catgirldownloader-screenshots",
		"icon-size": 400,
		"title": "Catgirl Downloader",
		"body": "This application satisfies one of the most important need that a weeb has: getting some random pictures of cute catgirls whenever you want",
		"buttons": [
			{
				"label": "Open Catgirl Downloader",
				"icon": None,
				"style": "suggested-action",
				"command": "flatpak run moe.nyarchlinux.catgirldownloader "
			}
		]
	},
	{
		"icon": "komikku-screenshots",
		"icon-size": 400,
		"title": "Read manga with Komikku",
		"body": "Komikku is an amazing open source application to read manga from the internet.",
		"buttons": [
			{
				"label": "Project page",
				"icon": None,
				"style": None,
				"command": "xdg-open https://valos.gitlab.io/Komikku/"
			},
			{
				"label": "Open Komikku",
				"icon": None,
				"style": "suggested-action",
				"command": "flatpak run info.febvre.Komikku"
			}
		]
	},
	{
		"icon": "shortwave-screenshots",
		"icon-size": 400,
		"title": "Listen to your favoirite weeb radio with Shortwave",
		"body": "Shortwave is an internet radio player that provides access to a station database with over 30000 stations.",
		"buttons": [
			{
				"label": "Project page",
				"icon": None,
				"style": None,
				"command": "xdg-open https://gitlab.gnome.org/World/Shortwave"
			},
			{
				"label": "Open Shortwave",
				"icon": None,
				"style": "suggested-action",
				"command": "flatpak run de.haeckerfelix.Shortwave"
			}
		]
	},
	{
		"icon": "fragments-screenshots",
		"icon-size": 400,
		"title": "Download Torrents with Fragments",
		"body": "Fragments is an easy to use BitTorrent client. It can be used to transfer files via the BitTorrent protocol.",
		"buttons": [
			{
				"label": "Project page",
				"icon": None,
				"style": None,
				"command": "xdg-open https://gitlab.gnome.org/World/Fragments"
			},
			{
				"label": "Open Fragments",
				"icon": None,
				"style": "suggested-action",
				"command": "flatpak run de.haeckerfelix.Fragments"
			}
		]
	},
	{
		"icon": "lollypop-screenshots",
		"icon-size": 400,
		"title": "Listen to music with Lollypop",
		"body": "Lollypop is an amazing lightwaight music player that a party mode, to stream music from the web or to reproduce music from your own collection.",
		"buttons": [
			{
				"label": "Project page",
				"icon": None,
				"style": None,
				"command": "xdg-open https://wiki.gnome.org/Apps/Lollypop"
			},
			{
				"label": "Open Lollypop",
				"icon": None,
				"style": "suggested-action",
				"command": "flatpak run org.gnome.Lollypop"
			}
		]
	},
	{
		"icon": "webapps-screenshots",
		"icon-size": 400,
		"title": "Turn your favourite streaming websites into apps",
		"body": "Webapp manager makes you create apps from websites that integrates with your desktop, it supports extensions and many browsers.",
		"buttons": [
			{
				"label": "Project page",
				"icon": None,
				"style": None,
				"command": "xdg-open https://github.com/linuxmint/webapp-manager"
			},
			{
				"label": "Open Webapp Manager",
				"icon": None,
				"style": "suggested-action",
				"command": "webapp-manager"
			}
		]
	},
	{
		"icon": "software-screenshots",
		"icon-size": 400,
		"title": "Need other apps?",
		"body": "Download your favourite applications from a vast catalog of applications including Arch Repositories and Flathub from Gnome Software.",
		"buttons": [
			{
				"label": "Open Gnome Software",
				"icon": None,
				"style": "suggested-action",
				"command": "gnome-software"
			}
		]
	},
	{
		"icon": "nyarchwizard-screenshots",
		"icon-size": 400,
		"title": "Need suggestions?",
		"body": "Nyarch Wizard will suggest you some software to get started with Nyarch Linux.",
		"buttons": [
			{
				"label": "Open Nyarch Wizard",
				"icon": None,
				"style": "suggested-action",
				"command": "flatpak run moe.nyarchlinux.wizard"
			}
		]
	},
	{
		"icon": "terminal-screenshots",
		"icon-size": 400,
		"title": "I use Nyarch, btw",
		"body": "We have included nyaofetch to tell everyone that you are using Nyarch Linux, and trizen to download packages from Arch User Repository",
		"buttons": [
			{
				"label": "Run terminal",
				"icon": None,
				"style": "suggested-action",
				"command": 'kitty nekofetch'
			}
		]
	},
	{
		"icon": "gnome-screenshot",
		"icon-size": 400,
		"title": "Discover more about the desktop",
		"body": "Run Gnome Tour to learn more about desktop navigation and touchpad gestures",
		"buttons": [
			{
				"label": "Open Tour",
				"icon": None,
				"style": "suggested-action",
				"command": 'gnome-tour'
			}
		]
	},




]

