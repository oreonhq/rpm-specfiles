%global source0_hash 9babbd3c86069c98563da044045fdc0ece4ec0c93dcdd2c68aa74eb34b4f3b77
%global tarball libFS
Summary:        X.Org X11 libFS runtime library
Name: libFS
Version: 1.0.10
Release:        1%{?dist}
License: MIT
URL: http://www.x.org
%if 0%{?gitdate}
Source0:        https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xorg-x11-util-macros
BuildRequires:  xorg-x11-xtrans-devel
# /oreon:deps
%description
X.Org X11 libFS runtime library

%package devel
Summary: X.Org X11 libFS development package
Requires: %{name} = %{version}-%{release}
%description devel
X.Org X11 libFS development package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build

autoreconf -v --install --force
%configure --disable-static
make
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_docdir}
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libFS-devel -f %{oreon_filedir}/libFS-devel.list

%changelog

%autochangelog
