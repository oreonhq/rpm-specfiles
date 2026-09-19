%global source0_hash f247d6970728c08c05275d2ef0818ea5a3d5a351be135e57fd26d1e5f538614c

%global gitdate 20240226
%global gitversion 23d05703

Name:           gfxstream
Version:        0.1.2^%{gitdate}git%{gitversion}
Release:        5%{?dist}

Summary:        Graphics Streaming Kit

# the project license declared in meson.build is "MIT OR Apache-2.0"
# but it also uses some MIT licensed headers and OpenGL headers are
# under the MIT-Khronos license, some files only have Apache-2.0
# license information.
#
# in the source package there are a number of other licenses
# that are (CC-BY-4.0) and not included in the
# software installed by the produced rpms,
# see the project LICENSE for a partial listing.
#
# See also licensecheck.txt for a full break down.
# (the project license will be clarified if/when it is accepted in mesa!27246)
License:        MIT AND Apache-2.0 AND MIT-Khronos-old

URL:            https://android.googlesource.com/platform/hardware/google/gfxstream

#VCS: https://android.googlesource.com/platform/hardware/google/gfxstream
# git snapshot.  to recreate, run:
# ./make-git-snapshot.sh `cat commitid`
Source0:        gfxstream-%{gitdate}.tar.xz
Source1:        make-git-snapshot.sh
Source2:        licensecheck.txt

Patch0000:      0001-meson-use-system-headers-if-possible.patch
Patch0001:      0001-meson-add-DGLM_ENABLE_EXPERIMENTAL.patch
Patch0002:      fix_missing_cstdint.patch

BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  meson
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(aemu_base)
BuildRequires:  pkgconfig(aemu_host_common)
BuildRequires:  pkgconfig(aemu_logging)
BuildRequires:  vulkan-headers
BuildRequires:  renderdoc-devel
BuildRequires:  glm-devel
BuildRequires:  libglvnd-devel
ExcludeArch:    %{ix86} %{power64} s390x

%description
Graphics Streaming Kit is a code generator that makes it easier to serialize and
forward graphics API calls from one place to another:
 - from a virtual machine guest to host for virtualized graphics
 - from one process to another for IPC graphics
 - from one computer to another via network sockets

%package devel
Summary: gfxstream development files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
gfxstream development files, used by QEMU to build against.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{gitdate} -p1

%build
%meson -Ddecoders=gles,vulkan,composer
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libgfxstream_backend.so.0*

%files devel
%dir %{_includedir}/gfxstream/
%{_includedir}/gfxstream/*
%{_libdir}/libgfxstream_backend.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
