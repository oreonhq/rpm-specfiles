%global source0_hash cdf28cd79758dc95ee0650dd9924482d928e315c8e553c52d926fe124bd50206

Name:		solar-kde-theme
Version:	0.1.19
Release:	29%{?dist}
Summary:	Solar KDE Theme

# Automatically converted from old format: GPLv2 and CC-BY-SA - review is highly recommended.
License:	GPL-2.0-only AND LicenseRef-Callaway-CC-BY-SA
# We are upstream for this package
URL:            https://fedorahosted.org/fedora-kde-artwork/
Source0:        https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	kde4-filesystem
Requires:	kde4-filesystem
Requires:	system-logos
Requires:	solar-backgrounds-common >= 0.91.0
%if 0%{?fedora} > 10
# for Leonidas system logo
Requires:	leonidas-kde-theme
%endif

%description
Solar KDE Theme based on Solar theme by Samuele Storari. This package
contains KDM Solar Mania theme, KSplash Solar Comet theme and Solar background.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# blank

%install
rm -rf %{buildroot}

# wallpapers
mkdir -p %{buildroot}%{_kde4_datadir}/wallpapers
ln -sf ../backgrounds/solar/standard/2048x1536/solar-0-morn.png %{buildroot}%{_kde4_datadir}/wallpapers/solar.png
ln -sf ../backgrounds/solar/wide/1920x1200/solar-0-morn.png %{buildroot}%{_kde4_datadir}/wallpapers/solar_wide.png
ln -sf ../backgrounds/solar/normalish/1280x1024/solar-0-morn.png %{buildroot}%{_kde4_datadir}/wallpapers/solar_high.png

# KDM
mkdir -p %{buildroot}/%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/SolarMania/ %{buildroot}/%{_kde4_appsdir}/kdm/themes/
(cd %{buildroot}/%{_kde4_appsdir}/kdm/themes/SolarMania/
ln -s ../../../../../wallpapers/solar.png solar-640x480.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../wallpapers/solar_wide.png solar-800x480.png
ln -s ../../../../../wallpapers/solar.png solar-800x600.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../wallpapers/solar_wide.png solar-1024x600.png
ln -s ../../../../../wallpapers/solar.png solar-1024x768.png
ln -s ../../../../../wallpapers/solar_wide.png solar-1152x720.png
ln -s ../../../../../wallpapers/solar.png solar-1152x864.png
ln -s ../../../../../wallpapers/solar.png solar-1200x900.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../wallpapers/solar_wide.png solar-1280x720.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../wallpapers/solar_wide.png solar-1280x768.png
ln -s ../../../../../wallpapers/solar_wide.png solar-1280x800.png
ln -s ../../../../../wallpapers/solar.png solar-1280x960.png
ln -s ../../../../../wallpapers/solar_high.png solar-1280x1024.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../wallpapers/solar_wide.png solar-1366x768.png
ln -s ../../../../../wallpapers/solar_wide.png solar-1440x900.png
ln -s ../../../../../wallpapers/solar.png solar-1440x1080.png
ln -s ../../../../../wallpapers/solar.png solar-1600x1200.png
ln -s ../../../../../wallpapers/solar_high.png solar-1600x1280.png
ln -s ../../../../../wallpapers/solar_wide.png solar-1680x1050.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../wallpapers/solar_wide.png solar-1920x1080.png
ln -s ../../../../../wallpapers/solar_wide.png solar-1920x1200.png
ln -s ../../../../../wallpapers/solar.png solar-1920x1440.png
ln -s ../../../../../wallpapers/solar.png solar-2048x1536.png
# KDM falls back to this one if there's no match
ln -s ../../../../../wallpapers/solar.png solar.png
)

mkdir -p %{buildroot}/%{_kde4_appsdir}/kdm/pics/users
cp -rp kdm/users %{buildroot}/%{_kde4_appsdir}/kdm/pics

# KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/SolarComet/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SolarComet/2048x1536
ln -s ../../../../../../wallpapers/solar.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SolarComet/2048x1536/solar.png
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SolarComet/1920x1200
ln -s ../../../../../../wallpapers/solar_wide.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SolarComet/1920x1200/solar.png
ln -s ../../../../../../wallpapers/solar_high.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SolarComet/1280x1024/solar.png

%if 0%{?fedora} > 10
# we have to drag Leonidas ksplash theme directory for F11
ln -s %{_kde4_appsdir}/ksplash/Themes/Leonidas/2048x1536/logo.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SolarComet/1280x1024/logo.png
%endif

# KDE 4 wallpapers theme
mkdir -p %{buildroot}%{_kde4_datadir}/wallpapers/Solar/contents/images
cp -rp wallpapers/Solar/metadata.desktop %{buildroot}%{_kde4_datadir}/wallpapers/Solar
cp -rp wallpapers/Solar/screenshot.png %{buildroot}%{_kde4_datadir}/wallpapers/Solar/contents
(cd %{buildroot}%{_kde4_datadir}/wallpapers/Solar/contents/images
ln -s ../../../solar.png 640x480.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../solar_wide.png 800x480.png
ln -s ../../../solar.png 800x600.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../solar_wide.png 1024x600.png
ln -s ../../../solar.png 1024x768.png
ln -s ../../../solar_wide.png 1152x720.png
ln -s ../../../solar.png 1152x864.png
ln -s ../../../solar.png 1200x900.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../solar_wide.png 1280x720.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../solar_wide.png 1280x768.png
ln -s ../../../solar_wide.png 1280x800.png
ln -s ../../../solar.png 1280x960.png
ln -s ../../../solar_high.png 1280x1024.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../solar_wide.png 1366x768.png
ln -s ../../../solar_wide.png 1440x900.png
ln -s ../../../solar.png 1440x1080.png
ln -s ../../../solar.png 1600x1200.png
ln -s ../../../solar_high.png 1600x1280.png
ln -s ../../../solar_wide.png 1680x1050.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../solar_wide.png 1920x1080.png
ln -s ../../../solar_wide.png 1920x1200.png
ln -s ../../../solar.png 1920x1440.png
ln -s ../../../solar.png 2048x1536.png
)

%files
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/kdm/themes/SolarMania/
%{_kde4_appsdir}/ksplash/Themes/SolarComet/
%{_kde4_datadir}/wallpapers/solar.png
%{_kde4_datadir}/wallpapers/solar_wide.png
%{_kde4_datadir}/wallpapers/solar_high.png
%{_kde4_datadir}/wallpapers/Solar/
%{_kde4_appsdir}/kdm/pics/users/default_solar.png

%changelog
%autochangelog
