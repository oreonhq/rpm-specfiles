%global source0_hash bba4b6fac2349fa6badc701aad5e7afb87504a7089a867b1a7cbed08fb2f3a90

%global commit0 7edbd580cfad509a3253c733e70144e36f02ecd4
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           rttr
Version:        0.9.7
Release:        0.14git%{shortcommit0}%{?dist}
Summary:        Run Time Type Reflection

License:        MIT
URL:            https://www.rttr.org
Source0:        https://github.com/rttrorg/rttr/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Patch0:         0001-cmake-Don-t-set-non-default-permissions.patch

BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  cmake3
BuildRequires:  make

%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  catch2-devel
%else
BuildRequires:  catch-devel
%endif
BuildRequires:  rapidjson-devel

%description
Run Time Type Reflection is the the ability of a computer program to
introspect and modify objects at runtime. It is also the name of the
library itself, which is written in C++.

%package -n librttr
Summary:        Run Time Type Reflection for C++
Provides:       bundled(nonius) = 1.1.2

%description -n librttr
Run Time Type Reflection is the the ability of a computer program to
introspect and modify objects at runtime. It is also the name of the
library itself, which is written in C++.

%package  -n librttr-devel
Summary:        Header files for the C++ Run Time Type Reflection library
Requires:       librttr%{?_isa} = %{version}-%{release}

%description  -n librttr-devel
Run Time Type Reflection is the the ability of a computer program to
introspect and modify objects at runtime. It is also the name of the
library itself, which is written in C++.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
The %{name}-documentation documentations for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit0}
find . -type f -exec chmod -x {} ';'
sed -i 's/PERMISSIONS OWNER_READ//' CMake/*.cmake

# Unbundle
rm -rf 3rd_party/catch-1.12.0 3rd_party/rapidjson-1.1.0

# Fix catch2 include
%if ! 0%{?el7}
find src/unit_tests/ -name *.cpp -exec sed -i -e 's|catch/catch.hpp|catch2/catch.hpp|' {} ';'
find src/unit_tests/ -name *.h -exec sed -i -e 's|catch/catch.hpp|catch2/catch.hpp|' {} ';'
%endif

# Disable compiler Werror
# See also https://github.com/rttrorg/rttr/issues/317
# and https://github.com/rttrorg/rttr/issues/357
sed -i -e 's/target_compile_options/#target_compile_options/' CMake/utility.cmake

%build
# TODO: Please submit an issue to upstream (rhbz#2381435)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake3 \
  -DCMAKE_INSTALL_CMAKEDIR=cmake \
  -DCMAKE_INSTALL_LIBDIR=%{_lib} \
  -DBUILD_EXAMPLES=OFF \
  -DBUILD_PACKAGE=OFF \
  -DUSE_PCH=OFF

%cmake3_build

%install
rm -rf __doc
%cmake3_install

# Rework doc
mkdir -p __doc
mv %{buildroot}%{_prefix}/doc/* __doc
find __doc -type f -exec chmod 0644 {} ';'
rm -rf %{buildroot}%{_datadir}/rttr/{LICENSE.txt,README.md}

%check
%ctest3 run_tests

%files -n librttr
%license LICENSE.txt
%doc README.md
%{_libdir}/librttr_core.so.%{version}

%files -n librttr-devel
%{_includedir}/rttr/
%{_libdir}/librttr_core.so
%{_datadir}/rttr/cmake/

%files doc
%doc __doc/*

%changelog
%autochangelog
