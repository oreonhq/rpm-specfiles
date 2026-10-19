%global source0_hash 5057365f847253e0e275871441e10ff7846c8322a5d88e1e187d326de1cd8d00
Name: libXScrnSaver
Version: 1.2.5
Release:        1%{?dist}
Summary:        X.Org X11 libXss runtime library
License: X11
URL: http://www.x.org
Source0:        https://www.x.org/releases/individual/lib/libXScrnSaver-%{version}.tar.xz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
X.Org X11 libXss runtime library

%package devel
Summary: X.Org X11 libXScrnSaver development package
Requires: %{name} = %{version}-%{release}
%description devel
X.Org X11 libXss development package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

autoreconf -v --install --force
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure --disable-static
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libXScrnSaver-devel -f %{oreon_filedir}/libXScrnSaver-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.4-7
- Import
