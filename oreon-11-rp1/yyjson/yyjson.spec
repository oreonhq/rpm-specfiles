%global source0_hash 34e0f62a2bc11ab20d601e8ca1cc2b2079503aa45119a19133d89d19b94a0fae
%global forgeurl https://github.com/ibireme/yyjson
Version:        0.13.0
%global tag %{version}
%forgemeta
Name:           yyjson
Release:        1%{?dist}
Summary:        A high performance JSON library written in ANSI C
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description
A high performance JSON library written in ANSI C.

Features
- Fast: can read or write gigabytes per second JSON data on modern CPUs.
- Portable: complies with ANSI C (C89) for cross-platform compatibility.
- Strict: complies with RFC 8259 JSON standard, ensuring strict number format
and UTF-8 validation.
- Extendable: offers options to allow comments, trailing commas, NaN/Inf, and
custom memory allocator.
- Accuracy: can accurately read and write int64, uint64, and double numbers.
- Flexible: supports unlimited JSON nesting levels, \u0000 characters, and non
null-terminated strings.
- Manipulation: supports querying and modifying using JSON Pointer, JSON Patch
and JSON Merge Patch.
- Developer-Friendly: easy integration with only one h and one c file.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

# https://github.com/ibireme/yyjson/issues/154
sed -i '/-Werror/d' CMakeLists.txt

%build

%cmake \
    -GNinja \
    -DYYJSON_BUILD_TESTS=ON \
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n yyjson-devel -f %{oreon_filedir}/yyjson-devel.list

%changelog

%autochangelog
