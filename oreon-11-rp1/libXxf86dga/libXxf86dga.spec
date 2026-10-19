%global source0_hash b3be5b444d324cb6e0f4b5019a4972c99ea336ccb8ab7968eccefecd917ffde6
%global tarball libXxf86dga
%global gitversion a8dc6be32
Summary:        X.Org X11 libXxf86dga runtime library
Name: libXxf86dga
Version: 1.1.7
Release:        1%{?dist}
License: MIT
URL: http://www.x.org
%if 0%{?gitdate}
Source0:        https://www.x.org/releases/individual/lib/libXxf86dga-1.1.7.tar.xz
Source1:        make-git-snapshot.sh
Source2:        commitid
%else
%endif
Requires: libX11 >= 1.5.99.902
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
X.Org X11 libXxf86dga runtime library

%package devel
Summary: X.Org X11 libXxf86dga development package
Requires: %{name} = %{version}-%{release}
%description devel
X.Org X11 libXxf86dga development package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build

autoreconf -v --install --force
%configure --disable-static
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libXxf86dga-devel -f %{oreon_filedir}/libXxf86dga-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.6-7
- Import
