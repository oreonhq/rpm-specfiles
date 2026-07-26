%global source0_hash 916f3ccc10d8477ecd286aa8bc60171d5d5431ba01eeb9e60730c118166e6f37

Name:		constantine-kde-theme
Version:	12.1.0
Release:	32%{?dist}
Summary:	Constantine KDE Theme

License:	GPL-2.0-or-later AND CC-BY-SA-1.0

# We are upstream for this package
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:	https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	kde4-filesystem
Requires:	kde4-filesystem
Requires:	system-logos
Requires:	constantine-backgrounds-kde >= 12.0.0

Provides:	constantine-kdm-theme = %{version}-%{release}
Provides:	constantine-ksplash-theme = %{version}-%{release}

%if 0%{?fedora} == 12
Provides:	system-kde-theme = %{version}-%{release}
Provides:	system-kdm-theme = %{version}-%{release}
Provides:	system-ksplash-theme = %{version}-%{release}
%endif

# replace it later for el6
%if 0%{?rhel} == 6
Provides:   system-kde-theme = %{version}-%{release}
Provides:   system-kdm-theme = %{version}-%{release}
Provides:   system-ksplash-theme = %{version}-%{release}
%endif

%description
This is Constantine KDE Theme Artwork containing
KDM, KSplash, and wallpaper theme.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# blank

%install
rm -rf %{buildroot}

# KDM
mkdir -p %{buildroot}/%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/Constantine/ %{buildroot}/%{_kde4_appsdir}/kdm/themes/
(cd %{buildroot}/%{_kde4_appsdir}/kdm/themes/Constantine/
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine-640x480.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-800x480.png
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine-800x600.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-1024x600.png
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine-1024x768.png
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-1152x720.png
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine-1152x864.png
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine-1200x900.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-1280x720.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-1280x768.png
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-1280x800.png
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine-1280x960.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-1366x768.png
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-1440x900.png
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine-1440x1080.png
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine-1600x1200.png
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-1680x1050.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-1920x1080.png
ln -s ../../../../../backgrounds/constantine/default/wide/constantine.png constantine-1920x1200.png
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine-1920x1440.png
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine-2048x1536.png
# KDM falls back to this one if there's no match
ln -s ../../../../../backgrounds/constantine/default/standard/constantine.png constantine.png
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
)

#mkdir -p %{buildroot}/%{_kde4_appsdir}/kdm/pics/users
#cp -rp kdm/users %{buildroot}/%{_kde4_appsdir}/kdm/pics

# KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/Constantine/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
ln -s ../../../../../../backgrounds/constantine/default/standard/constantine.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Constantine/2048x1536/constantine.png
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Constantine/1920x1200/
ln -s ../../../../../../backgrounds/constantine/default/wide/constantine.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Constantine/1920x1200/constantine.png

# end finally drag logo
ln -s ../../../../../../pixmaps/system-logo-white.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Constantine/2048x1536/logo.png

%files
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/kdm/themes/Constantine/
%{_kde4_appsdir}/ksplash/Themes/Constantine/
#%{_kde4_appsdir}/kdm/pics/users/default_constantine.png

%changelog
%autochangelog
