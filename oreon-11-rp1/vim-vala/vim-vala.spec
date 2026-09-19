%global source0_hash 6184e4bfc86f19ba061b1ecf07f0ed77fedb112c09f2747b57686865c99bf314

%global commit 44b2dfde07fb65e75e8b3a87b57f0c771efbbb13
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}

%global vimfilesdir %{_datadir}/vim/vimfiles

Name:           vim-vala
Version:        20251210g44b2dfd
Release:        %autorelease
Summary:        Vala syntax highlighting, indentation, snippets and more for Vim
License:        GPL-3.0-or-later and CC0-1.0
URL:            https://github.com/vala-lang/vala.vim
Source0:        https://github.com/vala-lang/vala.vim/archive/%commit/vala.vim-%{shortcommit}.tar.gz
Source1:        vim-vala.metainfo.xml
BuildArch:      noarch
Requires:       vim-data
Requires:       vim-filesystem
BuildRequires:  libappstream-glib

%description
This is a Vim plugin that provides file detection, syntax highlighting, proper
indentation, better Syntastic integration, code snippets and more for the Vala
programming language.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n vala.vim-%{commit}

%build

%install
install -m 755 -d %{buildroot}%{vimfilesdir}
files=$(ls | grep -v LICENSE | grep -v README.md)
tar cfp - $files | (cd %{buildroot}%{vimfilesdir}; tar xfp -)
# Conflict with vim-syntastic-vala package
rm %{buildroot}%{vimfilesdir}/syntax_checkers/vala/valac.vim
rmdir %{buildroot}%{vimfilesdir}/syntax_checkers/vala
rmdir %{buildroot}%{vimfilesdir}/syntax_checkers

install -Dpm0644 %{SOURCE1} %{buildroot}%{_metainfodir}/vim-vala.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/vim-vala.metainfo.xml

%files
%license LICENSE
%doc README.md
%{vimfilesdir}/UltiSnips
%{vimfilesdir}/*/vala.vim
%{_metainfodir}/vim-vala.metainfo.xml

%changelog
%autochangelog
