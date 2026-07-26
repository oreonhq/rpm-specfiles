%global source0_hash f8593801fcea340dfbd2a46965206a013acbf356a88f680553de6decaaa9f7eb

# remirepo/fedora spec file for php-seld-phar-utils
#
# Copyright (c) 2015-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    ea2f4014f163c1be4c601b9b7bd6af81ba8d701c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     Seldaek
%global gh_project   phar-utils

Name:           php-seld-phar-utils
Version:        1.2.1
Release:        9%{?dist}
Summary:        PHAR file format utilities

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3
# For test
BuildRequires:  php-cli
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json
#       "php": ">=5.3.0",
Requires:       php(language) >= 5.3.0
# From phpcompatifo report for 1.0.1
Requires:       php-date
Requires:       php-hash
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(seld/phar-utils) = %{version}

%description
PHAR file format utilities, for when PHP phars you up.

To use this library, you just have to add, in your project:
  require_once '%{_datadir}/php/Seld/PharUtils/autoload.php';

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

phpab --template fedora --output src/autoload.php src

%build
# Nothing

%install
# Restore PSR-0 tree
mkdir -p     %{buildroot}%{_datadir}/php/Seld/PharUtils/
cp -pr src/* %{buildroot}%{_datadir}/php/Seld/PharUtils/

%check
: Check if our autoloader works
php -r '
require "%{buildroot}%{_datadir}/php/Seld/PharUtils/autoload.php";
$a = new \Seld\PharUtils\Timestamps("%{SOURCE1}");
echo "Ok\n";
exit(0);
'

%files
%license LICENSE
%doc README.md
%doc composer.json
%{_datadir}/php/Seld

%changelog
%autochangelog
