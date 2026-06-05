%global source0_hash b50d4c25b97009a744706c1039c598f4d8e64910c9fde381994e1cae235d9242

%global tarball libXtst
#global gitdate 20130524
%global gitversion e7e04b7be

Summary: X.Org X11 libXtst runtime library
Name: libXtst
Version: 1.2.5
Release: 4%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
License: MIT-open-group AND HPND-sell-variant AND X11 AND HPND-doc AND HPND-doc-sell
URL: http://www.x.org

%if 0%{?gitdate}
Source0:        libXtst-1.2.5.tar.xz
Source1:        make-git-snapshot.sh
Source2:        commitid
%else
Source0:        libXtst-1.2.5.tar.xz
%endif

Requires: libX11 >= 1.5.99.902

BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool make
BuildRequires: xorg-x11-proto-devel
BuildRequires: libX11-devel >= 1.5.99.902
BuildRequires: libXext-devel
BuildRequires: libXi-devel
BuildRequires: xmlto

%description
X.Org X11 libXtst runtime library

%package devel
Summary: X.Org X11 libXtst development package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libXi-devel%{?_isa}

%description devel
X.Org X11 libXtst development package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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

rm -rf $RPM_BUILD_ROOT%{_docdir}

%ldconfig_post
%ldconfig_postun

%files
%doc COPYING
%{_libdir}/libXtst.so.6
%{_libdir}/libXtst.so.6.1.0

%files devel
%{_includedir}/X11/extensions/XTest.h
%{_includedir}/X11/extensions/record.h
%{_libdir}/libXtst.so
%{_libdir}/pkgconfig/xtst.pc
%{_mandir}/man3/XTest*.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.5-4
- Import
