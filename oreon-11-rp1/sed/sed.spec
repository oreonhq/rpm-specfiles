%global source0_hash b8e72182b2ec96a3574e2998c47b7aaa64cc20ce000d8e9ac313cc07cecf28c7
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: sed
Version: 4.10
Release: 1%{?dist}
Summary: GNU sed, the Unix stream editor
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/sed/
Source0: https://ftp.gnu.org/gnu/sed/sed-4.10.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
This is the GNU implementation of sed, the Unix stream editor.

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
