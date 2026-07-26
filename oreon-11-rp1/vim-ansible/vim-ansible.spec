%global source0_hash 497c3343fc92146fa3db040b61a11b49a6fd332925c25e8cd2d51bc5832f842d

Name:           vim-ansible
Version:        3.4
Release:        %autorelease
Summary:        Vim plugin for syntax highlighting ansible's common filetypes
License:        MIT AND BSD-3-Clause
URL:            https://github.com/pearofducks/ansible-vim
Source0:        %{url}/archive/%{version}/ansible-vim-%{version}.tar.gz
BuildArch:      noarch
# for %%vimfiles_root macro
BuildRequires:  vim-filesystem
Requires:       vim-filesystem

%description
This is a vim syntax plugin for Ansible 2.x, it supports YAML playbooks, Jinja2
templates, and Ansible's hosts files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ansible-vim-%{version}
mv syntax/jinja2.vim_LICENSE LICENSE_jinja2.vim

%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -r --preserve=mode,timestamps ftdetect ftplugin indent syntax %{buildroot}%{vimfiles_root}

%files
%license LICENSE LICENSE_jinja2.vim
%doc README.md
%{vimfiles_root}/ftdetect/ansible.vim
%{vimfiles_root}/ftplugin/ansible.vim
%{vimfiles_root}/ftplugin/ansible_hosts.vim
%{vimfiles_root}/indent/ansible.vim
%{vimfiles_root}/syntax/ansible.vim
%{vimfiles_root}/syntax/ansible_hosts.vim
%{vimfiles_root}/syntax/jinja2.vim

%changelog
%autochangelog
