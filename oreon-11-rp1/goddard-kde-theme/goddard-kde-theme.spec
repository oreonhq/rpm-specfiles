%global source0_hash 97cc0368a8640916b6257fe34092e76c077e962c2e7e7fd9352e79be572f569d

Name:		goddard-kde-theme
Version:	13.1.1
Release:	24%{?dist}
Summary:	Goddard KDE Theme

License:	GPL-2.0-or-later AND CC-BY-SA-1.0

# We are upstream for this package
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:	https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	kde4-filesystem
Requires:	kde4-filesystem
Requires:	system-logos
Requires:	goddard-backgrounds-kde >= 13.0.0 

Provides:	goddard-kdm-theme = %{version}-%{release}
Provides:	goddard-ksplash-theme = %{version}-%{release}
Provides:       goddard-plasma-desktoptheme = %{version}-%{release}

%if 0%{?fedora} == 13
Provides:	system-kde-theme = %{version}-%{release}
Provides:	system-kdm-theme = %{version}-%{release}
Provides:	system-ksplash-theme = %{version}-%{release}
Provides:       system-plasma-desktoptheme = %{version}-%{release}
%endif

%description
This is Goddard KDE Theme Artwork containing
KDM theme, KSplash theme, Plasma desktop, and Plasma netbook theme.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# blank

%install
rm -rf %{buildroot}

### Plasma desktoptheme's
mkdir -p %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Goddard/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Goddard-netbook/ %{buildroot}%{_kde4_appsdir}/desktoptheme/

### KDM
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/Goddard/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/Goddard/
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard-640x480.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-800x480.jpg
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard-800x600.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-1024x600.jpg
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard-1024x768.jpg
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-1152x720.jpg
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard-1152x864.jpg
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard-1200x900.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-1280x720.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-1280x768.jpg
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-1280x800.jpg
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard-1280x960.jpg
ln -s ../../../../../backgrounds/goddard/default/normalish/goddard.jpg goddard-1280x1024.jpg

# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-1366x768.jpg
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-1440x900.jpg
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard-1440x1080.jpg
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard-1600x1200.jpg
ln -s ../../../../../backgrounds/goddard/default/normalish/goddard.jpg goddard-1600x1280.jpg
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-1680x1050.jpg
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-1920x1080.jpg
ln -s ../../../../../backgrounds/goddard/default/wide/goddard.jpg goddard-1920x1200.jpg
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard-1920x1440.jpg
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard-2048x1536.jpg
# KDM falls back to this one if there's no match
ln -s ../../../../../backgrounds/goddard/default/standard/goddard.jpg goddard.jpg
# system logo
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd

## KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/Goddard/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
# goddard.png is not provided by goddard-backgrounds and is now embedded in the ksplash theme, no need for symlinks
#ln -s ../../../../../../backgrounds/goddard/default/standard/goddard.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Goddard/1400x1050/goddard.png
#mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Goddard/1280x800/
#ln -s ../../../../../../backgrounds/goddard/default/wide/goddard.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Goddard/1280x800/goddard.png

# system logo 
ln -s ../../../../../../pixmaps/system-logo-white.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Goddard/1400x1050/logo.png

%files
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/desktoptheme/Goddard/
%{_kde4_appsdir}/desktoptheme/Goddard-netbook/
%{_kde4_appsdir}/kdm/themes/Goddard/
%{_kde4_appsdir}/ksplash/Themes/Goddard/

%changelog
%autochangelog
