%global source0_hash 4b11f4331286ac0800a51c54103f13b7aabfaa6a50571889329e5bf4b408a149
%global backgrounds_kde_version 14.91.1
Name:		lovelock-kde-theme
Version:	14.92.1
Release:        1%{?dist}
Summary:        Lovelock KDE Theme
License:	GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:        https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch
Requires:	kde4-filesystem
Requires:	system-logos
Requires:	lovelock-backgrounds-kde >= %{backgrounds_kde_version}
Provides:	lovelock-kdm-theme = %{version}-%{release}
Provides:	lovelock-ksplash-theme = %{version}-%{release}
Provides:	lovelock-plasma-desktoptheme = %{version}-%{release}
# oreon:deps
BuildRequires:  kde4-filesystem
# /oreon:deps
%description
This is Lovelock KDE Theme Artwork containing KDM theme,
KSplash theme and Plasma Workspaces theme.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Lovelock/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Lovelock-netbook/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/Lovelock/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/Lovelock/
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/Lovelock/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
ln -s ../../../../../../backgrounds/lovelock/default/standard/lovelock.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Lovelock/2048x1536/
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Lovelock/1920x1200/
ln -s ../../../../../../backgrounds/lovelock/default/wide/lovelock.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Lovelock/1920x1200/lovelock.png
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Lovelock/1280x1024/
ln -s ../../../../../../backgrounds/lovelock/default/normalish/lovelock.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Lovelock/1280x1024/
ln -s ../../../../../../pixmaps/system-logo-white.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Lovelock/2048x1536/logo.png
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
