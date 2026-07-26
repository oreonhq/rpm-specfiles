%global source0_hash 7f0f3e870674458548bf219cba70ae11a5a7076399ca3fc2380982b61fb9d2da

%global vimfiles_root %{_datadir}/vim/vimfiles

Name:             vim-omnicppcomplete
Version:          0.41
Release:          27%{?dist}
Summary:          vim c++ completion omnifunc with a ctags database

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later
URL:              http://www.vim.org/scripts/script.php?script_id=1520
Source0:          http://www.vim.org/scripts/download_script.php?src_id=7722#/omnicppcomplete-%{version}.zip
Patch0:           license.patch

Requires:         ctags
Requires:         vim-filesystem
Requires(post):   vim
Requires(postun): vim

BuildArch:      noarch

%description
This script is for vim 7.0 or higher, it provides C/C++ completion thanks to a
ctags database.

Features :

 - Complete namespaces, classes, structs and union members.
 - Complete inherited members for classes and structs (single and multiple
   inheritance).
 - Complete attribute members eg: myObject->_child->_child etc...
 - Complete type returned by a function eg: myObject->get()->_child.
 - Complete the "this" pointer.
 - Complete a typedef.
 - Complete the current scope (global and class scope).
 - Complete an object after a cast (C and C++ cast).
 - Complete anonymous types (eg: struct {int a; int b;}g_Var; g_Var.???). It
   also works for a typedef of an anonymous type.

Notes :
 - The script manage cached datas for optimization.
 - Ambiguous namespaces are detected and are not included in the context stack.
 - The parsed code is tokenized so you can run a completion even if the current
   instruction has bad indentation, spaces, comments or carriage returns
   between words
   (even if it is not realistic).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c omnicppcomplete-%{version}
%patch -P0 -p1

%build

%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -ar {after,autoload,doc} %{buildroot}%{vimfiles_root}

%post
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null

%postun
rm %{vimfiles_root}/doc/tags
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null

%files
%doc %{vimfiles_root}/doc/*
%{vimfiles_root}/after
%{vimfiles_root}/autoload

%changelog
%autochangelog
