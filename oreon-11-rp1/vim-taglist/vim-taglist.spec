%global source0_hash 524e2a7001d1cf23449c443293b6e21aa654a1a238a52b6edce7f12d0cd98ba1

%global baseversion 46
%global zipversion 46
%global zipname taglist
#used for pre-releases:
%global vimfiles_root %{_datadir}/vim/vimfiles

Summary:          The taglist plugin for VIM editor
Name:             vim-%{zipname}
Version:          %{baseversion}
Release:          1%{?dist}

License:          Vim
URL:              http://vim-taglist.sourceforge.net/
Source:           https://sourceforge.net/projects/vim-taglist/files/vim-taglist/4.6/taglist_46.zip
Source1:          %{name}.metainfo.xml

Requires:         vim-common
Requires(post):   vim
Requires(postun): vim
Requires:         ctags
BuildRequires:    desktop-file-utils
BuildArch:        noarch

%description
The "Tag List" plugin is a source code browser plugin for vim and provides
an overview of the structure of source code files and allows you to efficiently
browse through source code files for different programming languages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c taglist -q -n %{zipname}

cp %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}/%{vimfiles_root}
cp -ar {doc,plugin} %{buildroot}%{vimfiles_root}
chmod 644 %{buildroot}%{vimfiles_root}/doc/*
mkdir -p %{buildroot}%{_datadir}/appdata
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/

%post
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null

%postun
rm %{vimfiles_root}/doc/tags
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null

%files 
%{vimfiles_root}/plugin/*
%doc %{vimfiles_root}/doc/*
%{_datadir}/appdata/%{name}.metainfo.xml

%changelog
%autochangelog
