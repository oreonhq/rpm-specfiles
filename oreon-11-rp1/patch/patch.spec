%global source0_hash f87cee69eec2b4fcbf60a396b030ad6aa3415f192aa5f7ee84cad5e11f7f5ae3
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: patch
Version: 2.8
Release: 1%{?dist}
Summary: GNU patch
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/patch/
Source0: https://ftp.gnu.org/gnu/patch/patch-2.8.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
This is GNU patch, which applies diff files to original files.

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
