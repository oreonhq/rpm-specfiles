%global source0_hash bc2e349b3bd8c12aaff036162b07162c290f4f8ae625c2306bdc819f62d80caf
%global gitdate 20240214
%global gitversion ae733ceb2
Name:	    rutabaga-gfx-ffi
Version:    0.1.3
Release:        1%{?dist}
Summary:        Handling virtio-gpu protocols
URL:        https://chromium.googlesource.com/crosvm/crosvm
License:    BSD-3-Clause AND BSD-2-Clause AND MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)
Source0:        rutabaga-gfx-%{gitdate}.tar.xz
Source1:    make-git-snapshot.sh
Patch0000:  drop-winapi.patch
Patch0001:  license.patch
ExclusiveArch: x86_64 aarch64
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description
A library for handling 2D and 3D virtio-gpu hypercalls, along with graphics
swapchain allocation and mapping.

%package devel
Summary: Rutabaga-gfx-ffi development files
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Rutabaga-gfx-ffi development files, used by QEMU to build against.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n rutabaga-gfx-%{gitdate} -p1
%oreon_vendor_cargo
%build

pushd ffi
mkdir -p target/release/
%cargo_build
%cargo_license_summary
%{cargo_license} > ../LICENSE.dependencies
popd
%install
pushd ffi
install -D -m 755 target/rpm/librutabaga_gfx_ffi.so %{buildroot}%{_libdir}/librutabaga_gfx_ffi.so.0.1.2
ln -s librutabaga_gfx_ffi.so.0.1.2 %{buildroot}%{_libdir}/librutabaga_gfx_ffi.so.0
ln -s librutabaga_gfx_ffi.so.0.1.2 %{buildroot}%{_libdir}/librutabaga_gfx_ffi.so
install -D -m 644 target/release/rutabaga_gfx_ffi.pc %{buildroot}%{_libdir}/pkgconfig/rutabaga_gfx_ffi.pc
install -D -m 644 src/include/rutabaga_gfx_ffi.h %{buildroot}%{_includedir}/rutabaga_gfx/rutabaga_gfx_ffi.h
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n rutabaga-gfx-ffi-devel -f %{oreon_filedir}/rutabaga-gfx-ffi-devel.list

%changelog

%autochangelog
