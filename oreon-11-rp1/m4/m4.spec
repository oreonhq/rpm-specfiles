%global source0_hash f25c6ab51548a73a75558742fb031e0625d6485fe5f9155949d6486a2408ab66
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: m4
Version: 1.4.21
Release: 1%{?dist}
Summary: GNU m4, the traditional Unix macro processor
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/m4/
Source0: https://ftp.gnu.org/gnu/m4/m4-1.4.21.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
GNU `m4' is an implementation of the traditional Unix macro processor. It is mostly SVR4 compatible, although it has some extensions (for example, handling more than 9 positional parameters to macros). `m4' also has built-in functions for including files, running shell commands, doing arithmetic, etc. Autoconf needs GNU `m4' for generating `configure' scripts, but not for running them.

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
