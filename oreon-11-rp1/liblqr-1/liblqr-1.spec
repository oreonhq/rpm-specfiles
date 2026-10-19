%global source0_hash 173a822efd207d72cda7d7f4e951c5000f31b10209366ff7f0f5972f7f9ff137
Name:           liblqr-1
Version:        0.4.2
Release:        29%{?dist}
Summary:        LiquidRescale library
License:        GPL-3.0-only
URL:            http://liquidrescale.wikidot.com/
Source0:        https://liblqr.wdfiles.com/local--files/en:download-page/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  make
# /oreon:deps
%description
The LiquidRescale (lqr) library provides a C/C++ API for
performing non-uniform resizing of images by the seam-carving
technique.

%package devel
Summary:        LiquidRescale library development kit
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glib2-devel, pkgconfig
%description devel
The libqr-devel package contains the header files
needed to develop applications with liblqr

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
export CFLAGS="$CFLAGS -std=gnu11"
export LDFLAGS="%{build_ldflags} `pkg-config --libs glib-2.0` -lm"
%configure
%make_build
%install
%make_install
find $RPM_BUILD_ROOT -name \*.la -exec %{__rm} -f {} \;
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n liblqr-1-devel -f %{oreon_filedir}/liblqr-1-devel.list

%changelog

%autochangelog
