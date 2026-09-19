%global source0_hash e169429a6a4bce5a32b94a3d7cc784c746f9d4fd78354122895ba50ded867afa

#used for pre-releases:
%global vimfiles_root %{_datadir}/vim/vimfiles
%global _python_bytecompile_extra 0

Name:          vim-jedi
Version:       0.11.2
Release:       11%{?dist}
Summary:       The Jedi vim plugin

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:       LGPL-3.0-only
URL:           https://github.com/davidhalter/jedi-vim
Source0:       https://github.com/davidhalter/jedi-vim/archive/%{version}/jedi-vim-%{version}.tar.gz
Source1:       %{name}.metainfo.xml

#Patch0:        jedi-vim-0.9.0-fix-debug.patch

Requires:      python3-jedi
Requires:      vim-common
BuildRequires: python3-devel
BuildRequires: python3-libs

BuildArch:     noarch

%description
vim-jedi is a VIM binding to the awesome auto completion library Jedi.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n jedi-vim-%{version}

cp %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -ar {doc,after,autoload,ftplugin,plugin} %{buildroot}%{vimfiles_root}
mkdir -p %{buildroot}/%{_datadir}/appdata
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/

mkdir -p %buildroot/%python3_sitelib
install -m 644 pythonx/*.py %buildroot/%python3_sitelib

%files
%doc README.rst AUTHORS.txt LICENSE.txt
%doc %{vimfiles_root}/doc/*
%{vimfiles_root}/after/*
%{vimfiles_root}/autoload/*
%{vimfiles_root}/ftplugin/*
%{vimfiles_root}/plugin/*
%{_datadir}/appdata/%{name}.metainfo.xml
%{python3_sitelib}/jedi_vim.py*
%{python3_sitelib}/jedi_vim_debug.py*
%{python3_sitelib}/__pycache__/jedi_vim*

%changelog
%autochangelog
