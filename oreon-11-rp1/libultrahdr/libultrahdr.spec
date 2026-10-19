%global source0_hash 2114acffc98c7abe5a7162e4cc6eb089f87bdfb7e4b330d91f24ac0375aa3c6f
%global gitdate       20251202
%global commit        8cbc983d2f6c2171af5cbcdb8801102f83fe92ab
%global short_commit  %(c="%{commit}"; echo ${c:0:7})
Name:           libultrahdr
Version:        1.4.0^%{gitdate}git%{short_commit}
Release:        1%{?dist}
Summary:        Reference codec for the Ultra HDR format
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/google/libultrahdr
Source0:        https://github.com/google/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch1:         https://github.com/google/libultrahdr/pull/383.patch#/remove-platform-and-architecture-detection-logic.patch
Patch2:         https://github.com/google/libultrahdr/pull/381.patch#/use-system-gtest.patch
Provides:       bundled(image_io)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  libjpeg-turbo-devel
# /oreon:deps
%description
libultrahdr is an image compression library that uses gain map technology to
store and distribute HDR images. Conceptually on the encoding side, the library
accepts SDR and HDR rendition of an image and from these a Gain Map (quotient
between the two renditions) is computed. The library then uses backward
compatible means to store the base image (SDR), gain map image and some
associated metadata. Legacy readers that do not support handling the gain map
image and/or metadata, will display the base image. Readers that support the
format combine the base image with the gain map and render a high dynamic range
image on compatible displays.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Rename license
mv third_party/image_io/src/modp_b64/LICENSE third_party/image_io/src/modp_b64/LICENSE.BSD-3-Clause

%build

%cmake -DUHDR_BUILD_TESTS=ON -DUHDR_ENABLE_SYSTEM_GTEST=ON
%cmake_build
%install
%cmake_install
rm %{buildroot}%{_libdir}/libuhdr.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifnarch s390x
%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n libultrahdr-devel -f %{oreon_filedir}/libultrahdr-devel.list

%changelog

%autochangelog
