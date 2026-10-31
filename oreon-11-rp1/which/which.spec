%global source0_hash 1cb83e4f702e60b8211ab5ec4c2afbab1b1dec80209456a7d2faf7584ed225ea
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: which
Version: 2.25
Release: 1%{?dist}
Summary: Locate a program in PATH
License: GPL-3.0-only
URL: https://savannah.gnu.org/projects/which/
Source0: https://ftp.gnu.org/gnu/which/which-%{version}.tar.gz
Source1: which-%{version}.tar.gz.sig
Source2: which-key.gpg
Source3: which2.sh
Source4: which2.csh

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
which prints the full path of a program found in PATH.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1

%build
%oreon_configure
%oreon_make

%install
%oreon_make_install
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -p -m 644 %{SOURCE3} %{SOURCE4} %{buildroot}%{_sysconfdir}/profile.d/
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
