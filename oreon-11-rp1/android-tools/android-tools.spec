%global source0_hash 2725d09f892a3a38e534429f47a321f58ecf6a3169caa42c915fb2cb7d46be0e
Name:          android-tools
Version:       37.0.0
Release:        1%{?dist}
Epoch:         1
Summary:        Android platform tools(adb, fastboot)
License:       Apache-2.0 AND (Apache-2.0 AND LicenseRef-Callaway-BSD)
URL:           http://developer.android.com/guide/developing/tools/
Source0:        https://github.com/nmeum/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Patch0:        0001-Fix-libusb-enumeration.patch
Patch1:        0002-extras-libjsonpb-Fix-incompatibility-with-protobuf-v30.patch
Patch2:        0003-Make-legacy-USB-driver-default-on-Linux.patch
Patch3:        0004-Add-missing-cstdint-includes-for-GCC-16-Fedora.patch
Provides:      adb = %{epoch}:%{version}-%{release}
Provides:      fastboot = %{epoch}:%{version}-%{release}
Provides:      mke2fs.android = %{epoch}:%{version}-%{release}
Provides: bundled(boringssl)
ExcludeArch: ppc ppc64 s390x ppc64le
# oreon:deps
BuildRequires:  brotli-devel
BuildRequires:  cmake
BuildRequires:  fmt-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libusbx-devel
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  multilib-rpm-config
BuildRequires:  pcre2-devel
BuildRequires:  perl
BuildRequires:  protobuf-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description

The Android Debug Bridge (ADB) is used to:

- keep track of all Android devices and emulators instances
  connected to or running on a given host developer machine

- implement various control commands (e.g. "adb shell", "adb pull", etc.)
  for the benefit of clients (command-line users, or helper programs like
  DDMS). These commands are what is called a 'service' in ADB.

Fastboot is used to manipulate the flash partitions of the Android phone. 
It can also boot the phone using a kernel image or root filesystem image 
which reside on the host machine rather than in the phone flash. 
In order to use it, it is important to understand the flash partition 
layout for the phone.
The fastboot program works in conjunction with firmware on the phone 
to read and write the flash partitions. It needs the same USB device 
setup between the host and the target phone as adb.

%prep
%oreon_prep
%build

%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
