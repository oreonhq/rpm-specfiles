%global source0_hash a5af9da05e3a65c530523edf7d10f090bad265fed4fe98c8892212e5a8f7919a

%global revdate     20191014
%global gitrevision 5130596a65330a4e8523d3ac1582f6c31ea6bc63
%global gitrev      %(full=%gitrevision ; echo ${full:0:6} )
%global posttag     %{revdate}git%{gitrev}

Name: vim-rhubarb
Version: 0
Release: 14.%{posttag}%{?dist}
Summary: GitHub support for vim-fugitive plugin
License: Vim
BuildArch: noarch

URL: https://github.com/tpope/vim-rhubarb
Source0: https://github.com/tpope/%name/archive/%gitrevision/%name-%gitrevision.tar.gz

Requires: vim-common
Requires: vim-fugitive

BuildRequires: vim-filesystem

%description
GitHub support for vim-fugitive plugin.  Enables :Gbrowse from fugitive.vim to
open GitHub URLs.  Sets up :Git to use hub if installed rather than git (when
available).  In commit messages, GitHub issues, issue URLs, and collaborators
can be omni-completed (<C-X><C-O>, see :help compl-omni).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %name-%gitrevision

%install
mkdir -p %{buildroot}%{vimfiles_root}/autoload
mkdir -p %{buildroot}%{vimfiles_root}/doc
mkdir -p %{buildroot}%{vimfiles_root}/plugin

install -p -m 0644 doc/rhubarb.txt %{buildroot}%{vimfiles_root}/doc
install -p -m 0644 plugin/rhubarb.vim %{buildroot}%{vimfiles_root}/plugin
install -p -m 0644 autoload/rhubarb.vim %{buildroot}%{vimfiles_root}/autoload

%files
# license file requested: https://github.com/tpope/vim-rhubarb/issues/55
%doc %{vimfiles_root}/doc/rhubarb.txt
%{vimfiles_root}/plugin/rhubarb.vim
%{vimfiles_root}/autoload/rhubarb.vim

%changelog
%autochangelog
