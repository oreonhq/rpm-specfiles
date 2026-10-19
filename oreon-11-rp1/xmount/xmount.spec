%global source0_hash 07c261e54e1e4cbcd4f7eaaf4f62efcbbbc68c76797ddca704592d99ebed3d10
Name:           xmount
Version:        1.2.0
Release:        1%{?dist}
Summary:        A on-the-fly convert for multiple hard disk image types
License:        GPL-3.0-or-later
URL:            https://www.sits.lu/xmount
Source0:        https://code.sits.lu/foss/xmount/-/archive/%{version}/xmount-%{version}.tar.bz2
Patch0:         xmount-suffix.patch
Patch1:         xmount-cflags.patch
Provides:       bundled(md5-deutsch)
# oreon:deps
BuildRequires:  afflib-devel
BuildRequires:  cmake
BuildRequires:  fuse3-devel
BuildRequires:  gcc-c++
BuildRequires:  libewf-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
xmount allows you to convert on-the-fly between multiple input
and output hard disk image types. xmount creates a virtual file
system using FUSE (Filesystem in Userspace) that contains a virtual
representation of the input image. The virtual representation can
be in raw DD, VirtualBox's virtual disk file format or in VmWare's
VMDK file format. Input images can be raw DD, EWF (Expert Witness
Compression Format) or AFF (Advanced Forensic Format) files. In
addition, xmount also supports virtual write access to the output
files that is redirected to a cache file. This makes it possible
to boot acquired hard disk images using QEMU, KVM, VirtualBox,
VmWare, or alike.

%prep

%setup -q
%patch -P0 -p1 -b .suffix
%patch -P1 -p1 -b .cflags
# Fix perm
chmod -x src/xmount.*

%build

%cmake \
    -DCMAKE_C_FLAGS="%{optflags} -fno-strict-aliasing" \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_SKIP_RPATH=ON \
    %{nil}
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
