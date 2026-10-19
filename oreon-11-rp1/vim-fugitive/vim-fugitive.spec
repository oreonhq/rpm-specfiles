%global source0_hash 1deeb9fffe3e3299375842657cb2d6b7059a67d3373dc0ab52c16d7a7c99ea2a
Name: vim-fugitive
Version: 3.7
Release:        1%{?dist}
Summary:        A Git wrapper so awesome, it should be illegal
License: Vim
URL: https://github.com/tpope/vim-fugitive
Source0:        https://github.com/tpope/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: vim-fugitive.metainfo.xml
Requires: vim-common
%if %{defined el7}
Requires(post): %{_bindir}/vim
Requires(postun): %{_bindir}/vim
%endif
BuildArch: noarch
# oreon:deps
BuildRequires:  libappstream-glib
BuildRequires:  vim-filesystem
# /oreon:deps
%description
Fugitive is the premier Vim plugin for Git. Or maybe it's the premier Git
plugin for Vim? Either way, it's "so awesome, it should be illegal". That's why
it's called Fugitive.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%install
install -D -p -m 0644 autoload/fugitive.vim %{buildroot}%{vimfiles_root}/autoload/fugitive.vim
install -D -p -m 0644 doc/fugitive.txt %{buildroot}%{vimfiles_root}/doc/fugitive.txt
install -D -p -m 0644 ftdetect/fugitive.vim %{buildroot}%{vimfiles_root}/ftdetect/fugitive.vim
install -D -p -m 0644 ftplugin/fugitiveblame.vim %{buildroot}%{vimfiles_root}/ftplugin/fugitiveblame.vim
install -D -p -m 0644 plugin/fugitive.vim %{buildroot}%{vimfiles_root}/plugin/fugitive.vim
install -D -p -m 0644 syntax/fugitive.vim %{buildroot}%{vimfiles_root}/syntax/fugitive.vim
install -D -p -m 0644 syntax/fugitiveblame.vim %{buildroot}%{vimfiles_root}/syntax/fugitiveblame.vim
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_metainfodir}/vim-fugitive.metainfo.xml
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%if %{defined el7}
%post

vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null
%postun

> %{vimfiles_root}/doc/tags
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
