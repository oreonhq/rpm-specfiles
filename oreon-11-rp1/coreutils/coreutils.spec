%global source0_hash a480198559733e9b3da999e90543ac6f888a2caa544d8d664c5a1f17e528e210
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: coreutils
Version: 9.12
Release: 1%{?dist}
Summary: GNU core utilities
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/coreutils/
Source0: https://ftp.gnu.org/gnu/coreutils/coreutils-9.12.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
These are the GNU core utilities. This package is the union of the GNU fileutils, sh-utils, and textutils packages.

Most of these programs have significant advantages over their Unix counterparts, such as greater speed, additional options, and fewer arbitrary limits.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure --without-openssl --without-selinux --without-gmp
%oreon_make

%install
%oreon_make_install
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
