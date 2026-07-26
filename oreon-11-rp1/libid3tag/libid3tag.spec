%global source0_hash 3b65150454818e3e46d113891e0e0c335516315c51f80d87565f6124b892bff4

Name:           libid3tag
Version:        0.16.3
Release:        %autorelease
Summary:        ID3 tag manipulation library

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://codeberg.org/tenacityteam/libid3tag
Source0:        %url/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Based on https://codeberg.org/tenacityteam/libid3tag/pulls/3
Patch0:         cmake-hook-genre.dat-and-gperf-files-generation.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gperf
BuildRequires:  zlib-devel >= 1.1.4

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

%autosetup -p1 -n %{name}

%build
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc CHANGES CREDITS README TODO
%license COPYING COPYRIGHT
%{_libdir}/libid3tag.so.0*

%files devel
%{_includedir}/id3tag.h
%{_libdir}/libid3tag.so
%{_libdir}/cmake/id3tag/
%{_libdir}/pkgconfig/id3tag.pc

%changelog
%autochangelog
