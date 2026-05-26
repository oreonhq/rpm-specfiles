Summary: X.Org X11 libxkbfile runtime library
Name: libxkbfile
Version: 1.1.3
Release: 5%{?dist}
License: MIT-open-group AND HPND AND SMLNJ
URL: http://www.x.org

Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 a9b63eea997abb9ee6a8b4fbb515831c841f471af845a09de443b28003874bec
%global source0_file libxkbfile-1.1.3.tar.xz
# oreon url source checksums end

BuildRequires: make
BuildRequires: pkgconfig(xproto) pkgconfig(x11)
BuildRequires: gcc

%description
X.Org X11 libxkbfile runtime library

%package devel
Summary: X.Org X11 libxkbfile development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libxkbfile development package

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libxkbfile-1.1.3.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a9b63eea997abb9ee6a8b4fbb515831c841f471af845a09de443b28003874bec" || { echo "oreon: Source0 SHA256 mismatch for libxkbfile-1.1.3.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
# FIXME: We use -fno-strict-aliasing, to work around the following bug:
# maprules.c:1373: warning: dereferencing type-punned pointer will break strict-aliasing rules)
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.3-5
- Prepare for Oreon 11 (RP1)
