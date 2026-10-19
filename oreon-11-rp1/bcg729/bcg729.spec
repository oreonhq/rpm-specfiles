%global source0_hash 9c22d98c2debc1e37163b8a703f05278ad5d9c03f1c6b373629d8a072092184a
Name:          bcg729
Version:       1.1.2
Release:        1%{?dist}
Summary:        Opensource implementation of the G.729 codec
License:       GPL-3.0-or-later
URL:           https://github.com/BelledonneCommunications/bcg729
Source0:        https://github.com/BelledonneCommunications/bcg729/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:        bcg729_cmakedir.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
bcg729 is an opensource implementation of both encoder and decoder of the
ITU G729 Annex A speech codec.
The library written in C 99 is fully portable and can be executed on many
platforms including both ARM  processor and x86.
bcg729 supports concurrent channels encoding/decoding for multi call
application such conferencing.

%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description   devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DENABLE_STATIC=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles bcg729-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%files -f %{oreon_filedir}/main.list
%files -n bcg729-devel -f %{oreon_filedir}/bcg729-devel.list

%changelog

%autochangelog
