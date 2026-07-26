%global source0_hash de3f45952ff9f3cd165a1266e243521e8ed8cea5b7033b6120154a984f35a63c

%global commit      26e5737264354be41cb11d16d48132779795e168
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           vim-mediawiki
Version:        0.2^1.%{shortcommit}
Release:        %autorelease
Summary:        Vim syntax highlighting for MediaWiki
License:        LicenseRef-Fedora-Public-Domain
URL:            https://github.com/chikamichi/mediawiki.vim
Source:         %{url}/archive/%{commit}/mediawiki.vim-%{shortcommit}.tar.gz
BuildArch:      noarch
# for %%vimfiles_root macro
BuildRequires:  vim-filesystem
Requires:       vim-filesystem

%description
Syntax highlighting for MediaWiki-based projects, such as Wikipedia.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n mediawiki.vim-%{commit}

%install
install -D -p -m 0644 autoload/mediawiki.vim %{buildroot}%{vimfiles_root}/autoload/mediawiki.vim
install -D -p -m 0644 ftdetect/mediawiki.vim %{buildroot}%{vimfiles_root}/ftdetect/mediawiki.vim
install -D -p -m 0644 ftplugin/mediawiki.vim %{buildroot}%{vimfiles_root}/ftplugin/mediawiki.vim
install -D -p -m 0644 syntax/mediawiki.vim   %{buildroot}%{vimfiles_root}/syntax/mediawiki.vim

%files
%doc README.md
%{vimfiles_root}/autoload/mediawiki.vim
%{vimfiles_root}/ftdetect/mediawiki.vim
%{vimfiles_root}/ftplugin/mediawiki.vim
%{vimfiles_root}/syntax/mediawiki.vim

%changelog
%autochangelog
