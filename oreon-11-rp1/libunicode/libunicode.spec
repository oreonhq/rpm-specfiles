%global source0_hash 78b715bc2d929530bc89e47c1c6772b72f511e1831b14e7d6d92cceb62592920
Name:           libunicode
Version:        0.9.3
Release:        2%{?dist}
Summary:        Modern C++20 Unicode Library
License:        Apache-2.0
URL:            https://github.com/contour-terminal/libunicode
Source0:        https://github.com/contour-terminal/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  x86_64 aarch64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(fmt)
BuildRequires:  cmake(range-v3)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(catch2)
BuildRequires:  unicode-ucd
# /oreon:deps
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
%oreon_prep
%build

%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DLIBUNICODE_UCD_DIR=/usr/share/unicode/ucd
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n libunicode-devel -f %{oreon_filedir}/libunicode-devel.list
%files -n libunicode-tools -f %{oreon_filedir}/libunicode-tools.list

%changelog

%autochangelog
