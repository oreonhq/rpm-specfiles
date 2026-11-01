%global source0_hash 4d7e4fdef2eca6afe07a2682151cea78781e0a4e8f9622142d9f70c083a2fd4f
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: help2man
Version: 1.49.3
Release: 1%{?dist}
Summary: Create manual pages from --help output
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/help2man/
Source0: https://ftp.gnu.org/gnu/help2man/help2man-%{version}.tar.xz
Source1: help2man-%{version}.tar.xz.sig
Source2: help2man-key.asc
BuildArch: noarch

Requires: perl

BuildRequires: oreon-rpm-macros
BuildRequires: perl
BuildRequires: make
BuildRequires: gnupg2
%if %{without bootstrap} && !0%{?bootstrap}
%endif

%description
help2man builds a simple manual page from the --help and --version
output of a program.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n help2man-%{version} -p1

%build
%oreon_configure --disable-nls
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_infodir}/dir
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
