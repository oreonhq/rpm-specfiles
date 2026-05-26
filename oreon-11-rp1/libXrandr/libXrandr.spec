%global tarball libXrandr
#global gitdate 20130524
%global gitversion c90f74497

Summary: X.Org X11 libXrandr runtime library
Name: libXrandr
Version: 1.5.4
Release: 8%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
License: HPND-sell-variant
URL: http://www.x.org

%if 0%{?gitdate}
Source0:        https://xorg.freedesktop.org/archive/individual/lib/libXrandr-1.5.4.tar.xz
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
Source0: https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 1ad5b065375f4a85915aa60611cc6407c060492a214d7f9daf214be752c3b4d3
%global source0_file libXrandr-1.5.4.tar.xz
# oreon url source checksums end
%endif

Requires: libX11 >= 1.6.0

BuildRequires: make
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: xorg-x11-proto-devel
BuildRequires: pkgconfig(randrproto) >= 1.5.0
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(x11) >= 1.6.0

%description
X.Org X11 libXrandr runtime library

%package devel
Summary: X.Org X11 libXrandr development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXrandr development package

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libXrandr-1.5.4.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1ad5b065375f4a85915aa60611cc6407c060492a214d7f9daf214be752c3b4d3" || { echo "oreon: Source0 SHA256 mismatch for libXrandr-1.5.4.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf -v --install --force
%configure  --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%doc AUTHORS COPYING
%{_libdir}/libXrandr.so.2
%{_libdir}/libXrandr.so.2.2.0

%files devel
%{_includedir}/X11/extensions/Xrandr.h
%{_libdir}/libXrandr.so
%{_libdir}/pkgconfig/xrandr.pc
%{_mandir}/man3/*.3*

%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.4-8
- Drop commented man3x line (rpmbuild expands macros in comments)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.4-7
- Prepare for Oreon 11 (RP1)
