%global source0_hash 7d34910958e1c1f8d193d828fea1b7da192297280a35437af0692f003ba03755

%global tarball libXv
#global gitdate 20130524
%global gitversion 50fc4cb18

Summary: X.Org X11 libXv runtime library
Name:    libXv
Version: 1.0.13
Release: 5%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
License: SMLNJ AND HPND-sell-variant
URL: http://www.x.org

%if 0%{?gitdate}
Source0:        https://www.x.org/archive/individual/lib/%{name}-%{version}.tar.xz
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
Source0:        https://www.x.org/archive/individual/lib/%{name}-%{version}.tar.xz
%endif

Requires: libX11 >= 1.5.99.902

BuildRequires: make
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig(videoproto) pkgconfig(xext)
BuildRequires: libX11-devel >= 1.5.99.902

%description
X.Org X11 libXv runtime library

%package devel
Summary: X.Org X11 libXv development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXv development package

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf -v --install --force
%configure --disable-static
make %{?_smp_mflags}

%install

rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%doc AUTHORS COPYING
%{_libdir}/libXv.so.1
%{_libdir}/libXv.so.1.0.0

%files devel
%doc man/xv-library-v2.2.txt
%{_includedir}/X11/extensions/Xvlib.h
%{_libdir}/libXv.so
%{_libdir}/pkgconfig/xv.pc
%{_mandir}/man3/*.3*

%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.13-5
- Drop commented man3x line (rpmbuild expands macros in comments)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.13-4
- Prepare for Oreon 11 (RP1)
