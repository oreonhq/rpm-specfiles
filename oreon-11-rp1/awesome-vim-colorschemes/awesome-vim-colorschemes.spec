%global source0_hash 3627d77d19118dd5bb48986e67beed74dd303de5369d37ebd90285eb76175b6d
%global commit ae5e02298c8de6a5aa98fe4d29a21874cfcc3619
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20240722
Name: awesome-vim-colorschemes
Version: 0
Release:        1%{?dist}
Summary:        Collection of color schemes for Neo/vim, merged for quick use
BuildArch: noarch
License: Vim AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-CC-BY
URL: https://github.com/rafi/awesome-vim-colorschemes
Source0:        https://github.com/rafi/%{name}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1: %{name}.metainfo.xml
Patch0: https://github.com/rafi/awesome-vim-colorschemes/pull/13#/remove-executable-bit-&-fix-wrong-file-end-of-line-encoding.patch
Requires: vim-enhanced
Requires: vim-jellybeans
# oreon:deps
BuildRequires:  libappstream-glib
BuildRequires:  vim-filesystem
# /oreon:deps
%description
Collection of awesome color schemes for Neo/vim, merged for quick use.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p1
# There is a separate vim-jellybeans package
# We do not want an implicit conflict to show up later
rm -rf colors/jellybeans.vim

%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -a {autoload,colors} %{buildroot}%{vimfiles_root}
install -Dpm0644 %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
