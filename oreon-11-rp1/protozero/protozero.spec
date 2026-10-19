%global source0_hash 68d1df951b4d8397355c8fc9ffed40d9c06282a877fe847403feac6edcee3ef1
%global debug_package %{nil}
Name:           protozero
Version:        1.8.2
Release:        1%{?dist}
Summary:        Minimalistic protocol buffer decoder and encoder in C++
License:        BSD-2-Clause
URL:            https://github.com/mapbox/protozero
Source0:        https://github.com/mapbox/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  catch2-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  make
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  protobuf-lite-devel
# /oreon:deps
%description
Minimalistic protocol buffer decoder and encoder in C++.

Designed for high performance. Suitable for writing zero copy parsers
and encoders with minimal need for run-time allocation of memory.

Low-level: this is designed to be a building block for writing a
very customized decoder for a stable protobuf schema. If your protobuf
schema is changing frequently or lazy decoding is not critical for your
application then this approach offers no value: just use the decoding
API available via the C++ API that can be generated via the Google
Protobufs protoc program.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
%description    devel
Minimalistic protocol buffer decoder and encoder in C++.

Designed for high performance. Suitable for writing zero copy parsers
and encoders with minimal need for run-time allocation of memory.

Low-level: this is designed to be a building block for writing a
very customized decoder for a stable protobuf schema. If your protobuf
schema is changing frequently or lazy decoding is not critical for your
application then this approach offers no value: just use the decoding
API available via the C++ API that can be generated via the Google
Protobufs protoc program.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{name}-%{version}
rm -rf test/catch
ln -sf /usr/include/catch2 test/catch
mkdir build

%build

%cmake -DWERROR=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n protozero-devel -f %{oreon_filedir}/protozero-devel.list

%changelog

%autochangelog
