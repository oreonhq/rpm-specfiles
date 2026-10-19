%global source0_hash 9d8392705cb10803d5fe1d27d236cbab3f664e26841ce01916bbbe430cf273e2
%define _x11fontdir		%{_datadir}/X11/fonts
Summary:        X.Org X11 libfontenc runtime library
Name: libfontenc
Version: 1.1.9
Release:        1%{?dist}
License: MIT
URL: http://www.x.org
Source0:        https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-font-utils
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xorg-x11-util-macros
BuildRequires:  zlib-devel
# /oreon:deps
%description
X.Org X11 libfontenc runtime library

%package devel
Summary: X.Org X11 libfontenc development package
Requires: %{name} = %{version}-%{release}
%description devel
X.Org X11 libfontenc development package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

export CFLAGS="$RPM_OPT_FLAGS -Os"
%configure --disable-static --with-fontrootdir=%{_x11fontdir}
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -type f -name '*.la' | xargs rm -f -- || :
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libfontenc-devel -f %{oreon_filedir}/libfontenc-devel.list

%changelog

%autochangelog
