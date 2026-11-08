# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3f33b22135219c39c3c695f7b7171c2567d3e2a17c798c0a90607320cbb268f2

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Summary: The GNU line editor
Name: ed
Version:        1.22.6
Release:        1%{?dist}

# The entire source is GPLv2 except doc/ed.info and doc/ed.texi, which are GFDL
License: GPL-2.0-only AND GFDL-1.3-no-invariants-or-later
URL:     https://www.gnu.org/software/ed/
Source0:        https://mirror.cs.odu.edu/gnu/ed/ed-%{version}.tar.lz
Source1:        ed-1.22.6.tar.lz.sig
Source2:        antoniodiazdiaz-keyring-2026.asc

BuildRequires: gcc
BuildRequires: make
BuildRequires: lzip
# for gpg verification
BuildRequires: gnupg2
BuildRequires:  oreon-rpm-macros

%description
ed is a line-oriented text editor, used to create, display, and modify text
files (both interactively and via shell scripts). For most purposes, ed has been
replaced in normal usage by full-screen editors (emacs and vi, for example).

%prep
%oreon_sha256

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}

%autosetup

%build
%set_build_flags
# Custom configure script; not Autoconf, so we do not use %%configure macro
./configure \
    --prefix=%{_prefix} \
    --exec-prefix=%{_exec_prefix} \
    --bindir=%{_bindir} \
    --datarootdir=%{_datadir} \
    --infodir=%{_infodir} \
    --mandir=%{_mandir} \
    --program-prefix=%{?_program_prefix} \
    CC="${CC-gcc}" \
    CPPFLAGS="${CPPFLAGS}" \
    CFLAGS="${CFLAGS}" \
    LDFLAGS="${LDFLAGS}"
%make_build

%install
%make_install
rm -vrf %{buildroot}%{_infodir}/dir

%check
%make_build check

%files
%license COPYING doc/fdl.texi
%doc ChangeLog NEWS README AUTHORS
%{_bindir}/ed
%{_bindir}/red
%{_mandir}/man1/ed.1*
%{_mandir}/man1/red.1*
%{_infodir}/ed.info*

