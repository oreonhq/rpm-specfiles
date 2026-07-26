%global source0_hash 79586af479f8066830b28194c61124eb07e91f984dd7888c8482696c7486def6

Name:		beefy-miracle-kde-theme
Version:	16.91.0.3
Release:	26%{?dist}
Summary:	Beefy Miracle KDE Theme

License:	GPL-2.0-or-later AND CC-BY-SA-1.0

# We are upstream for this package
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:	https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	kde4-filesystem
Requires:	kde4-filesystem
Requires:	system-logos
Requires:	beefy-miracle-backgrounds-kde >= 16.91.0

Provides:	beefy-miracle-kdm-theme = %{version}-%{release}
Provides:	beefy-miracle-ksplash-theme = %{version}-%{release}
Provides:	beefy-miracle-plasma-desktoptheme = %{version}-%{release}

%if 0%{?fedora} == 17
Provides:	system-kde-theme = %{version}-%{release}
Provides:	system-kdm-theme = %{version}-%{release}
Provides:	system-ksplash-theme = %{version}-%{release}
Provides:	system-plasma-desktoptheme = %{version}-%{release}
%endif

%description
This is Beefy Miracle KDE Theme Artwork containing KDM theme,
KSplash theme and Plasma Workspaces theme.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# blank

%install
rm -rf %{buildroot}

### Plasma desktoptheme's
mkdir -p %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Beefy_Miracle/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Beefy_Miracle-netbook/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
# the branding image branding.svgz is still missing in fedora-logos
# we should add it in next fedora release
# pushd %{buildroot}%{_kde4_appsdir}/desktoptheme/widgets/
# ln -s ../../../../../../pixmaps/branding.svgz branding.svgz
# popd

### KDM
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/BeefyMiracle/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/BeefyMiracle/
# system logo
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd

## KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/BeefyMiracle/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
ln -s ../../../../../../backgrounds/beefy-miracle/default/standard/beefy-miracle.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/BeefyMiracle/2048x1536/
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/BeefyMiracle/1920x1200/
ln -s ../../../../../../backgrounds/beefy-miracle/default/wide/beefy-miracle.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/BeefyMiracle/1920x1200/beefy-miracle.png
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/BeefyMiracle/1280x1024/
ln -s ../../../../../../backgrounds/beefy-miracle/default/normalish/beefy-miracle.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/BeefyMiracle/1280x1024/
 
# system logo 
ln -s ../../../../../../pixmaps/system-logo-white.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/BeefyMiracle/2048x1536/logo.png

%files
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/desktoptheme/Beefy_Miracle/
%{_kde4_appsdir}/desktoptheme/Beefy_Miracle-netbook/
%{_kde4_appsdir}/kdm/themes/BeefyMiracle/
%{_kde4_appsdir}/ksplash/Themes/BeefyMiracle/

%changelog
%autochangelog
