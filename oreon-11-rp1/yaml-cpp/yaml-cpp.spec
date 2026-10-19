%global source0_hash 25cb043240f828a8c51beb830569634bc7ac603978e0f69d6b63558dadefd49a
%global sover 0.9
Name:           yaml-cpp
Version:        0.9.0
Release:        1%{?dist}
License:        MIT
Summary:        A YAML parser and emitter for C++
URL:            https://github.com/jbeder/yaml-cpp
Source0:        https://github.com/jbeder/yaml-cpp/archive/refs/tags/yaml-cpp-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         https://github.com/jbeder/yaml-cpp/pull/1211.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       libstdc++-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        static
Summary:        Static library for %{name}
Requires:       %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description    static
The %{name}-static package contains the static library for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir yaml-cpp-yaml-cpp-%{version}
%oreon_prep
%build

%global _vpath_builddir %{_target_platform}-${variant}
variant=static
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DYAML_CPP_BUILD_TOOLS:BOOL=OFF \
    -DYAML_CPP_FORMAT_SOURCE:BOOL=OFF \
    -DYAML_CPP_INSTALL:BOOL=ON \
    -DYAML_BUILD_SHARED_LIBS:BOOL=OFF \
    -DYAML_CPP_BUILD_TESTS:BOOL=OFF
variant=shared
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DYAML_CPP_BUILD_TOOLS:BOOL=OFF \
    -DYAML_CPP_FORMAT_SOURCE:BOOL=OFF \
    -DYAML_CPP_INSTALL:BOOL=ON \
    -DYAML_BUILD_SHARED_LIBS:BOOL=ON \
    -DYAML_CPP_BUILD_TESTS:BOOL=OFF
for variant in static shared; do
  %cmake_build
done
%install
variant=static
%cmake_install
mv %{buildroot}%{_libdir}/cmake/%{name} \
    %{buildroot}%{_libdir}/cmake/%{name}-static
mv %{buildroot}%{_libdir}/pkgconfig/%{name}.pc \
    %{buildroot}%{_libdir}/pkgconfig/%{name}-static.pc
variant=shared
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n yaml-cpp-devel -f %{oreon_filedir}/yaml-cpp-devel.list
%files -n yaml-cpp-static -f %{oreon_filedir}/yaml-cpp-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8.0-5
- Prepare for Oreon 11 (RP1)
