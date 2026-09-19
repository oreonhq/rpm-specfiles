%global source0_hash 0197170058032d2f59604921bcb95959fe9d6c75f1f7046594a4beebf399bbc2

%global commit  5540b3faa2288b226a8d9a4e8244558b12c598aa
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20230228

Name:           vim-trailing-whitespace
Version:        1.0
Release:        9.%{date}git%{shortcommit}.%autorelease
Summary:        Highlights trailing whitespace in red and provides :FixWhitespace to fix it

# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA
URL:            https://github.com/bronson/vim-trailing-whitespace
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        %{name}.metainfo.xml
BuildArch:      noarch

BuildRequires:  libappstream-glib
BuildRequires:  vim-filesystem

Requires:       vim-enhanced

%description
This plugin causes all trailing whitespace to be highlighted in red.

To fix the whitespace errors, just call :FixWhitespace. By default it operates
on the entire file. Pass a range (or use V to select some lines) to restrict
the portion of the file that gets fixed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p1

%install
mkdir -p        %{buildroot}%{vimfiles_root}
cp -ar plugin   %{buildroot}%{vimfiles_root}
install -m0644 -Dp %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%doc README doc/*
%{vimfiles_root}/plugin/*
%{_metainfodir}/*.xml

%changelog
%autochangelog
