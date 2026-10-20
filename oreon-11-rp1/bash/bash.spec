%global source0_hash 0d5cd86965f869a26cf64f4b71be7b96f90a3ba8b3d74e27e8e9d9d5550f31ba
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: bash
Version: 5.3.20
Release: 1%{?dist}
Summary: GNU Bash, the GNU Project's Bourne Again SHell
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/bash/
Source0: https://ftp.gnu.org/gnu/bash/bash-5.3.tar.gz
Patch1: https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-001
Patch2: https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-002
Patch3: https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-003
Patch4: https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-004
Patch5: https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-005
Patch6: https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-006
Patch7: https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-007
Patch8: https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-008
Patch9: https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-009
Patch10: https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-010
Patch11: https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-011
Patch12: https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-012
Patch13: https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-013
Patch14: https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-014
Patch15: https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-015
Patch16: https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-016
Patch17: https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-017
Patch18: https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-018
Patch19: https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-019
Patch20: https://ftp.gnu.org/gnu/bash/bash-5.3-patches/bash53-020

BuildRequires: oreon-rpm-macros
BuildRequires: readline-devel
BuildRequires: ncurses-devel
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
This is GNU Bash, version 5.3. Bash is the GNU Project's Bourne Again SHell, a complete implementation of the POSIX shell spec, but also with interactive command line editing, job control on architectures that support it, csh-like features such as history substitution and brace expansion, and a slew of other features.

%prep
%oreon_sha256
%autosetup -n bash-5.3 -p0

%build
%oreon_configure --with-installed-readline --without-bash-malloc
%oreon_make

%install
%oreon_make_install
ln -sf bash %{buildroot}%{_bindir}/sh
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
