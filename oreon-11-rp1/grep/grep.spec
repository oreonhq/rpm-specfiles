%global source0_hash 2649b27c0e90e632eadcd757be06c6e9a4f48d941de51e7c0f83ff76408a07b9
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: grep
Version: 3.12
Release: 1%{?dist}
Summary: GNU grep
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/grep/
Source0: https://ftp.gnu.org/gnu/grep/grep-3.12.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
This is GNU grep, the "fastest grep in the west" (we hope). All bugs reported in previous releases have been fixed. Many exciting new bugs have probably been introduced in this revision.

GNU grep is based on a fast lazy-state deterministic matcher hybridized with Boyer-Moore and Aho-Corasick searches for fixed strings that eliminate impossible text from being considered by the full regexp matcher without necessarily having to look at every character. The result is typically many times faster than traditional implementations. (Regular expressions containing back-references will run more slowly, however.)

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
