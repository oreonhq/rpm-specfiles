%global source0_hash 0f84e5dab6a5748e315cdbe371b218cad8db439d3d6e8d0efc17ba959aa6a5ab

#For git snapshots, set to 0 to use release instead:
%global usesnapshot 1
%if 0%{?usesnapshot}
%global commit0 8b8bb63a10fa22760eb976b1fd57338f3dba3233
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global snapshottag .git%{shortcommit0}
%global upstream_tag 0.9.0-b1
%endif

Name:           variety
%if 0%{?usesnapshot}
#Release:        0.17%%{?snapshottag}%%{?dist}
Version:        0.9.0
Release:        0.1.beta1%{?dist}
%else
Version:        0.8.13
Release:        8%{?dist}
%endif
Summary:        Wallpaper changer that automatically downloads wallpapers
License:        GPL-3.0-only
URL:            https://github.com/varietywalls/variety

%if 0%{?usesnapshot}
#Source0:       %%{url}/archive/%%{commit0}/%%{name}-%%{shortcommit0}.tar.gz
Source0:        %{url}/archive/refs/tags/%{upstream_tag}.tar.gz#/%{name}-%{upstream_tag}.tar.gz
%else
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3dist(setuptools-gettext)
BuildRequires:  python3-configobj
BuildRequires:  python3-lxml
BuildRequires:  python3-gexiv2
BuildRequires:  python3-pycurl
BuildRequires:  python3-requests
BuildRequires:  python3-pillow-devel
BuildRequires:  intltool
BuildRequires:  yelp-devel
BuildRequires:  python3-dbus
BuildRequires:  python3-cairo-devel
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  %{py3_dist beautifulsoup4}
BuildRequires:  python3-cairo
Requires:       python3-dbus
Requires:       hicolor-icon-theme
Requires:       ImageMagick
Requires:       libappindicator-gtk3
Requires:       python3-lxml
Requires:       python3-pillow
#Requires:       python3-appindicator -- not available yet
Requires:       python3-beautifulsoup4
Requires:       python3-configobj
Requires:       python3-gexiv2
Requires:       python3-pycurl
Requires:       python3-requests
Requires:       python3-httplib2
Requires:       xorg-x11-fonts-Type1
Requires:       python3-zombie-imp

%description
Variety changes the desktop wallpaper on a regular basis, 
using user-specified or automatically downloaded images.

Variety sits conveniently as an indicator in the panel 
and can be easily paused and resumed. The mouse wheel 
can be used to scroll wallpapers back and forth until 
you find the perfect one for your current mood.

Apart from displaying images from local folders, several 
different online sources can be used to fetch wallpapers 
according to user-specified criteria.

Variety can also automatically apply various fancy 
filters to the displayed images - charcoal painting, 
oil painting, heavy blurring, etc. - so that your 
desktop is always fresh and unique. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?usesnapshot}
#%%autosetup -p1 -n %%{name}-%%{commit0}
%autosetup -p1 -n %{name}-%{upstream_tag}
%else
%autosetup -p1
%endif

# Fix setuptools package discovery warnings (Python 3.14)
sed -i 's/include = \["variety", "variety_lib"\]/include = ["variety*","variety_lib*"]/' pyproject.toml || :

# Fix invalid gettext-style desktop keys (_Name/_Comment not allowed anymore)
sed -i \
  -e 's/^_Name=/Name=/' \
  -e 's/^_Comment=/Comment=/' \
  variety.desktop.in

# remove debian part
#rm -rf debian

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files variety variety_lib jumble

# --------------------------------------------------------------------
# Move media files from site-packages to /usr/share/variety/media
# --------------------------------------------------------------------
install -d %{buildroot}%{_datadir}/%{name}/media

cp -a %{buildroot}%{python3_sitelib}/variety/data/media/* \
      %{buildroot}%{_datadir}/%{name}/media/

# Remove duplicate media from Python directory
rm -rf %{buildroot}%{python3_sitelib}/variety/data/media

# --------------------------------------------------------------------
# Install application icons properly (hicolor theme)
# --------------------------------------------------------------------
install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -d %{buildroot}%{_datadir}/icons/hicolor/128x128/apps

install -m 0644 %{buildroot}%{_datadir}/%{name}/media/variety.svg \
        %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/variety.svg

install -m 0644 %{buildroot}%{_datadir}/%{name}/media/variety128.png \
        %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/variety.png

# Install desktop file
install -D -m 644 %{name}.desktop.in %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install man page (if exists)
if [ -f debian/%{name}.1 ]; then
    install -D -m 644 debian/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
fi

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.appdata.xml

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{python3_sitelib}/jumble/
%{python3_sitelib}/%{name}-*.dist-info
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}_lib/
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
