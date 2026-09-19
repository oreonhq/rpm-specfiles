%global source0_hash d33ef2bbdd13a04da877dd8b13c0be9ecf37b7780e8d14d719bfbe93d97a67fd

# remirepo/fedora spec file for php-lukasreschke-id3parser
#
# Copyright (c) 2016 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    62f4de76d4eaa9ea13c66dacc1f22977dace6638
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     LukasReschke
%global gh_project   ID3Parser
%global pk_owner     lukasreschke
%global pk_project   id3parser

Name:           php-%{pk_owner}-%{pk_project}
Version:        0.0.3
Release:        22%{?dist}
Summary:        ID3 parser library

# https://github.com/LukasReschke/ID3Parser/issues/1
License:        GPL-1.0-or-later
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch

BuildRequires:  php(language) >= 5.4
BuildRequires:  %{_bindir}/phpab
BuildRequires:  %{_bindir}/php

# From composer.json, "require": {
#        "php": ">=5.4"
Requires:       php(language) >= 5.4
# From phpcompatifo report for 0.0.1
Requires:       php-date
Requires:       php-iconv
Requires:       php-pcre
Requires:       php-xml
Requires:       php-zlib

Provides:       php-composer(%{pk_owner}/%{pk_project}) = %{version}

%description
This is a pure ID3 parser based upon getID3.
It supports the following ID3 versions inside MP3 files:

* ID3v1 (v1.0 & v1.1)
* ID3v2 (v2.2, v2.3 & v2.4)

Autoloader: %{_datadir}/php/%{gh_project}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
: Generate autoloader
%{_bindir}/phpab --output src/autoload.php src

%install
mkdir -p   %{buildroot}%{_datadir}/php
cp -pr src %{buildroot}%{_datadir}/php/%{gh_project}

%check
: Check our autoloader
%{_bindir}/php -r '
  require "%{buildroot}%{_datadir}/php/%{gh_project}/autoload.php";
  $analyzer = new \ID3Parser\ID3Parser();
'

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md composer.json
%{_datadir}/php/%{gh_project}

%changelog
%autochangelog
