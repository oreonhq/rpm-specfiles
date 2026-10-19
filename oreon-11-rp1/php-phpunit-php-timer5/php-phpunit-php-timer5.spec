%global source0_hash 79151e4b45847aa828916431f13cd6e0121e6ade364146653156ce8dd121c5d7
%bcond_without       tests
%global gh_commit    5a63ce20ed1b5bf577850e2c4e87f4aa902afbd2
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-timer
%global pk_vendor    phpunit
%global pk_project   %{gh_project}
%global ns_vendor    SebastianBergmann
%global ns_project   Timer
%global major        5
%global php_home     %{_datadir}/php
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        7.0.0
Release:        1%{?dist}
Summary:        PHP Utility class for timing, version 5
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
Patch0:         https://patch-diff.githubusercontent.com/raw/sebastianbergmann/php-timer/pull/36.patch
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 7.3
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit9
# /oreon:deps
%description
Utility class for timing things, factored out of PHPUnit into a stand-alone
component.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}
%patch -P0 -p1

%build

phpab \
   --template fedora \
   --output  src/autoload.php \
   src
%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main
%if %{with tests}
%check

mkdir vendor
touch vendor/autoload.php
: Run upstream test suite
ret=0
for cmd in php php80 php81 php82; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit9 \
        --verbose || ret=1
  fi
done
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
