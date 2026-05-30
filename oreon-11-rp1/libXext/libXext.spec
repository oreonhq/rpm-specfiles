%global source0_hash edb59fa23994e405fdc5b400afdf5820ae6160b94f35e3dc3da4457a16e89753

%global tarball libXext
#global gitdate 20130524
%global gitversion dfe6e1f3b

Summary: X.Org X11 libXext runtime library
Name: libXext
Version: 1.3.6
Release: 6%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
License: MIT-open-group AND X11 AND HPND AND HPND-sell-variant AND SMLNJ AND MIT AND ISC AND HPND-doc AND HPND-doc-sell
URL: http://www.x.org

%if 0%{?gitdate}
Source0:        http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
Source0:        http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz
%endif

Requires: libX11 >= 1.5.99.902

BuildRequires: make
BuildRequires: autoconf automake libtool
BuildRequires: xorg-x11-proto-devel >= 7.4-23
BuildRequires: libX11-devel >= 1.5.99.902
BuildRequires: libXau-devel
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool pkgconfig
BuildRequires: xmlto

%description
X.Org X11 libXext runtime library

%package devel
Summary: X.Org X11 libXext development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXext development package

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

# do this with %%doc below
rm -rf $RPM_BUILD_ROOT%{_docdir}

%ldconfig_post
%ldconfig_postun

%files
%doc AUTHORS COPYING
%{_libdir}/libXext.so.6
%{_libdir}/libXext.so.6.4.0

%files devel
%{_includedir}/X11/extensions/MITMisc.h
%{_includedir}/X11/extensions/XEVI.h
%{_includedir}/X11/extensions/XLbx.h
%{_includedir}/X11/extensions/XShm.h
%{_includedir}/X11/extensions/Xag.h
%{_includedir}/X11/extensions/Xcup.h
%{_includedir}/X11/extensions/Xdbe.h
%{_includedir}/X11/extensions/Xext.h
%{_includedir}/X11/extensions/Xge.h
%{_includedir}/X11/extensions/dpms.h
%{_includedir}/X11/extensions/extutil.h
%{_includedir}/X11/extensions/multibuf.h
%{_includedir}/X11/extensions/security.h
%{_includedir}/X11/extensions/shape.h
%{_includedir}/X11/extensions/sync.h
%{_includedir}/X11/extensions/xtestext1.h
%{_libdir}/libXext.so
%{_libdir}/pkgconfig/xext.pc
%{_mandir}/man3/*.3*

%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.6-6
- Drop commented man3x line (rpmbuild expands macros in comments)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.6-5
- Prepare for Oreon 11 (RP1)
