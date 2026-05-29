%global source0_hash none

%global tarball_version %(echo %{version} | tr '~' '.')

Name:           adwaita-icon-theme-legacy
Version:        46.2
Release:        1%{?dist}
Summary:        Full-color icons for the Adwaita icon theme

License:        LGPL-3.0-only OR CC-BY-SA-3.0
URL:            https://gitlab.gnome.org/GNOME/adwaita-icon-theme-legacy
Source0: https://download.gnome.org/sources/adwaita-icon-theme-legacy/46/adwaita-icon-theme-legacy-%{tarball_version}.tar.xz
BuildArch:      noarch

BuildRequires:  meson

Provides:       adwaita-legacy-icon-theme = %{version}-%{release}

%description
This package contains the full color Adwaita icons for the Adwaita icon theme
used by the GNOME desktop.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

Provides:       adwaita-legacy-icon-theme-devel = %{version}-%{release}

%description    devel
The %{name}-devel package contains the pkgconfig file for
developing applications that use %{name}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{name}-%{tarball_version}
sed -i '/^gtk_update_icon_cache = find_program(/,/^)$/d' meson.build
sed -i '/^meson.add_install_script(/,/^)$/d' meson.build

%build
%meson
%meson_build

%install
%meson_install

rm -rf %{buildroot}%{_licensedir}/adwaita-icon-theme

find %{buildroot} -name ".placeholder" -delete
find %{buildroot} -name ".empty" -delete

touch %{buildroot}%{_datadir}/icons/AdwaitaLegacy/.icon-theme.cache

%transfiletriggerin -- %{_datadir}/icons/AdwaitaLegacy
gtk-update-icon-cache --force %{_datadir}/icons/AdwaitaLegacy &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/AdwaitaLegacy
gtk-update-icon-cache --force %{_datadir}/icons/AdwaitaLegacy &>/dev/null || :

%files
%license COPYING*
%dir %{_datadir}/icons/AdwaitaLegacy/
%{_datadir}/icons/AdwaitaLegacy/8x8/
%{_datadir}/icons/AdwaitaLegacy/16x16/
%{_datadir}/icons/AdwaitaLegacy/22x22/
%{_datadir}/icons/AdwaitaLegacy/24x24/
%{_datadir}/icons/AdwaitaLegacy/32x32/
%{_datadir}/icons/AdwaitaLegacy/48x48/
%{_datadir}/icons/AdwaitaLegacy/index.theme
%ghost %{_datadir}/icons/AdwaitaLegacy/.icon-theme.cache

%files devel
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Sat May 23 2026 Oreon Packaging Team <packaging@oreonhq.com> - 46.2-1
- Import for or11
