%global source0_hash aaa0f7696f17f74f42d97d0880aa088f5d68ed3079f3ed15d13b6e74909d3132

Name:		halibut
Summary:	TeX-like software manual tool
Version:	1.3
Release:	12%{?dist}
License:	MIT and APAFML
URL:		http://www.chiark.greenend.org.uk/~sgtatham/halibut.html
Source0:	http://www.chiark.greenend.org.uk/~sgtatham/halibut/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:	gcc
BuildRequires:	perl-interpreter
BuildRequires:	make
BuildRequires:	cmake
# Already fixed upstream
Patch:		halibut-1.3-cmake-4-fix.patch

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

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
install -Dpm 0644 misc/halibut.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/halibut.vim

%files
%doc LICENCE
%doc %{_docdir}/%{name}/*.html
%{_bindir}/%{name}
%{_infodir}/*
%{_mandir}/man1/*.1*

%files -n vim-halibut
%doc LICENCE
%{_datadir}/vim/vimfiles/syntax/*.vim

%changelog
%autochangelog
