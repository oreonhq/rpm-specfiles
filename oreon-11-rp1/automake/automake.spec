%global source0_hash e3e2c2e3abf37898138db5b6c1d1dc35c9160c5978be7947d2c741705251d445
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: automake
Version: 1.19
Release: 1%{?dist}
Summary: Generate GNU-standard Makefile.in files
License: GPL-2.0-or-later
URL: https://www.gnu.org/software/automake/
Source0: https://ftp.gnu.org/gnu/automake/automake-%{version}.tar.xz
Source1: automake-%{version}.tar.xz.sig
Source2: automake-key.asc
BuildArch: noarch

Requires: autoconf
Requires: perl

BuildRequires: oreon-rpm-macros
BuildRequires: autoconf
BuildRequires: perl
BuildRequires: make
BuildRequires: gnupg2
%if %{without bootstrap} && !0%{?bootstrap}
%endif

%description
Automake builds Makefile.in templates from Makefile.am descriptions,
for use with Autoconf generated configure scripts.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n automake-%{version} -p1

%build
%oreon_configure
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_infodir}/dir
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
