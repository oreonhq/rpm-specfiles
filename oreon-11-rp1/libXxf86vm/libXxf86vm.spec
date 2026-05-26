%global tarball libXxf86vm
#global gitdate 20130524
%global gitversion 4c4123441

Summary: X.Org X11 libXxf86vm runtime library
Name: libXxf86vm
Version: 1.1.6
Release: 4%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
License: X11-distribute-modifications-variant
URL: http://www.x.org

%if 0%{?gitdate}
Source0:        http://xorg.freedesktop.org/archive/individual/lib/libXxf86vm-1.1.6.tar.xz
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
Source0: http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 96af414c73ce1d5449ad04be7f9f27fa8330f844b6dda843ef22e3e1befb3ee3
%global source0_file libXxf86vm-1.1.6.tar.xz
# oreon url source checksums end
%endif

Requires: libX11 >= 1.5.99.902

BuildRequires: make
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig(xext) pkgconfig(xf86vidmodeproto)
BuildRequires: libX11-devel >= 1.5.99.902

%description
X.Org X11 libXxf86vm runtime library

%package devel
Summary: X.Org X11 libXxf86vm development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXxf86vm development package

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libXxf86vm-1.1.6.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "96af414c73ce1d5449ad04be7f9f27fa8330f844b6dda843ef22e3e1befb3ee3" || { echo "oreon: Source0 SHA256 mismatch for libXxf86vm-1.1.6.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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

%files
%doc README.md COPYING
%{_libdir}/libXxf86vm.so.1
%{_libdir}/libXxf86vm.so.1.0.0

%files devel
%{_libdir}/libXxf86vm.so
%{_libdir}/pkgconfig/xxf86vm.pc
%{_mandir}/man3/*.3*
%{_includedir}/X11/extensions/xf86vmode.h

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.6-4
- Prepare for Oreon 11 (RP1)
