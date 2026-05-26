# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 fbe74bbdcee21d656715688706da3c8becfd946d92cd44705cc6098bb23b3a16
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global sover 0.8

Name:           yaml-cpp
Version:        0.8.0
Release:        5%{?dist}

License:        MIT
Summary:        A YAML parser and emitter for C++
URL:            https://github.com/jbeder/yaml-cpp
Source0:        https://github.com/jbeder/yaml-cpp/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:         yaml-cpp-include.patch

# Allow CMake 4.0 build
Patch1:         https://github.com/jbeder/yaml-cpp/pull/1211.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

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
%oreon_verify_sources
%autosetup -p1

%build
# Define separate build directories for static and shared
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

# Move files so they don't get trampled
mv %{buildroot}%{_libdir}/cmake/%{name} \
    %{buildroot}%{_libdir}/cmake/%{name}-static
mv %{buildroot}%{_libdir}/pkgconfig/%{name}.pc \
    %{buildroot}%{_libdir}/pkgconfig/%{name}-static.pc

variant=shared
%cmake_install

%files
%doc CONTRIBUTING.md README.md
%license LICENSE
%{_libdir}/lib%{name}.so.%{sover}*

%files devel
%{_includedir}/yaml-cpp/
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%files static
%license LICENSE
%{_libdir}/lib%{name}.a
%{_libdir}/cmake/%{name}-static
%{_libdir}/pkgconfig/%{name}-static.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8.0-5
- Prepare for Oreon 11 (RP1)
