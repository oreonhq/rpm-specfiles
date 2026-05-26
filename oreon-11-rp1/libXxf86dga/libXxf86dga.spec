%global tarball libXxf86dga
#global gitdate 20130524
%global gitversion a8dc6be32

Summary: X.Org X11 libXxf86dga runtime library
Name: libXxf86dga
Version: 1.1.6
Release: 7%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
License: MIT
URL: http://www.x.org

%if 0%{?gitdate}
Source0:        https://www.x.org/pub/individual/lib/libXxf86dga-1.1.6.tar.xz
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 be44427579808fe3a217d59f51cae756a26913eb6e4c8738ccab65ff56d7980f
%global source0_file libXxf86dga-1.1.6.tar.xz
# oreon url source checksums end
%endif

Requires: libX11 >= 1.5.99.902

BuildRequires: make
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig
BuildRequires: xorg-x11-proto-devel >= 7.4-32
BuildRequires: libX11-devel >= 1.5.99.902
BuildRequires: libXext-devel

%description
X.Org X11 libXxf86dga runtime library

%package devel
Summary: X.Org X11 libXxf86dga development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXxf86dga development package

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libXxf86dga-1.1.6.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "be44427579808fe3a217d59f51cae756a26913eb6e4c8738ccab65ff56d7980f" || { echo "oreon: Source0 SHA256 mismatch for libXxf86dga-1.1.6.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf -v --install --force
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%doc COPYING README.md
%{_libdir}/libXxf86dga.so.1
%{_libdir}/libXxf86dga.so.1.0.0

%files devel
%{_libdir}/libXxf86dga.so
%{_libdir}/pkgconfig/xxf86dga.pc
%{_mandir}/man3/*.3*
%{_includedir}/X11/extensions/xf86dga1.h
%{_includedir}/X11/extensions/Xxf86dga.h

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.6-7
- Import
