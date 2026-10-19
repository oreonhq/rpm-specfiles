%global source0_hash a1ada76ef35e5af9c2fbd063754dc9e37a8d989417c6eb1ecebb089b1383ae9e
Name:          sbc
Version:       2.2
Release:        1%{?dist}
Summary:        Sub Band Codec used by bluetooth A2DP
License:       GPL-2.0-only AND LGPL-2.1-or-later
URL:           http://www.bluez.org
Source0:        http://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.xz
Requires: lib%{name}%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libsndfile-devel
BuildRequires:  make
# /oreon:deps
%description
SBC (Sub Band Codec) is a low-complexity audio codec used in the Advanced Audio 
Distribution Profile (A2DP) bluetooth standard but can be used standalone. It 
uses 4 or 8 subbands, an adaptive bit allocation algorithm in combination with 
an adaptive block PCM quantizers.

%package -n libsbc
Summary: Library for the SBC (Sub Band Codec)
%description -n libsbc
Library for SBC (Sub Band Codec) is a low-complexity audio codec used in the
Advanced Audio Distribution Profile (A2DP) bluetooth standard but can be used
standalone. It uses 4 or 8 subbands, an adaptive bit allocation algorithm in
combination with an adaptive block PCM quantizers.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: lib%{name}%{?_isa} = %{version}-%{release}
%description devel
Files for development with %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
%make_build
%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
%ldconfig_scriptlets
%oreon_autofiles libsbc usr/*/lib*.so.*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libsbc -f %{oreon_filedir}/libsbc.list
%files -n sbc-devel -f %{oreon_filedir}/sbc-devel.list

%changelog

%autochangelog
