%global source0_hash 28434604a7b038731ac0231731388ff104f565bb2330cc24e78cda04cfd3ef7d
Name:           libgnome-games-support1
Version:        2.0.2
Release:        1%{?dist}
Summary:        Support library for GNOME games
License:        LGPLv3+
URL:            https://gitlab.gnome.org/GNOME/libgnome-games-support/
Source0:        https://download.gnome.org/sources/libgnome-games-support/1.8/libgnome-games-support-%{version}.tar.xz
Conflicts:      libgnome-games-support < 2.0.0
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  vala
# /oreon:deps
%description
libgnome-games-support is a small library intended for internal use
by GNOME Games, but it may be used by others.
The API will only break with the major version number.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      libgnome-games-support-devel < 2.0.0
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libgnome-games-support-%{version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang libgnome-games-support
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libgnome-games-support1-devel -f %{oreon_filedir}/libgnome-games-support1-devel.list

%changelog

%autochangelog
