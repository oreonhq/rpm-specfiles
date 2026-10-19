%global source0_hash 20771ef0c4e13e79b1d7c30e03def4f3ff6fc887778f6b8d610c6480c7a37747
Name:		laughlin-kde-theme
Version:	14.0.1
Release:        1%{?dist}
Summary:        Laughlin KDE Theme
License:	GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:        https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch
Requires:	kde4-filesystem
Requires:	system-logos
Requires:	laughlin-backgrounds-kde >= 14.0.0
Provides:	laughlin-kdm-theme = %{version}-%{release}
Provides:	laughlin-ksplash-theme = %{version}-%{release}
Provides:       laughlin-plasma-desktoptheme = %{version}-%{release}
# oreon:deps
BuildRequires:  kde4-filesystem
# /oreon:deps
%description
This is Laughlin KDE Theme Artwork containing
KDM theme, KSplash theme, Plasma desktop, and Plasma netbook theme.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Laughlin/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Laughlin-netbook/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/Laughlin/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/Laughlin/
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin-640x480.png
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-800x480.png
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin-800x600.png
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-1024x600.png
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin-1024x768.png
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-1152x720.png
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin-1152x864.png
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin-1200x900.png
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-1280x720.png
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-1280x768.png
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-1280x800.png
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin-1280x960.png
ln -s ../../../../../backgrounds/laughlin/default/normalish/laughlin.png laughlin-1280x1024.png
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-1366x768.png
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-1440x900.png
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin-1440x1080.png
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin-1600x1200.png
ln -s ../../../../../backgrounds/laughlin/default/normalish/laughlin.png laughlin-1600x1280.png
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-1680x1050.png
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-1920x1080.png
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-1920x1200.png
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin-1920x1440.png
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin-2048x1536.png
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin.png
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/Laughlin/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
ln -s ../../../../../../backgrounds/laughlin/default/standard/laughlin.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Laughlin/2048x1536/
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Laughlin/1920x1200/
ln -s ../../../../../../backgrounds/laughlin/default/wide/laughlin.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Laughlin/1920x1200/laughlin.png
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Laughlin/1280x1024/
ln -s ../../../../../../backgrounds/laughlin/default/normalish/laughlin.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Laughlin/1280x1024/
ln -s ../../../../../../pixmaps/system-logo-white.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Laughlin/2048x1536/logo.png
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
