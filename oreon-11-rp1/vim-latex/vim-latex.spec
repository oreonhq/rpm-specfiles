%global source0_hash f1a9d2d0446c99d9fa0fa83386609ee5201a0de3f1e7ff4aae8d40763ed84f6d

Name:		vim-latex
Version:	1.10.0
Release:	18%{?dist}
Summary:	Tools to view, edit and compile LaTeX documents in Vim
# According to doc/latex-suite license is Vim charityware license
License:	Vim
URL:		http://vim-latex.sourceforge.net/
Source0:	http://downloads.sourceforge.net/vim-latex/vim-latex-%{version}.tar.gz
Source1:	http://downloads.sourceforge.net/vim-latex/vim-latex-%{version}.tar.gz.asc
Source2:	vim-latex-gpgkeys.gpg
# Use Python 3, bug #1676189
Patch0:		vim-latex-1.10.0-Interpret-outline.py-by-Python-3.patch
BuildArch:	noarch

# We need vim-filesystem for dir ownership
Requires:	vim-filesystem
# Needed for compilation
Requires:	tex(latex)
# Needed for display
Requires:	xdvi

# Needed for vim macros
BuildRequires: vim-filesystem

# Needed to build documentation
BuildRequires:	make
BuildRequires:	libxslt
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-dtds

# For source verification with gpgv
BuildRequires:	gnupg2

%description
A comprehensive set of tools to view, edit and compile LaTeX documents without
needing to ever quit Vim. Together, they provide tools starting from macros to
speed up editing LaTeX documents to compiling TeX files to forward searching
.dvi documents.

%package doc
Summary:	Documentation for vim-latex

%description doc
Documentation for vim-latex.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
# build documentation
%make_build -C doc

%install
# Install files
%make_install VIMDIR=%{vimfiles_root} BINDIR=%{_bindir} PREFIX=%{_prefix}

%files
%doc %{vimfiles_root}/doc/imaps.txt
%doc %{vimfiles_root}/doc/latex*.txt
%{_bindir}/latextags
%{_bindir}/ltags
%{_datadir}/appdata/vim-latex.metainfo.xml
%{vimfiles_root}/compiler/*
%{vimfiles_root}/ftplugin/*
%{vimfiles_root}/indent/*
%{vimfiles_root}/plugin/*

%files doc
%doc doc/latex-suite doc/latex-suite-quickstart

%changelog
%autochangelog
