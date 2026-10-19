%global source0_hash be3ce93dbd5edde07c5d0e1efdc91a0ac47d2c57f48fceef6c7ba57ffafbf365
%global gh_commit    4cdce31c1b5120779a01225b5b0968f9321342d6
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     theseer
%global gh_project   DirectoryScanner
%global php_home     %{_datadir}/php/TheSeer
%global pear_name    DirectoryScanner
%global pear_channel pear.netpirates.net
%bcond_with     tests
Name:           php-theseer-directoryscanner
Version:        1.3.3
Release:        1%{?dist}
Summary:        A recursive directory scanner and filter
License:        BSD-2-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}.tar.gz
Patch0:         %{name}-tests.patch
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 5.3.1
Requires:       php-fileinfo
Provides:       php-composer(theseer/directoryscanner) = %{version}
Provides:       php-pear(%{pear_channel}/%{pear_name}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  phpunit9
# /oreon:deps
%description
A recursive directory scanner and filter.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}
%patch -P0 -p1

%build

%install
mkdir -p   %{buildroot}%{php_home}
cp -pr src %{buildroot}%{php_home}/%{gh_project}
%oreon_autofiles main

%check

%if %{with tests}
cat << 'EOF' | tee bs.php
<?php
require_once '%{buildroot}%{php_home}/%{gh_project}/autoload.php';
EOF
ret=0
for cmd in php php81 php82 php83 php84; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 \
         --bootstrap bs.php \
         --verbose \
         --no-coverage \
         --do-not-cache-result \
         --test-suffix=.test.php \
         --no-configuration \
         tests || ret=1
  fi
done
exit $ret
%endif
%post

if [ -x %{_bindir}/pear ]; then
  %{_bindir}/pear uninstall --nodeps --ignore-errors --register-only \
      %{pear_channel}/%{pear_name} >/dev/null || :
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
