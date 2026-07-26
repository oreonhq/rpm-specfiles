%global source0_hash a20f6bfb6914b24e5ec9b2df0f078eb8a29dc6d55af631c136e1b6efcfcc8d48

Name:		php-email-address-validation
Summary:	PHP class for validating email addresses
License:	BSD-2-Clause

Version:	2.0.1
Release:	16%{?dist}

%global repo_owner	aziraphale
%global repo_name	email-address-validator
URL:		https://github.com/%{repo_owner}/%{repo_name}
Source0:	%{URL}/archive/%{version}/%{repo_name}-%{version}.tar.gz

Patch0:	0000-update-tests-for-phpunit10.patch

BuildArch:	noarch

BuildRequires:	php-composer(phpunit/phpunit) >= 10
BuildRequires:	php-composer(phpunit/phpunit) < 11

Requires:	php-common
Requires:	php-pcre

Provides:	php-composer(aziraphale/email-address-validator) = %{version}

%description
This PHP class is used to check email addresses for technical validity.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{repo_name}-%{version} -p1
# Replace \r\n endlines with \n
sed -i 's/\r$//g' ./EmailAddressValidator.php tests/EmailAddressValidatorTest.php

%build
# nothing to do here

%install
install -m 755 -d %{buildroot}%{_datadir}/php/%{name}
install -m 644 -p EmailAddressValidator.php %{buildroot}%{_datadir}/php/%{name}/

%check
phpunit10 --bootstrap %{buildroot}%{_datadir}/php/%{name}/EmailAddressValidator.php

%files
%doc tests/
%doc composer.json
%{_datadir}/php/%{name}

%changelog
%autochangelog
