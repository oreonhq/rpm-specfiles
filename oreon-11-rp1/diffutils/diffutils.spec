%global source0_hash 7c8b7f9fc8609141fdea9cece85249d308624391ff61dedaf528fcb337727dfd
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: diffutils
Version: 3.12
Release: 1%{?dist}
Summary: GNU diff, diff3, sdiff, and cmp
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/diffutils/
Source0: https://ftp.gnu.org/gnu/diffutils/diffutils-3.12.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
This directory contains the GNU diff, diff3, sdiff, and cmp utilities. Their features are a superset of the Unix features and they are significantly faster.

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
