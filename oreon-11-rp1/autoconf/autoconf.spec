%global source0_hash 9fd672b1c8425fac2fa67fa0477b990987268b90ff36d5f016dae57be0d6b52e
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: autoconf
Version: 2.73
Release: 1%{?dist}
Summary: Generate configure scripts for source packages
License: GPL-3.0-or-later WITH Autoconf-exception-3.0
URL: https://www.gnu.org/software/autoconf/
Source0: https://ftp.gnu.org/gnu/autoconf/autoconf-%{version}.tar.xz
Source1: autoconf-%{version}.tar.xz.sig
Source2: autoconf-key.asc
BuildArch: noarch

Requires: m4
Requires: perl

BuildRequires: oreon-rpm-macros
BuildRequires: m4
BuildRequires: perl
BuildRequires: make
BuildRequires: gnupg2
%if %{without bootstrap} && !0%{?bootstrap}
%endif

%description
Autoconf produces portable shell scripts that configure source code
packages for the system they are built on.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n autoconf-%{version} -p1

%build
%oreon_configure M4=/usr/bin/m4
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_infodir}/dir
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
