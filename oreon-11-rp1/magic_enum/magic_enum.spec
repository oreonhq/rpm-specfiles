%global source0_hash 1e54959a3f3cb675938d858603ad69d0f3f7c82439fc2bf86d7232daec2bd10e
%global debug_package %{nil}
%global common_description %{expand:
Magic Enum is a header-only C++17 library that provides static reflection for
enums, working with any enum type without any macro or boilerplate code.}
Name:           magic_enum
Version:        0.9.8
Release:        1%{?dist}
Summary:        Static reflection for enums for modern C++
License:        MIT
URL:            https://github.com/Neargye/magic_enum
Source0:        https://github.com/Neargye/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  catch2-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description    %{common_description}

%package        devel
Summary:        %{summary}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%description    devel %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Replace bundled copy of Catch2 with the system one
ln -sf %{_includedir}/catch2/catch.hpp test/3rdparty/Catch2/include/catch2/

%build

%cmake
%cmake_build
%install
%cmake_install
rm %{buildroot}%{_datadir}/%{name}/package.xml
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n magic_enum-devel -f %{oreon_filedir}/magic_enum-devel.list

%changelog

%autochangelog
