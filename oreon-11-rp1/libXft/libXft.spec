%global source0_hash 60a25b78945ed6932635b3bb1899a517d31df7456e69867ffba27f89ff3976f5
Summary:        X.Org X11 libXft runtime library
Name: libXft
Version: 2.3.9
Release:        1%{?dist}
License: HPND-sell-variant
URL: http://www.x.org
Source0:        https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
Patch:   fix_font_loading.patch
Requires: fontconfig >= 2.2-1
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xrender)
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
X.Org X11 libXft runtime library

%package devel
Summary: X.Org X11 libXft development package
Requires: %{name} = %{version}-%{release}
%description devel
X.Org X11 libXft development package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -v --install --force
%configure --disable-static
make %{?_smp_mflags} 
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libXft-devel -f %{oreon_filedir}/libXft-devel.list

%changelog

%autochangelog
