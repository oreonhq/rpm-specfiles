%global source0_hash 2875c94b0581f5c628b4f50c0d1aaf8930e524661604e58fc2a1c31c31ed8001

Name:		leonidas-kde-theme
Version:	11.0.3
Release:	30%{?dist}
Summary:	Leonidas KDE Theme

# Automatically converted from old format: GPLv2+ and CC-BY-SA and CC-BY - review is highly recommended.
License:	GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-CC-BY

# We are upstream for this package
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:	https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	kde4-filesystem
Requires:	kde4-filesystem
Requires:	system-logos
Requires:	leonidas-backgrounds-common >= 11.0.0-1
Requires:	leonidas-backgrounds-kdm >= 11.0.0-1

%description
This is Leonidas KDE Theme Artwork containing KSplash theme, KDM theme and
wallpapers theme. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%package lion
Summary:	Leonidas Lion KDE Theme
Requires:	leonidas-backgrounds-lion >= 11.0.0-1

%description lion
This is an optional Leonidas Lion KDE wallpaper theme.

%package landscape
Summary:	Leonidas Landscape KDE Theme
Requires:	leonidas-backgrounds-landscape >= 11.0.0-1

%description landscape
This is an optional Leonidas Landscape KDE wallpaper theme.

%build
# blank

%install
rm -rf %{buildroot}

# wallpapers
# no more wallpapers links in wallpapers directory which causes all wp in list,
# not only theme
mkdir -p %{buildroot}%{_kde4_datadir}/wallpapers

# KDM
# for KDM and splash we use PNG wallpaper from leonidas-kdm package
# thus only one aspect ratio

mkdir -p %{buildroot}/%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/leonidas/ %{buildroot}/%{_kde4_appsdir}/kdm/themes/
(cd %{buildroot}/%{_kde4_appsdir}/kdm/themes/leonidas/
ln -s ../../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.png leonidas.png
)

mkdir -p %{buildroot}/%{_kde4_appsdir}/kdm/pics/users
cp -rp kdm/users %{buildroot}/%{_kde4_appsdir}/kdm/pics

# KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/Leonidas/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
ln -s ../../../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Leonidas/2048x1536/leonidas.png

# KDE 4 wallpapers theme
mkdir -p %{buildroot}%{_kde4_datadir}/wallpapers/leonidas/contents/images
cp -rp wallpapers/leonidas/metadata.desktop %{buildroot}%{_kde4_datadir}/wallpapers/leonidas
cp -rp wallpapers/leonidas/screenshot.png %{buildroot}%{_kde4_datadir}/wallpapers/leonidas/contents
(cd %{buildroot}%{_kde4_datadir}/wallpapers/leonidas/contents/images
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg 640x480.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 800x480.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg 800x600.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 1024x600.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg 1024x768.jpg
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 1152x720.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg 1152x864.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg 1200x900.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 1280x720.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 1280x768.jpg
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 1280x800.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg 1280x960.jpg
ln -s ../../../../backgrounds/leonidas/lion/normalish/1280x1024/leonidas-1-noon.jpg 1280x1024.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 1366x768.jpg
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 1440x900.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg 1440x1080.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg 1600x1200.jpg
ln -s ../../../../backgrounds/leonidas/lion/normalish/1280x1024/leonidas-1-noon.jpg 1600x1280.jpg
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 1680x1050.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 1920x1080.jpg
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg 1920x1200.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg 1920x1440.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg 2048x1536.jpg
)

# KDE 4 wallpapers theme lion
mkdir -p %{buildroot}%{_kde4_datadir}/wallpapers/leonidas-lion/contents/images
cp -rp wallpapers/leonidas-lion/metadata.desktop %{buildroot}%{_kde4_datadir}/wallpapers/leonidas-lion
cp -rp wallpapers/leonidas-lion/screenshot.png %{buildroot}%{_kde4_datadir}/wallpapers/leonidas-lion/contents
(cd %{buildroot}%{_kde4_datadir}/wallpapers/leonidas-lion/contents/images
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg 640x480.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 800x480.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg 800x600.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 1024x600.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg 1024x768.jpg
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 1152x720.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg 1152x864.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg 1200x900.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 1280x720.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 1280x768.jpg
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 1280x800.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg 1280x960.jpg
ln -s ../../../../backgrounds/leonidas/lion/normalish/1280x1024/leonidas-1-noon_right.jpg 1280x1024.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 1366x768.jpg
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 1440x900.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg 1440x1080.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg 1600x1200.jpg
ln -s ../../../../backgrounds/leonidas/lion/normalish/1280x1024/leonidas-1-noon_right.jpg 1600x1280.jpg
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 1680x1050.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 1920x1080.jpg
ln -s ../../../../backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg 1920x1200.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg 1920x1440.jpg
ln -s ../../../../backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg 2048x1536.jpg
)

# KDE 4 wallpapers theme landscape
mkdir -p %{buildroot}%{_kde4_datadir}/wallpapers/leonidas-landscape/contents/images
cp -rp wallpapers/leonidas-landscape/metadata.desktop %{buildroot}%{_kde4_datadir}/wallpapers/leonidas-landscape
cp -rp wallpapers/leonidas-landscape/screenshot.png %{buildroot}%{_kde4_datadir}/wallpapers/leonidas-landscape/contents
(cd %{buildroot}%{_kde4_datadir}/wallpapers/leonidas-landscape/contents/images
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 640x480.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 800x480.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 800x600.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 1024x600.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 1024x768.png
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 1152x720.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 1152x864.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 1200x900.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 1280x720.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 1280x768.png
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 1280x800.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 1280x960.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 1280x1024.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 1366x768.png
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 1440x900.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 1440x1080.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 1600x1200.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 1600x1280.png
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 1680x1050.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 1920x1080.png
ln -s ../../../../backgrounds/leonidas/landscape/wide/1920x1200/leonidas-1-noon_left.png 1920x1200.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 1920x1440.png
ln -s ../../../../backgrounds/leonidas/landscape/normal/1400x1050/leonidas-1-noon_left.png 2048x1536.png
)

%files
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/kdm/themes/leonidas/
%{_kde4_appsdir}/ksplash/Themes/Leonidas/
%{_kde4_datadir}/wallpapers/leonidas/
%{_kde4_appsdir}/kdm/pics/users/default_leonidas.png

%files lion
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_datadir}/wallpapers/leonidas-lion/

%files landscape
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_datadir}/wallpapers/leonidas-landscape/

%changelog
%autochangelog
