%global source0_hash c8b43a6208145b87355c5d5d3e8b72e35bd1337e8bf76739c6a6e1a691de2b9c
%global srcname icons
%global appname io.elementary.icons
Name:           elementary-icon-theme
Summary:        Icons from the Elementary Project
Version:        9.0.0
Release:        1%{?dist}
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/icons
Source0:        https://github.com/elementary/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  librsvg2-tools
BuildRequires:  meson
BuildRequires:  xcursorgen
# /oreon:deps
%description
This is an icon theme designed to be smooth, sexy, clear, and efficient.

%package        gimp-palette
Summary:        Icons from the Elementary Project (GIMP palette)
Requires:       %{name} = %{version}-%{release}
Requires:       gimp
%description    gimp-palette
This is an icon theme designed to be smooth, sexy, clear, and efficient.

This package contains a palette file for the GIMP.

%package        inkscape-palette
Summary:        Icons from the Elementary Project (inkscape palette)
Requires:       %{name} = %{version}-%{release}
Requires:       inkscape
%description    inkscape-palette
This is an icon theme designed to be smooth, sexy, clear, and efficient.

This package contains a palette file for inkscape.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build

for i in $(find -type f -executable); do
    chmod a-x $i;
done
%meson -Dvolume_icons=false
%meson_build
%install
%meson_install
touch %{buildroot}/%{_datadir}/icons/elementary/icon-theme.cache
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml || :
%transfiletriggerin -- %{_datadir}/icons/elementary
gtk-update-icon-cache --force %{_datadir}/icons/elementary &>/dev/null || :
%transfiletriggerpostun -- %{_datadir}/icons/elementary
gtk-update-icon-cache --force %{_datadir}/icons/elementary &>/dev/null || :
%files -f %{oreon_filedir}/main.list
%files -n elementary-icon-theme-gimp-palette -f %{oreon_filedir}/elementary-icon-theme-gimp-palette.list
%files -n elementary-icon-theme-inkscape-palette -f %{oreon_filedir}/elementary-icon-theme-inkscape-palette.list

%changelog

%autochangelog
