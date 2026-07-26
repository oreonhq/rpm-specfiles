%global source0_hash 386cb590a931772a26a1a00d4fd56169ba7967ecc598984c434e7f4bebf2361e

%global		oname torbrowser_launcher
Name:		torbrowser-launcher
Version:	0.3.9
Release:	3%{?dist}
Summary:	Tor Browser Bundle managing tool
License:	MIT
URL:		https://github.com/micahflee/torbrowser-launcher/
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
ExclusiveArch: %{ix86} x86_64
BuildRequires:	desktop-file-utils
BuildRequires:	python3-devel
BuildRequires:	gettext
BuildRequires:	libappstream-glib
BuildRequires:  python3-distro
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
Requires:	python3
Requires:	gnupg2
Requires:	tor
Requires:	python3-pysocks
Requires:	python3-gpg
Requires:	python3-pyside6
Requires:	python3-requests
Requires:       python3-packaging
Requires:       dbus-glib

%description
Tor Browser Launcher is intended to make Tor Browser easier to
install and use for GNU/Linux users. You install torbrowser-launcher
from your distribution's package manager and it handles everything else:

* Downloads and installs the most recent version of Tor Browser in your language
  and for your computer's architecture, or launches Tor Browser if it's already
  installed (Tor Browser will automatically update itself)
* Verifies Tor Browser's signature for you, to ensure the version you downloaded
  was cryptographically signed by Tor developers and was not tampered with
* Adds "Tor Browser" and "Tor Browser Launcher Settings" application launcher
  to your desktop environment's menu
* Optionally plays a modem sound when you open Tor Browser
  (because Tor is so slow)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

# We need to specify the distro we are building on, Fedora!
sed -i 's#distro = .*#distro = "Fedora"#g' setup.py
sed -i 's/Ubuntu/Fedora/g' setup.py
sed -i "s#'update_over_tor': True#'update_over_tor': False#g" torbrowser_launcher/common.py
sed -i -r "s/^([ \t]+)self.label1 = gtk.Label\(_\('Not installed'\)\)/\
\1self.label1 = gtk.Label\(_\('Not installed'\)\)\n\1self.tor_update_checkbox.\
set_active\(False\)/g" torbrowser_launcher/settings.py

%build
%pyproject_wheel
desktop-file-validate share/applications/org.torproject.torbrowser-launcher.desktop
desktop-file-validate share/applications/org.torproject.torbrowser-launcher.settings.desktop

%install
find . -name apparmor -type d -print0|xargs -0 rm -r --
%pyproject_install
install -m 644 -D share/metainfo/org.torproject.torbrowser-launcher.metainfo.xml \
    %{buildroot}%{_datadir}/metainfo/org.torproject.torbrowser-launcher.metainfo.xml

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.torproject.torbrowser-launcher.metainfo.xml

%files -f %{name}.lang
%{_bindir}/%{name}
%doc README.md
%license LICENSE
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/128x128/apps/org.torproject.torbrowser-launcher.png
%{_datadir}/%{name}/*
%{python3_sitelib}/%{oname}/*
%{_metainfodir}/org.torproject.torbrowser-launcher.metainfo.xml
%{python3_sitelib}/%{oname}-%{version}.dist-info/

%changelog
%autochangelog
