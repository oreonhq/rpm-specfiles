%global source0_hash b16246f617b2a136c78d73e5e2647c6f1de1313e46678062985bdcf1f40bb75d

%global forgeurl https://github.com/ibireme/yyjson
Version:        0.12.0
%global tag %{version}
%forgemeta

Name:           yyjson
Release:        %autorelease
Summary:        A high performance JSON library written in ANSI C
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

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

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libyyjson.so.0*

%files devel
%{_includedir}/yyjson.h
%{_libdir}/libyyjson.so
%{_libdir}/cmake/yyjson/
%{_libdir}/pkgconfig/yyjson.pc

%changelog
%autochangelog
