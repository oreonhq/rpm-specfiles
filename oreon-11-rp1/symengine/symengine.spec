%global source0_hash 11c5f64e9eec998152437f288b8429ec001168277d55f3f5f1df78e3cf129707
%global common_description %{expand:
SymEngine is a standalone fast C++ symbolic manipulation library. Optional thin
wrappers allow usage of the library from other languages.}
Name:           symengine
Version:        0.14.0
Release:        1%{?dist}
Summary:        Fast symbolic manipulation library
License:        MIT
URL:            https://symengine.org/
ExcludeArch:    %{ix86}
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         https://github.com/symengine/symengine/commit/d8234815beee37447bd85d51c70f4a855509c20f.patch
Patch1:         https://github.com/symengine/symengine/commit/00085a24acbffd95dafb94331fa4a07a0da44ffa.patch
# oreon:deps
BuildRequires:  cereal-devel
BuildRequires:  cmake
BuildRequires:  flint-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  llvm-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description    %{common_description}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem
%description    devel %{common_description}

The %{name}-devel package contains libraries and header files for developing
applications that use SymEngine.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i -e 's|DEF_INSTALL_CMAKE_DIR lib/cmake|DEF_INSTALL_CMAKE_DIR %{_lib}/cmake|g' CMakeLists.txt

%build

%cmake \
    -DINTEGER_CLASS=flint \
%ifarch s390x
    -DHAVE_SYMENGINE_RTTI=no \
%endif
    -DWITH_GMP=on \
    -DWITH_LLVM=on \
    -DWITH_LLVM=on \
    -DWITH_MPFR=on \
    -DWITH_SYSTEM_CEREAL=on \
    -DWITH_SYMENGINE_THREAD_SAFE=on
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n symengine-devel -f %{oreon_filedir}/symengine-devel.list

%changelog

%autochangelog
