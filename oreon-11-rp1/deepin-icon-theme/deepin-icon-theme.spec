%global source0_hash e4c9470d3f4f2064ff89eeafc3cc105f16ec1eddd8a97d75580639a21e115505
%global themes bloom bloom-dark bloom-classic bloom-classic-dark Sea vintage
%global start_logo start-here
Name:           deepin-icon-theme
Version:        2026.02.27
Release:        1%{?dist}
Summary:        Icons for the Deepin Desktop Environment
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-icon-theme
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       papirus-icon-theme
Requires:       fedora-logos
# oreon:deps
BuildRequires:  /usr/bin/python
BuildRequires:  fedora-logos
BuildRequires:  gtk-update-icon-cache
BuildRequires:  make
BuildRequires:  xcursorgen
# /oreon:deps
%description
%{summary}.

%prep
%oreon_prep
%build

%make_build
%install
%make_install
cp -a ./Sea ./usr/share/icons/hicolor %{buildroot}%{_datadir}/icons
for theme in %{themes}; do
    for dir in %{buildroot}%{_datadir}/icons/$theme/places/*; do
        size=$(basename $dir)
        if [ -f %{_datadir}/icons/hicolor/${size}x${size}/places/%{start_logo}.png ]; then
            ln -sf ../../../hicolor/${size}x${size}/places/%{start_logo}.png $dir
        elif [ -f %{_datadir}/icons/hicolor/${size}/places/%{start_logo}.svg ]; then
            ln -sf ../../../hicolor/${size}/places/%{start_logo}.svg $dir
        fi
    done
    touch %{buildroot}%{_datadir}/icons/$theme/icon-theme.cache
done
%oreon_autofiles main

%post

for theme in %{themes}; do
  touch --no-create %{_datadir}/icons/$theme &>/dev/null || :
done
%postun

if [ $1 -eq 0 ] ; then
  for theme in %{themes}; do
    touch --no-create %{_datadir}/icons/$theme &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$theme &>/dev/null || :
  done
fi
%posttrans

for theme in %{themes}; do
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$theme &>/dev/null || :
done
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
