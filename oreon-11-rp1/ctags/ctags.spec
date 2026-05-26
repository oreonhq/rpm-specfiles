Summary: A C programming language indexing and/or cross-reference tool
Name: ctags
Version: 6.2.1
Release: 3%{?dist}
License: GPL-2.0-or-later
URL: https://ctags.io/
Source0: https://github.com/universal-ctags/ctags/releases/download/v%{version}/universal-%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 2c63efe9e0e083dc50e6fdd8c5414781cc8873d8c8940cf553c01870ed962f8c
%global source0_file universal-ctags-6.2.1.tar.gz
# oreon url source checksums end

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: jansson-devel
BuildRequires: libseccomp-devel
BuildRequires: libxml2-devel
BuildRequires: libyaml-devel
BuildRequires: make
BuildRequires: pkgconfig
BuildRequires: python3-docutils

Obsoletes: %{name}-etags <= 5.8

%description
Ctags generates an index (or tag) file of C language objects found in
C source and header files.  The index makes it easy for text editors or
other utilities to locate the indexed items.  Ctags can also generate a
cross reference file which lists information about the various objects
found in a set of C language files in human readable form.  Exuberant
Ctags improves on ctags because it can find all types of C language tags,
including macro definitions, enumerated values (values inside enum{...}),
function and method definitions, enum/struct/union tags, external
function prototypes, typedef names and variable declarations.  Exuberant
Ctags is far less likely to be fooled by code containing #if preprocessor
conditional constructs than ctags.  Exuberant ctags supports output of
Emacs style TAGS files and can be used to print out a list of selected
objects found in source files.

Install ctags if you are going to use your system for C programming.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/universal-ctags-6.2.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2c63efe9e0e083dc50e6fdd8c5414781cc8873d8c8940cf553c01870ed962f8c" || { echo "oreon: Source0 SHA256 mismatch for universal-ctags-6.2.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n universal-%{name}-%{version}

%build
./autogen.sh
%configure

%make_build

%install
%make_install

%check
#make check

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_bindir}/optscript
%{_bindir}/readtags
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man7/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.2.1-3
- Prepare for Oreon 11 (RP1)
