%global source0_hash bfd19cb06cc71f3352d567e90284d8cdac02ac89774bbeadf0b533b0c11432fd
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: findutils
Version: 4.11.0
Release: 1%{?dist}
Summary: GNU find, xargs, and locate
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/findutils/
Source0: https://ftp.gnu.org/gnu/findutils/findutils-4.11.0.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
This package contains the GNU find, xargs, and locate programs. find and xargs comply with POSIX 1003.2. They also support a large number of additional options, some borrowed from Unix and some unique to GNU.

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
