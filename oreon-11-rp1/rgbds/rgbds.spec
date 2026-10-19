%global source0_hash e79e51bdc0e53d8b52b5b9b58a5cbe15d6a380092da67dd625aeca29f6679660
Name:		rgbds
Version:	1.0.3
Release:        1%{?dist}
Summary:        A development package for the Game Boy, including an assembler
License:	MIT
URL:		https://github.com/gbdev/%{name}
Source0:        https://github.com/gbdev/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  bison
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  g++
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  pkgconfig(libpng)
# /oreon:deps
%description
RGBDS (Rednex Game Boy Development System) is a free assembler/linker package
for the Game Boy and Game Boy Color.

It consists of:

* rgbasm (assembler)
* rgblink (linker)
* rgbfix (checksum/header fixer)
* rgbgfx (PNG‐to‐2bpp graphics converter)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build Q="" CFLAGS="%{optflags}" VERSION_STRING=""
%install
%make_install PREFIX=%{_prefix} bindir=%{_bindir} mandir=%{_mandir} STRIP="-p" MANMODE="644 -p" Q=""
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
