%global source0_hash 462373d172bd7bdaba6675a9e44fef65a1d58e13cc3ddcef19fff0793d49e174
%global commit b5e720e4a080bf4e7cc2edc09c19d73db21b401a
%global commitdate 20251118
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%undefine _auto_set_build_flags
%global debug_package %{nil}
Name:           stubble
Version:        0.0~%{commitdate}git%{shortcommit}
Release:        1%{?dist}
Summary:        UEFI kernel boot stub with auto-DTB selection
License:        LGPL-2.1-or-later
URL:            https://github.com/ubuntu/stubble
Source0:        https://github.com/ubuntu/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch1:         0001-Makefile-Add-fPIC-to-CFLAGS.patch
ExclusiveArch:  %{arm64}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3-pyelftools
# /oreon:deps
%description
A minimal UEFI kernel boot stub for loading machine specific device trees
embedded within a kernel image. Compatible with systemd-stub and ukify.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n stubble-%{commit}

%build

%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
