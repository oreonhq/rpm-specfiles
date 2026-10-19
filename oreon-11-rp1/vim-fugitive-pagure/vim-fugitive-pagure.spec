%global source0_hash f05b9c40edba3198cfdb93a9832eecd72dfbce400789588da802d7d72f51b6e1
Name: vim-fugitive-pagure
Version: 1.5
Release:        1%{?dist}
Summary:        Pagure support for vim-fugitive plugin
License: GPL-2.0-or-later
BuildArch: noarch
URL: https://github.com/FrostyX/vim-fugitive-pagure
Source0:        %{name}-%{version}.tar.gz
Requires: vim-common
Requires: vim-fugitive
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  vim-filesystem
# /oreon:deps
%description
Pagure support for :Gbrowse feature provided by vim-fugitive plugin

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%install
mkdir -p %{buildroot}%{vimfiles_root}/plugin
install -D -p -m 0644 plugin/* %{buildroot}%{vimfiles_root}/plugin/
%oreon_autofiles main

%check

python3 -B -m pytest . -v -s
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
