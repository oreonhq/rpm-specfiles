%global source0_hash 548480f58589a54b72d18833b755b15ffbd567e3187249d74e2e1f8f99f22fb4
%global tarball_version %(echo %{version} | tr '~' '.')
Name:           adwaita-icon-theme-legacy
Version:        46.2
Release:        1%{?dist}
Summary:        Full-color icons for the Adwaita icon theme
License:        LGPL-3.0-only OR CC-BY-SA-3.0
URL:            https://gitlab.gnome.org/GNOME/adwaita-icon-theme-legacy
Source0:        https://download.gnome.org/sources/%{name}/46/%{name}-%{version}.tar.xz
BuildArch:      noarch
Provides:       adwaita-legacy-icon-theme = %{version}-%{release}
# oreon:deps
BuildRequires:  meson
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles adwaita-icon-theme-legacy-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n adwaita-icon-theme-legacy-devel -f %{oreon_filedir}/adwaita-icon-theme-legacy-devel.list

%changelog

* Sat May 23 2026 Oreon Packaging Team <packaging@oreonhq.com> - 46.2-1
- Import for or11
