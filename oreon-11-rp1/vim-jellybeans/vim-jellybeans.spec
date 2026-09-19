%global source0_hash 608906d5d5e0d805486ef3e4bc37b149744c0f15a37d9fb1cde0d83eaa674957

Name:           vim-jellybeans
Version:        1.7
Release:        15%{?dist}
Summary:        A colorful, dark color scheme for Vim
License:        MIT
URL:            https://github.com/nanotech/jellybeans.vim
Source0:        %{url}/archive/v%{version}/jellybeans.vim-%{version}.tar.gz
# extracted from source code comments
Source1:        LICENSE
BuildArch:      noarch
# for %%vimfiles_root macro
BuildRequires:  vim-filesystem
Requires:       vim-filesystem

%description
A colorful, dark color scheme for Vim.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n jellybeans.vim-%{version}
cp %{S:1} .

%install
install -D -p -m 644 colors/jellybeans.vim %{buildroot}%{vimfiles_root}/colors/jellybeans.vim

%files
%license LICENSE
%doc README.markdown
%{vimfiles_root}/colors/jellybeans.vim

%changelog
%autochangelog
