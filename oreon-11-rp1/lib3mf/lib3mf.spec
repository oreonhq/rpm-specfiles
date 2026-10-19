%global source0_hash 96e85e278fc5474123e3c47237dd42faaf1fdf8e182541a84af7fe84ddd3cbde
Name:           lib3mf
Version:        2.2.0
Release:        1%{?dist}
Summary:        Implementation of the 3D Manufacturing Format file standard
License:        BSD-2-Clause AND Zlib
URL:            https://3mf.io
Source0:        https://github.com/3MFConsortium/lib3mf/archive/v%{version}/lib3mf-%{version}.tar.gz
Patch289:       https://github.com/3MFConsortium/lib3mf/pull/289.patch
Patch290:       https://github.com/3MFConsortium/lib3mf/pull/290.patch
Patch407:       https://github.com/3MFConsortium/lib3mf/pull/407.patch
%bcond_without  tests
%if %{with tests}
%endif
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
ExcludeArch:    %{ix86}
%endif
Provides:       bundled(cpp-base64) = 1.01.00
%define __cmake_in_source_build 1
# oreon:deps
BuildRequires:  act
BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libzip-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# A bundled x86 executable, we use the packaged one instead
# https://github.com/3MFConsortium/lib3mf/issues/199
rm AutomaticComponentToolkit/bin/act.linux
ln -s /usr/bin/act AutomaticComponentToolkit/bin/act.linux

# c++11 does not work with gtest 1.13+
sed -i 's/ -std=c++11//' CMakeLists.txt

# remove unused bundled libraries
rm {Include,Source}/Libraries/{libzip,zlib} -r
sed -i -e 's|Libraries/libzip/zip.h|zip.h|' \
       -e 's|Libraries/zlib/zlib.h|zlib.h|' \
  {Include,Source}/Common/*/*

%build

mkdir -p build
cd build
%cmake3 %{!?with_tests:-DLIB3MF_TESTS=OFF} \
  -DUSE_INCLUDED_ZLIB=OFF \
  -DUSE_INCLUDED_LIBZIP=OFF \
  -DUSE_INCLUDED_GTEST=OFF \
  -DUSE_INCLUDED_SSL=OFF \
  -DSTRIP_BINARIES=OFF \
  -DCMAKE_INSTALL_LIBDIR=%{_lib} \
  -DCMAKE_INSTALL_INCLUDEDIR=include/%{name} \
  ..
%make_build
cd ..
%install
%make_install -C build
cp -a Include/* %{buildroot}%{_includedir}/%{name}/
rm -r %{buildroot}%{_includedir}/%{name}/Libraries
ln -s Bindings/C/lib3mf.h \
      Bindings/Cpp/lib3mf_abi.hpp \
      Bindings/CDynamic/lib3mf_dynamic.h \
      Bindings/CppDynamic/lib3mf_dynamic.hpp \
      Bindings/Cpp/lib3mf_implicit.hpp \
      Bindings/NodeJS/lib3mf_nodewrapper.h \
      Bindings/C/lib3mf_types.h \
      Bindings/Cpp/lib3mf_types.hpp \
  %{buildroot}%{_includedir}/%{name}/
ln -s lib3mf.pc %{buildroot}%{_libdir}/pkgconfig/lib3MF.pc
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with tests}
%check

cd build
%ctest --rerun-failed --output-on-failure
cd ..
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n lib3mf-devel -f %{oreon_filedir}/lib3mf-devel.list

%changelog

%autochangelog
