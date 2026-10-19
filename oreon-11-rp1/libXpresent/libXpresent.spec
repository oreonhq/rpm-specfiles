%global source0_hash c11ae015141a9afbe10f4f2b8ee00b11adca6373dc1b9808d7c6c138b2da7b8a
Name:           libXpresent
Version:        1.0.0
Release:        1%{?dist}
Summary:        A Xlib-compatible API for the Present extension
License:        MIT
URL:            https://www.x.org
Source0:        https://xorg.freedesktop.org/archive/individual/lib/libXpresent-%{version}.tar.bz2
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(presentproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
This package contains header files and documentation for the Present
extension.  Library and server implementations are separate.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

autoreconf -v --install --force
%configure --disable-static
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libXpresent-devel -f %{oreon_filedir}/libXpresent-devel.list

%changelog

%autochangelog
