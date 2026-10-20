%global source0_hash 07f6f7342b7febe4313fc2c2542ad93d64fe20ad8717200109f105a826f5fd37
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: gawk
Version: 5.4.1
Release: 1%{?dist}
Summary: GNU Awk
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/gawk/
Source0: https://ftp.gnu.org/gnu/gawk/gawk-5.4.1.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
This is GNU Awk 5.4.0. It is upwardly compatible with Brian Kernighan's version of Unix awk. It is almost completely compliant with the 2024 POSIX 1003 standard for awk.

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
