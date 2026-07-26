%global source0_hash 7b653d8cb3c620cc80118184ccab9c02f7e9a4bf9d1e4b190dae2d5681a0bca4

Name:           libunicode
Version:        0.7.0
Release:        %autorelease
Summary:        Modern C++20 Unicode Library
License:        Apache-2.0
URL:            https://github.com/contour-terminal/libunicode
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  x86_64 aarch64

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(fmt)
BuildRequires:  cmake(range-v3)
BuildRequires:  unicode-ucd
BuildRequires:  pkgconfig(catch2)

%description
The goal of libunicode library is to bring painless unicode support to C++
with simple and easy to understand APIs. The API naming conventions are chosen
to look familiar to those using the C++ standard libary.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%package        tools
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
The %{name}-tools package contains tools about %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -C

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DLIBUNICODE_UCD_DIR=/usr/share/unicode/ucd
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libunicode*.so.0.7*

%files devel
%{_includedir}/libunicode/
%{_libdir}/cmake/libunicode/
%{_libdir}/libunicode*.so

%files tools
%{_bindir}/unicode-query

%changelog
%autochangelog
