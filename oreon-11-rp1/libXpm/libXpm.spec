%global source0_hash ad3576d689221a39dc728f0e0dc02ca7bb6a0d724c9a77fd1bfa1e9af83be900
Summary:        X.Org X11 libXpm runtime library
Name: libXpm
Version: 3.5.19
Release:        1%{?dist}
License: MIT AND X11-distribute-modifications-variant
URL: http://www.x.org
Source0:        https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  gzip
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncompress
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xt)
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
X.Org X11 libXpm runtime library

%package devel
Summary: X.Org X11 libXpm development package
Requires: %{name} = %{version}-%{release}
%description devel
X.Org X11 libXpm development package

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
%files -n libXpm-devel -f %{oreon_filedir}/libXpm-devel.list

%changelog

%autochangelog
