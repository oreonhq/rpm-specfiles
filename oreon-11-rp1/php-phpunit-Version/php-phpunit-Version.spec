%global source0_hash a50e02a89c795a9d685e62577bec716821394a4832e8d1991a8b54a16faf9c86

# remirepo/fedora spec file for php-phpunit-Version
#
# Copyright (c) 2013-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    99732be0ddb3361e16ad77b68ba41efc8e979019
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   version
%global php_home     %{_datadir}/php/SebastianBergmann/
%global with_tests   %{?_without_tests:0}%{!?_withou_tests:1}

Name:           php-phpunit-Version
Version:        2.0.1
Release:        22%{?dist}
Summary:        Managing the version number of Git-hosted PHP projects

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=5.6"
Requires:       php(language) >= 5.6
Requires:       php-spl
Requires:       git
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(sebastian/version) = %{version}

%description
Library that helps with managing the version number
of Git-hosted PHP projects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

: Restore PSR-0 layout
mkdir src/Version

%build
: Generate autoloader
%{_bindir}/phpab \
  --template fedora \
  --output  src/Version/autoload.php \
  src

%install
mkdir -p %{buildroot}%{php_home}

cp -pr src/* %{buildroot}%{php_home}

%post
if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      pear.phpunit.de/Version >/dev/null || :
fi

%files
%license LICENSE
%doc README.md
%doc composer.json
%dir %{php_home}
     %{php_home}/Version*

%changelog
%autochangelog
