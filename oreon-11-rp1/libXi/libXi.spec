%global source0_hash 7ad60056f01af4f786cfe93b3a7707447711626fc8da2637bec71a90409babe5
%global tarball libXi
%global gitversion 661c45ca1
Summary:        X.Org X11 libXi runtime library
Name: libXi
Version: 1.8.3
Release:        1%{?dist}
License: MIT-open-group AND SMLNJ AND MIT
URL: http://www.x.org
%if 0%{?gitdate}
Source0:        https://xorg.freedesktop.org/releases/individual/lib/libXi-1.8.3.tar.xz
Source1:        make-git-snapshot.sh
%else
%endif
Requires: libX11 >= 1.5.99.902
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  xmlto
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
X.Org X11 libXi runtime library

%package devel
Summary: X.Org X11 libXi development package
Requires: %{name} = %{version}-%{release}
Requires: xorg-x11-proto-devel
Requires: pkgconfig
%description devel
X.Org X11 libXi development package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build

autoreconf -v --install || exit 1
%configure --disable-specs \
	   --disable-static
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libXi-devel -f %{oreon_filedir}/libXi-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.3-1
- Import
