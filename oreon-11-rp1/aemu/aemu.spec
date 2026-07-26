%global source0_hash 9fde54ab2529b062a4a4d3f6a2d41f40930d50a8f6d2a4765229ba93cb29284b

%global toolchain clang
%global gitdate 20231031
%global gitversion dd8b929c

Name:       aemu
Version:    0.1.2^%{gitdate}git%{gitversion}
Release:    9%{?dist}

Summary:    Android emulator library
License:    Apache-2.0
URL:        https://android.googlesource.com/platform/hardware/google/aemu

#VCS: https://android.googlesource.com/platform/hardware/google/aemu
# git snapshot.  to recreate, run:
# ./make-git-snapshot.sh `cat commitid`
Source0:    aemu-%{gitdate}.tar.xz
Source1:    make-git-snapshot.sh
Patch0000:  del-cuda.patch
Patch0001:  skip-tests.patch
Patch0002:  add-riscv.patch

BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
ExcludeArch:    %{ix86} %{power64} s390x

%description
Android developper library for emulators.

%package devel
Summary: AEMU development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
AEMU development files, used by gfxstream to build against.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{gitdate} -p1

%build
%cmake \
       -DAEMU_COMMON_GEN_PKGCONFIG=ON \
       -DAEMU_COMMON_BUILD_CONFIG=gfxstream
%cmake_build

%install
%cmake_install

%check
%cmake \
       -DAEMU_COMMON_BUILD_CONFIG=gfxstream \
       -DENABLE_VKCEREAL_TESTS=ON \
       -DBUILD_SHARED_LIBS=OFF
%cmake_build
%ctest

%files
%doc README.md
%license LICENSE
%{_libdir}/libaemu-*.so.0*

%files devel
%{_includedir}/aemu/
%{_libdir}/libaemu-*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
