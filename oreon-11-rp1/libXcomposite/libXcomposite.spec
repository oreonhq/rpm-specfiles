%global source0_hash 8bdf310967f484503fa51714cf97bff0723d9b673e0eecbf92b3f97c060c8ccb
Summary:        X Composite Extension library
Name: libXcomposite
Version: 0.4.7
Release:        1%{?dist}
License: MIT AND HPND-sell-variant
URL: http://www.x.org
Source0:        https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(compositeproto)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
X Composite Extension library

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
%description devel
X.Org X11 libXcomposite development package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

autoreconf -v --install --force
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
%files -n libXcomposite-devel -f %{oreon_filedir}/libXcomposite-devel.list

%changelog

%autochangelog
