%global source0_hash 22dc59566d73c0065350f5a97340e62ecc7b08c4df19183804bb8be24c8fe870
Name:           libgnomekbd
Version:        3.28.1
Release:        9%{?dist}
Summary:        A keyboard configuration library
License:        LGPL-2.0-or-later
URL:            http://gswitchit.sourceforge.net
Source0:        https://download.gnome.org/sources/libgnomekbd/3.28/libgnomekbd-%{version}.tar.xz
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  libxklavier-devel
BuildRequires:  meson
# /oreon:deps
%description
The libgnomekbd package contains a GNOME library which manages
keyboard configuration and offers various widgets related to
keyboard configuration.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The libgnomekbd-devel package contains libraries and header files for
developing applications that use libgnomekbd.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/gkbd-keyboard-display.desktop
%files -f %{oreon_filedir}/main.list
%files -n libgnomekbd-devel -f %{oreon_filedir}/libgnomekbd-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.28.1-9
- Import
