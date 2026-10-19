%global source0_hash ba561cf3c96305a47179fa5605856ad695c9238ea07f7093aebd9ba80c4e323b
%global adwlegacy_ver 46.2
%global tarball_version %(echo %{version} | tr '~' '.')
Name:           adwaita-icon-theme
Version:        51.0
Release:        1%{?dist}
Summary:        Adwaita icon theme
License:        LGPL-3.0-only OR CC-BY-SA-3.0
URL:            https://gitlab.gnome.org/GNOME/adwaita-icon-theme
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
BuildArch:      noarch
%if 0%{?fedora} || (0%{?oreon} >= 11)
Requires:       %{name}-legacy >= %{adwlegacy_ver}
%endif
Requires:       adwaita-cursor-theme = %{version}-%{release}
# oreon:deps
BuildRequires:  meson
# /oreon:deps
%description
This package contains the Adwaita icon theme used by the GNOME desktop.

%package -n     adwaita-cursor-theme
Summary:        Adwaita cursor theme
%description -n adwaita-cursor-theme
The adwaita-cursor-theme package contains a modern set of cursors originally
designed for the GNOME desktop.

%package        devel
Summary:        Development files for %{name}
%if 0%{?fedora} || (0%{?oreon} >= 11)
Requires:       %{name}-legacy-devel >= %{adwlegacy_ver}
%endif
Requires:       %{name} = %{version}-%{release}
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
touch $RPM_BUILD_ROOT%{_datadir}/icons/Adwaita/.icon-theme.cache
%transfiletriggerin -- %{_datadir}/icons/Adwaita
gtk-update-icon-cache --force %{_datadir}/icons/Adwaita &>/dev/null || :
%transfiletriggerpostun -- %{_datadir}/icons/Adwaita
gtk-update-icon-cache --force %{_datadir}/icons/Adwaita &>/dev/null || :
%oreon_autofiles adwaita-cursor-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles adwaita-icon-theme-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n adwaita-cursor-theme -f %{oreon_filedir}/adwaita-cursor-theme.list
%files -n adwaita-icon-theme-devel -f %{oreon_filedir}/adwaita-icon-theme-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50~rc-1
- Prepare for Oreon 11 (RP1)
