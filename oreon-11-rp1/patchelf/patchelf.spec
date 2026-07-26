%global source0_hash 64de10e4c6b8b8379db7e87f58030f336ea747c0515f381132e810dbf84a86e7

# hardening breaks the set-interpreter-long test on i686, x86_64, ppc64le, s390x
%undefine _hardened_build

Name:           patchelf
Version:        0.18.0
Release:        9%{?dist}
Summary:        A utility for patching ELF binaries

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://nixos.org/patchelf.html
Source0:        https://github.com/NixOS/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Allocate PHT & SHT at the end of the *.elf file
# This is needed after a change in binutils, see https://bugzilla.redhat.com/2321588
# Rebased form https://github.com/NixOS/patchelf/commit/43b75fbc9f
Patch:          0001-Allocate-PHT-SHT-at-the-end-of-the-.elf-file.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel

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
%configure
%make_build

%check
make check || (cat tests/*.log; exit 1)

%install
%make_install

# the docs get put in a funny place, so delete and include in the
# standard way in the docs section below
rm -rf %{buildroot}/usr/share/doc/%{name}

%files
%license COPYING
%doc README.md
%{_bindir}/patchelf
%{_mandir}/man1/patchelf.1*
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_patchelf

%changelog
%autochangelog
