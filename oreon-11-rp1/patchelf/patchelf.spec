%global source0_hash 39cd33c4810f10ec479d22b8ee6cf8e7acb77c356f3864e3270e2d45f7d23448
%undefine _hardened_build
Name:           patchelf
Version:        0.19.1
Release:        1%{?dist}
Summary:        A utility for patching ELF binaries
License:        GPL-3.0-or-later
URL:            http://nixos.org/patchelf.html
Source0:        https://github.com/NixOS/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  make
# /oreon:deps
%description
PatchELF is a simple utility for modifying an existing ELF executable
or library.  It can change the dynamic loader ("ELF interpreter")
of an executable and change the RPATH of an executable or library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# package ships elf.h - delete to use glibc-headers one
rm src/elf.h

%build

autoreconf -fi
%configure
%make_build
%check

make check || (cat tests/*.log; exit 1)
%install
%make_install
rm -rf %{buildroot}/usr/share/doc/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
