%global source0_hash cc9df4a26a0e84d0b326ccbf8fb1502c39a09c81ade0599ab51d5b92356ad933

# spec file for php-phpunit-git
#
# Copyright (c) 2013-2017 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    815bbbc963cf35e5413df195aa29df58243ecd24
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   git
%global php_home     %{_datadir}/php/SebastianBergmann
%global pear_name    Git
%global pear_channel pear.phpunit.de
%global with_tests   %{?_without_tests:1}%{!?_without_tests:0}

Name:           php-phpunit-git
Version:        2.1.4
Release:        21%{?dist}
Summary:        Simple wrapper for Git

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.3.3
BuildRequires:  php-fedora-autoloader-devel

Requires:       git
# From composer.json
#      "php": ">=5.3.3"
Requires:       php(language) >= 5.3.3
# From phpcompatinfo report for 2.1.2
Requires:       php-date
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(sebastian/git) = %{version}

# For compatibility with pear mode
Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
# Package have be renamed
Obsoletes:      php-phpunit-Git < 1.2.0-3
Provides:       php-phpunit-Git = %{version}-%{release}

%description
Simple PHP wrapper for Git.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
%{_bindir}/phpab \
  --template fedora \
  --output src/autoload.php \
  src

%install
mkdir -p   %{buildroot}%{php_home}
cp -pr src %{buildroot}%{php_home}/%{pear_name}

%post
if [ -x %{_bindir}/pear ]; then
   %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md
%doc composer.json
%dir %{php_home}
     %{php_home}/%{pear_name}

%changelog
%autochangelog
