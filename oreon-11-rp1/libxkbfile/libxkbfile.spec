%global source0_hash 7f71884e5faf56fb0e823f3848599cf9b5a9afce51c90982baeb64f635233ebf

Summary: X.Org X11 libxkbfile runtime library
Name: libxkbfile
Version: 1.2.0
Release: 1%{?dist}
License: MIT-open-group AND HPND AND SMLNJ
URL: http://www.x.org

Source0:        https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: pkgconfig(xproto) pkgconfig(x11)
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: xorg-x11-util-macros

%description
X.Org X11 libxkbfile runtime library

%package devel
Summary: X.Org X11 libxkbfile development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libxkbfile development package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
autoreconf -fi
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
%doc COPYING ChangeLog
%{_libdir}/libxkbfile.so.1
%{_libdir}/libxkbfile.so.1.0.2

%files devel
%{_includedir}/X11/extensions/XKBbells.h
%{_includedir}/X11/extensions/XKBconfig.h
%{_includedir}/X11/extensions/XKBfile.h
%{_includedir}/X11/extensions/XKBrules.h
%{_includedir}/X11/extensions/XKM.h
%{_includedir}/X11/extensions/XKMformat.h
%{_libdir}/libxkbfile.so
%{_libdir}/pkgconfig/xkbfile.pc

%changelog
%autochangelog
