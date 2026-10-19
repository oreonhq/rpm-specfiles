%global source0_hash a89c03e2b0f16239d67a2031b9003f31b5a686106bbdb3c797fb88ae472af380
%global with_devel 0%{?rhel} && 0%{?rhel} <= 8
Summary:        X.Org X11 libXxf86misc runtime library
Name: libXxf86misc
Version: 1.0.4
Release:        20%{?dist}
License: MIT
URL: http://www.x.org
Source0:        https://www.x.org/releases/individual/lib/libXxf86misc-1.0.4.tar.bz2
Source1:        xf86misc.h
Source2:        xf86mscstr.h
%if !%{with_devel}
Obsoletes: libXxf86misc-devel <= 1.0.4-4
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  sed
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
X.Org X11 libXxf86misc runtime library

%if %{with_devel}
%package devel
Summary: X.Org X11 libXxf86misc development package
Requires: %{name} = %{version}-%{release}
%description devel
X.Org X11 libXxf86misc development package
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
sed -i s/xf86miscproto// configure.ac
mkdir -p src/X11/extensions/
cp %{SOURCE1} %{SOURCE2} src/X11/extensions/

%build

autoreconf -v --install --force
%configure --disable-static
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%if %{with_devel}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/X11/extensions
install -m 0644 -p %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_includedir}/X11/extensions
%else
rm -f $RPM_BUILD_ROOT%{_libdir}/*.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig
rm -rf $RPM_BUILD_ROOT%{_mandir}/man3/*.3*
%endif
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.4-20
- Import
