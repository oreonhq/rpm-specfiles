%global source0_hash aaa0f7696f17f74f42d97d0880aa088f5d68ed3079f3ed15d13b6e74909d3132
Name:		halibut
Summary:        TeX-like software manual tool
Version:	1.3
Release:        1%{?dist}
License:	MIT and APAFML
URL:		http://www.chiark.greenend.org.uk/~sgtatham/halibut.html
Source0:        http://www.chiark.greenend.org.uk/~sgtatham/halibut/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch:		halibut-1.3-cmake-4-fix.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Halibut is yet another text formatting system, intended primarily for
writing software documentation. It accepts a single source format and
outputs a variety of formats, planned to include text, HTML, Texinfo,
Windows Help, Windows HTMLHelp, PostScript and PDF. It has comprehensive
indexing and cross-referencing support, and generates hyperlinks within
output documents wherever possible.

%package -n vim-halibut
Summary:	Syntax file for the halibut manual tool
Requires:	vim-filesystem
BuildArch:	noarch
%description -n vim-halibut
This package provides vim syntax support for Halibut input files (*.but).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
install -Dpm 0644 misc/halibut.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/halibut.vim
%oreon_autofiles vim-halibut usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n vim-halibut -f %{oreon_filedir}/vim-halibut.list

%changelog

%autochangelog
