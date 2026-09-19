%global source0_hash 7901169767966cb7e4b636612181032a182da5e1ee54fb5fd730de9414442b6e

#
# Fedora spec file for php-simplepie
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#
%global gh_commit    76cccb1b2c5dcaf44f304c925ab30c0f48643992
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     simplepie
%global gh_project   simplepie
%global gh_version   1.9.0
%bcond_with       tests

Name:       php-%{gh_project}
Version:    1.9.0
Release:    3%{?dist}
Summary:    A simple Atom/RSS parsing library for PHP

Group:      Development/Libraries
License:    BSD-3-Clause
URL:        http://simplepie.org/

# Use a git snapshot as upstream remove tests from distribution
Source0:       %{name}-%{gh_version}-%{gh_short}.tgz
# Script to pull the git snapshot
Source1:       %{name}-makesrc.sh

# Adapt autoloader for installation tree
Patch0:     %{name}-rpm.patch
# Adpat to phpunit7 and php 8
Patch1:     %{name}-tests.patch

BuildArch:  noarch
%if %{with tests}
# From composer.json, "require-dev"
#		"phpunit/phpunit": "~5.4.3 || ~6.5"
BuildRequires:    phpunit8
%global phpunit %{_bindir}/phpunit8
%endif

# from composer.json, "require"
#               "php": ">=5.6.0",
#               "ext-pcre": "*",
#               "ext-xml": "*",
#               "ext-xmlreader": "*"
Requires:    php(language) >= 5.6
Requires:    php-pcre
Requires:    php-xml
Requires:    php-xmlreader
# from composer.json, "suggests"
#               "ext-curl": "",
#               "ext-iconv": "",
#               "ext-intl": "",
#               "ext-mbstring": "",
Requires:    php-curl
Requires:    php-iconv
Requires:    php-intl
Requires:    php-mbstring
# from phpcompatinfo
Requires:    php-IDNA_Convert
Requires:    php-date
Requires:    php-dom
Requires:    php-libxml
Requires:    php-pdo
Requires:    php-reflection
# Optional: memcache, memcached, redis, zlib

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}

%description
SimplePie is a very fast and easy-to-use class, written in PHP, that puts the 
'simple' back into 'really simple syndication'. Flexible enough to suit 
beginners and veterans alike, SimplePie is focused on speed, ease of use, 
compatibility and standards compliance.

Autoloader: %{_datadir}/php/%{name}/autoloader.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{gh_project}-%{gh_commit}

#%patch0 -p1 -b .rpm
#%patch1 -p1 -b .php8

# fix rpmlint warnings
find . -type f -exec chmod -x {} \;
# drop demo; contains flash files
rm -rf demo

%build
#non-empty build section to quell the belching that rpmlint does with an empty build

%install
mkdir -p %{buildroot}/%{_datadir}/php/%{name}
cp -ar library src -t %{buildroot}/%{_datadir}/php/%{name}

install -pm 644 autoloader.php \
    %{buildroot}/%{_datadir}/php/%{name}/autoloader.php

%if %{with tests}
%check
sed -e 's:@PATH@:%{buildroot}/%{_datadir}/php/%{name}:' \
    -i tests/bootstrap.php

ret=0
for cmdarg in "php %{phpunit}" php; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit8} --verbose || ret=1
  fi
done
exit $ret
%endif

%files
%license LICENSES/
%doc composer.json
%doc README.markdown
%{_datadir}/php/%{name}

%changelog
%autochangelog
