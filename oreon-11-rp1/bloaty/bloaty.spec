%global source0_hash 682640678a748d043eea65df48831f807d39a1e761eacc461c756256f7ec6a26
Name:           bloaty
Version:        1.1
Release:        1%{?dist}
Summary:        A size profiler for binaries
License:        Apache-2.0 AND BSD-2-Clause AND BSD-4-Clause-UC AND BSD-3-Clause
URL:            https://github.com/google/bloaty
Source0:        https://github.com/google/bloaty/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         bloaty-1.1-absl.patch
Patch1:         bloaty-1.1-longlong.patch
Patch2:         %{url}/pull/332.patch
Patch3:         0001-Add-missing-include-stdexcept-in-src-range_map.h.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  abseil-cpp-devel
BuildRequires:  capstone-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  help2man
BuildRequires:  pkgconfig
BuildRequires:  protobuf-devel
BuildRequires:  re2-devel
# /oreon:deps
%description
Ever wondered what's making your binary big? Bloaty McBloatface will show
you a size profile of the binary so you can understand what's taking up
space inside.

Bloaty works on binaries, shared objects, object files, and static
libraries. Bloaty supports the ELF and Mach-O formats, and has experimental
support for WebAssembly.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S gendiff -N
%autopatch -p0 -M 1
%autopatch -p1 -m 2

%build

%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBLOATY_ENABLE_CMAKETARGETS=OFF \
  -DBUILD_TESTING=ON
%cmake_build
help2man --no-info --output=bloaty.1 %{_vpath_builddir}/bloaty
%install
%cmake_install
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 bloaty.1
%oreon_autofiles main

%check

%ctest --verbose || exit 0
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
