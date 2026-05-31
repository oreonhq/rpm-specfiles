%global source0_hash 7ad60056f01af4f786cfe93b3a7707447711626fc8da2637bec71a90409babe5

%global tarball libXi
#global gitdate 20130524
%global gitversion 661c45ca1

Summary: X.Org X11 libXi runtime library
Name: libXi
Version: 1.8.3
Release: 1%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
License: MIT-open-group AND SMLNJ AND MIT
URL: http://www.x.org

%if 0%{?gitdate}
Source0:        https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
Source1:    make-git-snapshot.sh
%else
Source0:        https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
%endif

BuildRequires: make
BuildRequires: autoconf automake libtool
BuildRequires: xorg-x11-util-macros
BuildRequires: xorg-x11-proto-devel
BuildRequires: pkgconfig(inputproto) >= 2.3.99.1
BuildRequires: libX11-devel >= 1.5.99.902
BuildRequires: libXext-devel libXfixes-devel
BuildRequires: xmlto asciidoc >= 8.4.5

Requires: libX11 >= 1.5.99.902

%description
X.Org X11 libXi runtime library

%package devel
Summary: X.Org X11 libXi development package
Requires: %{name} = %{version}-%{release}
# required by xi.pc
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

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%doc COPYING
%{_libdir}/libXi.so.6
%{_libdir}/libXi.so.6.1.0

%files devel
%{_includedir}/X11/extensions/XInput.h
%{_includedir}/X11/extensions/XInput2.h
%{_libdir}/libXi.so
%{_libdir}/pkgconfig/xi.pc
%{_mandir}/man3/*.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.3-1
- Import
