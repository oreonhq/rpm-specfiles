%global source0_hash ae0064d4ae00cfa7fb5363592914fb3573dcf8bf1f608794b499c53e4f698b57
%global github_owner     phpDocumentor
%global github_name      ReflectionCommon
%global github_version   2.2.0
%global github_commit    1d01c49d4ed62f25aa84a747ad35d5a16924662b
%global composer_vendor  phpdocumentor
%global composer_project reflection-common
%global major            2
%global php_min_ver 7.2
%global with_tests 0%{!?_without_tests:1}
%{!?phpdir:  %global phpdir  %{_datadir}/php}
Name:          php-%{composer_vendor}-%{composer_project}%{major}
Version:       %{github_version}
Release:        1%{?dist}
Summary:        Common reflection classes used by phpdocumentor
Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:        %{name}-%{version}-%{github_commit}.tar.gz
Source1:       makesrc.sh
BuildArch:     noarch
%if %{with_tests}
%endif
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(fedora/autoloader)
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit9
# /oreon:deps
%description
Common reflection classes used by phpdocumentor to reflect the code structure.

Autoloader: %{phpdir}/phpDocumentor/Reflection%{major}/autoload-common.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

%build

: Create autoloader
%{_bindir}/phpab --template fedora --output src/autoload-common.php src
%install
mkdir -p %{buildroot}%{phpdir}/phpDocumentor
cp -rp src %{buildroot}%{phpdir}/phpDocumentor/Reflection%{major}
%oreon_autofiles main

%check

%if %{with_tests}
BOOTSTRAP=%{buildroot}%{phpdir}/phpDocumentor/Reflection%{major}/autoload-common.php
mkdir vendor
touch vendor/autoload.php
: Upstream tests
RETURN_CODE=0
for PHP_EXEC in php php81 php82 php83 php84; do
    if which $PHP_EXEC; then
        $PHP_EXEC -d auto_prepend_file=$BOOTSTRAP \
            %{_bindir}/phpunit9 --no-coverage || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
