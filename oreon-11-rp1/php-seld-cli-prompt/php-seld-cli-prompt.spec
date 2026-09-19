%global source0_hash 45a21dd195773b360bed13bf3080da78371972603851370358ba48eb7396438f

# remirepo/fedora spec file for php-seld-cli-prompt
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    b8dfcf02094b8c03b40322c229493bb2884423c5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     Seldaek
%global gh_project   cli-prompt

Name:           php-seld-cli-prompt
Version:        1.0.4
Release:        13%{?dist}
Summary:        Allows you to prompt for user input on the command line

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

# Autoloader
Source1:        %{gh_project}-autoload.php

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3
# For test
BuildRequires:  php-cli
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)

# From composer.json
#       "php": ">=5.3.0",
Requires:       php(language) >= 5.3.0
# From phpcompatifo report for 1.0.0
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(seld/cli-prompt) = %{version}

%description
While prompting for user input using fgets() is quite easy, sometimes you
need to prompt for sensitive information. In these cases, the characters typed
in by the user should not be directly visible, and this is quite a pain to do
in a cross-platform way.

Autoloader: %{_datadir}/php/Seld/CliPrompt/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

cp %{SOURCE1} src/autoload.php

%build
# Nothing

%install
# Restore PSR-0 tree
mkdir -p     %{buildroot}%{_datadir}/php/Seld/CliPrompt
cp -pr src/* %{buildroot}%{_datadir}/php/Seld/CliPrompt/

%check
: Check if our autoloader works
php -r '
require "%{buildroot}%{_datadir}/php/Seld/CliPrompt/autoload.php";
$a = new \Seld\CliPrompt\CliPrompt();
echo "Ok\n";
exit(0);
'

%files
%license LICENSE
%doc README.md composer.json res/example.php
%{_datadir}/php/Seld

%changelog
%autochangelog
