%global source0_hash 242eefb0a920cf8a97cf129529ac6356287fe5f04eda761efff68fefbf11c8db
%global gh_commit    edf364cefe8c43501e21e88110aac10b284c3c9f
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     composer
%global gh_project   spdx-licenses
%global php_home     %{_datadir}/php
%bcond_without       tests
Name:           php-composer-spdx-licenses
Version:        1.6.0
Release:        1%{?dist}
Summary:        SPDX licenses list and validation library
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
Patch0:         %{name}-rpm.patch
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 5.3.2
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  phpunit9
# /oreon:deps
%description
SPDX licenses list and validation library.

Originally written as part of composer/composer,
now extracted and made available as a stand-alone library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p0 -b .rpm
find . -name \*.rpm -delete -print

%build

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Composer\\Spdx\\', __DIR__);
AUTOLOAD
%install
: Library
pushd src
for fic in *
do
  if ! grep $fic ../.gitattributes; then
    install -Dpm 0644 $fic %{buildroot}%{php_home}/Composer/Spdx/$fic
  fi
done
popd
: Resources
cp -pr res   %{buildroot}%{_datadir}/%{name}
%oreon_autofiles main

%check

%if %{with tests}
rm tests/SpdxLicensesUpdaterTest.php
export BUILDROOT_SPDX=%{buildroot}
sed -e  '/setUp()/s/$/:void/' -i tests/*.php
ret=0
for cmd in php php81 php82 php83 php84; do
  if which $cmd; then
    $cmd -d memory_limit=1G ${2:-%{_bindir}/phpunit9} \
      --bootstrap %{buildroot}%{php_home}/Composer/Spdx/autoload.php \
      --no-coverage \
      --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
