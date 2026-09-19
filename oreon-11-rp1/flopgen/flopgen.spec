%global source0_hash c49e87b747554632d22d795f542191de3e0e129b0d22915f56432afa225d297c

Name:           flopgen
Version:        0.1.0
Release:        %autorelease
Summary:        Tool for automatic creation of FAT-formatted floppy disk images

# Automatically converted from old format: GPLv3 and BSD - review is highly recommended.
License:        GPL-3.0-only AND LicenseRef-Callaway-BSD
URL:            https://github.com/maksgraczyk/Flopgen
Source0:        %{url}/archive/v%{version}/Flopgen-%{version}.tar.gz
# PR#2: Fix the build on GCC 8
Patch0:         %{url}/commit/16f69999297e6808cd35aad402f208d40a4710c1.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  sed
BuildRequires:  cli11-devel
%if 0%{?fedora}
BuildRequires:  cli11-static
%endif

# Added in 3c9b2d695ba35cb5a36265e1bb52793c40412c3b and modified, see
# README.md for details.
Provides:       bundled(fatfs) = 0.14

%description
Flopgen is a tool for automatic creation of FAT-formatted floppy disk images
with user-supplied files.

This program should be especially useful for people who need to transfer files
frequently between their main machines and emulated/virtualised legacy systems
with no or unreliable CD support.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Flopgen-%{version} -p1
# neuter hardcoded flags
sed -e '/CXXFLAGS = --std=c++17/d' -e '/LDFLAGS = -lstdc++fs/d' -i Makefile
# replace embedded copy of cli11 with the system one
rm -f cli/*
ln -s /usr/include/CLI/CLI.hpp cli/CLI11.hpp

%build
export CFLAGS="-I/usr/include/CLI --std=c++17 %{optflags}"
export CXXFLAGS="-I/usr/include/CLI --std=c++17 %{optflags}"
export LDFLAGS="-lstdc++fs %{build_ldflags}"
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
cp -P flopgen %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%changelog
%autochangelog
