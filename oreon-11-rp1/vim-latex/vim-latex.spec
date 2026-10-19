%global source1_hash d1174d2b573914320e5f8c29af6006d9877f0450e20e0aa0ec64b27b7da61c68
%global source0_hash f1a9d2d0446c99d9fa0fa83386609ee5201a0de3f1e7ff4aae8d40763ed84f6d
Name:		vim-latex
Version:	1.10.0
Release:        1%{?dist}
Summary:        Tools to view, edit and compile LaTeX documents in Vim
License:	Vim
URL:		http://vim-latex.sourceforge.net/
Source0:        http://downloads.sourceforge.net/vim-latex/vim-latex-%{version}.tar.gz
Source1:	http://downloads.sourceforge.net/vim-latex/vim-latex-%{version}.tar.gz.asc
Source2:	vim-latex-gpgkeys.gpg
Patch0:		vim-latex-1.10.0-Interpret-outline.py-by-Python-3.patch
BuildArch:	noarch
Requires:	vim-filesystem
Requires:	tex(latex)
Requires:	xdvi
# oreon:deps
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gnupg2
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  vim-filesystem
# /oreon:deps
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

%make_build -C doc
%install
%make_install VIMDIR=%{vimfiles_root} BINDIR=%{_bindir} PREFIX=%{_prefix}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n vim-latex-doc -f %{oreon_filedir}/vim-latex-doc.list

%changelog

%autochangelog
