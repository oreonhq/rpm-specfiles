%global source0_hash f29f0e4bb86e12d2f832c0c117a0de219358815ed3a4d39511a273b84271e75a
Name:		beefy-miracle-kde-theme
Version:	16.91.0.3
Release:        26%{?dist}
Summary:        Beefy Miracle KDE Theme
License:	GPL-2.0-or-later AND CC-BY-SA-1.0
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:        https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch
Requires:	kde4-filesystem
Requires:	system-logos
Requires:	beefy-miracle-backgrounds-kde >= 16.91.0
Provides:	beefy-miracle-kdm-theme = %{version}-%{release}
Provides:	beefy-miracle-ksplash-theme = %{version}-%{release}
Provides:	beefy-miracle-plasma-desktoptheme = %{version}-%{release}
# oreon:deps
BuildRequires:  kde4-filesystem
# /oreon:deps
%description
This is Beefy Miracle KDE Theme Artwork containing KDM theme,
KSplash theme and Plasma Workspaces theme.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Beefy_Miracle/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Beefy_Miracle-netbook/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/BeefyMiracle/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/BeefyMiracle/
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd
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
ln -s ../../../../../../pixmaps/system-logo-white.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/BeefyMiracle/2048x1536/logo.png
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
