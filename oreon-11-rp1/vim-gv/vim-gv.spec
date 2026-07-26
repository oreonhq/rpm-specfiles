%global source0_hash 7b34b59d18745e95419a5e842e342872d2e804b171ae479873eac323747864fb

%global commit  320cc8c477c5acc4fa0e52a460d87b2af54fa051
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20221025

Name:           vim-gv
Version:        0
Release:        15.%{date}git%{shortcommit}.%autorelease
Summary:        Git commit browser in Vim
BuildArch:      noarch

License:        MIT
URL:            https://github.com/junegunn/gv.vim
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        %{name}.metainfo.xml

BuildRequires:  libappstream-glib
BuildRequires:  vim-filesystem

Requires:       vim-enhanced
Requires:       vim-fugitive

%description
A git commit browser.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n gv.vim-%{commit}

%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -rp plugin %{buildroot}%{vimfiles_root}
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%doc README.md test/
%{vimfiles_root}/plugin/*
%{_metainfodir}/*.xml

%changelog
%autochangelog
