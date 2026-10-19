%global source0_hash ae50c0f669e0af5a67cc4cd0f54f21d64a64d2660af883e80e95d3fe51b945d8
%global tarball libXxf86vm
%global gitversion 4c4123441
Summary:        X.Org X11 libXxf86vm runtime library
Name: libXxf86vm
Version: 1.1.7
Release:        1%{?dist}
License: X11-distribute-modifications-variant
URL: http://www.x.org
%if 0%{?gitdate}
Source0:        https://www.x.org/archive/individual/lib/%{name}-%{version}.tar.xz
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
%endif
Requires: libX11 >= 1.5.99.902
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libX11-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xf86vidmodeproto)
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
X.Org X11 libXxf86vm runtime library

%package devel
Summary: X.Org X11 libXxf86vm development package
Requires: %{name} = %{version}-%{release}
%description devel
X.Org X11 libXxf86vm development package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build

autoreconf -v --install --force
%configure --disable-static
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libXxf86vm-devel -f %{oreon_filedir}/libXxf86vm-devel.list

%changelog

%autochangelog
