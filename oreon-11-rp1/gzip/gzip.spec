%global source0_hash 9aa0cc780dec156b8282844833b342ab7cb08c25d2cd9a1869cdd0df31deff48
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: gzip
Version: 1.15
Release: 1%{?dist}
Summary: gzip (GNU zip)
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/gzip/
Source0: https://ftp.gnu.org/gnu/gzip/gzip-1.15.tar.xz
Patch0: gzip-1.15-aarch64-head.patch

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
gzip (GNU zip) is a compression utility designed to be a replacement for 'compress'. Its main advantages over compress are much better compression and freedom from patented algorithms. The GNU Project uses it as the standard compression program for its system.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure
%oreon_make

%install
%oreon_make_install
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
