%global source0_hash 0561009778513a95d91dac33cee8418d6622f710450a7cb56a74636d53b588cb
Name:           libid3tag
Version:        0.16.3
Release:        1%{?dist}
Summary:        ID3 tag manipulation library
License:        GPL-2.0-or-later
URL:            https://codeberg.org/tenacityteam/libid3tag
Source0:        https://codeberg.org/tenacityteam/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         cmake-hook-genre.dat-and-gperf-files-generation.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  zlib-devel
# /oreon:deps
%description
libid3tag is a library for reading and (eventually) writing ID3 tags,
both ID3v1 and the various versions of ID3v2.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
ID3 tag library development files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libid3tag-devel -f %{oreon_filedir}/libid3tag-devel.list

%changelog

%autochangelog
