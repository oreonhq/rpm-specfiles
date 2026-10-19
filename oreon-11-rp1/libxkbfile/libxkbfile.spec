%global source0_hash 7f71884e5faf56fb0e823f3848599cf9b5a9afce51c90982baeb64f635233ebf
Summary:        X.Org X11 libxkbfile runtime library
Name: libxkbfile
Version: 1.2.0
Release:        1%{?dist}
License: MIT-open-group AND HPND AND SMLNJ
URL: http://www.x.org
Source0:        https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
X.Org X11 libxkbfile runtime library

%package devel
Summary: X.Org X11 libxkbfile development package
Requires: %{name} = %{version}-%{release}
%description devel
X.Org X11 libxkbfile development package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libxkbfile-devel -f %{oreon_filedir}/libxkbfile-devel.list

%changelog

%autochangelog
