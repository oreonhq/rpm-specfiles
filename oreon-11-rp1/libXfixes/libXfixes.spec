%global tarball libXfixes
#global gitdate 20130524
%global gitversion c480fe327

Summary: X Fixes library
Name: libXfixes
Version: 6.0.1
Release: 7%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
License: MIT AND HPND-sell-variant
URL: http://www.x.org

%if 0%{?gitdate}
Source0:    %{tarball}-%{gitdate}.tar.xz
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
Source0: http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz
%endif

Requires: libX11 >= 1.6

BuildRequires: make
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig(fixesproto) pkgconfig(xext)
BuildRequires: libX11-devel >= 1.5.99.902

%description
X Fixes library.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
libXfixes development package

%prep
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf -v --install --force
%configure --disable-static
make V=1 %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%doc AUTHORS COPYING README.md
%{_libdir}/libXfixes.so.3
%{_libdir}/libXfixes.so.3.1.0

%files devel
%{_includedir}/X11/extensions/Xfixes.h
%{_libdir}/libXfixes.so
%{_libdir}/pkgconfig/xfixes.pc
%{_mandir}/man3/Xfixes.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.0.1-7
- Prepare for Oreon 11 (RP1)
