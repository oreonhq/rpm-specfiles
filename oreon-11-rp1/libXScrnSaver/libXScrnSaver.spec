%global source0_hash none

Name: libXScrnSaver
Version: 1.2.4
Release: 7%{?dist}
Summary: X.Org X11 libXss runtime library
License: X11
URL: http://www.x.org

Source0:        libXScrnSaver-1.2.4.tar.xz

BuildRequires: make
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig
BuildRequires: xorg-x11-proto-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel

%description
X.Org X11 libXss runtime library

%package devel
Summary: X.Org X11 libXScrnSaver development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXss development package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build
autoreconf -v --install --force
# FIXME: XScrnSaver.c:429: warning: dereferencing type-punned pointer will break strict-aliasing rules
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_post
%ldconfig_postun

%files
%doc COPYING README.md ChangeLog
%{_libdir}/libXss.so.1
%{_libdir}/libXss.so.1.0.0

%files devel
%{_libdir}/libXss.so
%{_libdir}/pkgconfig/xscrnsaver.pc
%{_mandir}/man3/*.3*
%{_includedir}/X11/extensions/scrnsaver.h

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.4-7
- Import
