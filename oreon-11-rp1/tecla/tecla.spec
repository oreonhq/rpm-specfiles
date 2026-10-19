%global source0_hash ddf1a8555044171d0d84b580d6d541c3c621ae77996f6bc5edde598de2f8625b
Name:           tecla
Version:        51.0
Release:        1%{?dist}
Summary:        Keyboard layout viewer
License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/tecla
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-wayland)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)
# /oreon:deps
%description
Tecla is a keyboard layout viewer. It uses GTK/Libadwaita for UI, and
libxkbcommon to deal with keyboard maps.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains a pkg-config file for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir tecla-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang tecla
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Tecla.desktop
%meson_test
%files -f %{oreon_filedir}/main.list
%files -n tecla-devel -f %{oreon_filedir}/tecla-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Import
