%global source0_hash c0ef3c0776ce4269fdff94698f26232dee7852b0179920e4b1a92dfa125262ac

Name:		verne-kde-theme
Version:	15.91.1
Release:	24%{?dist}
Summary:	Verne KDE Theme

# Automatically converted from old format: GPLv2+ and CC-BY-SA - review is highly recommended.
License:	GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA

# We are upstream for this package
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:	https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	kde4-filesystem
Requires:	kde4-filesystem
Requires:	system-logos
Requires:	verne-backgrounds-kde >= %{version}

Provides:	verne-kdm-theme = %{version}-%{release}
Provides:	verne-ksplash-theme = %{version}-%{release}
Provides:	verne-plasma-desktoptheme = %{version}-%{release}

%if 0%{?fedora} == 16
Provides:	system-kde-theme = %{version}-%{release}
Provides:	system-kdm-theme = %{version}-%{release}
Provides:	system-ksplash-theme = %{version}-%{release}
Provides:	system-plasma-desktoptheme = %{version}-%{release}
%endif

%description
This is Verne KDE Theme Artwork containing KDM theme,
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
cp -rp desktoptheme/Verne/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Verne-netbook/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
# the branding image branding.svgz is still missing in fedora-logos
# we should add it in next fedora release
# pushd %{buildroot}%{_kde4_appsdir}/desktoptheme/widgets/
# ln -s ../../../../../../pixmaps/branding.svgz branding.svgz
# popd

### KDM
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/Verne/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/Verne/
# system logo
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd

## KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/Verne/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
ln -s ../../../../../../backgrounds/verne/default/standard/verne.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Verne/2048x1536/
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Verne/1920x1200/
ln -s ../../../../../../backgrounds/verne/default/wide/verne.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Verne/1920x1200/verne.png
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Verne/1280x1024/
ln -s ../../../../../../backgrounds/verne/default/normalish/verne.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Verne/1280x1024/
 
# system logo 
ln -s ../../../../../../pixmaps/system-logo-white.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Verne/2048x1536/logo.png

%files
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/desktoptheme/Verne/
%{_kde4_appsdir}/desktoptheme/Verne-netbook/
%{_kde4_appsdir}/kdm/themes/Verne/
%{_kde4_appsdir}/ksplash/Themes/Verne/

%changelog
%autochangelog
