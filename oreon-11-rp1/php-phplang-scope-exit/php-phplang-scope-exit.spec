%global source0_hash ea6b115727cd6ba3dc7399a82ec4321072d0d00914c6efb17169079c1cc283e1
%global with_tests   0%{!?_without_tests:1}
%global gh_commit    8b5a1cbc54df7c1d14916711fb339e67d08cb3dd
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phplang
%global gh_project   scope-exit
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
%global ns_vendor    PhpLang
%global ns_project   %nil
%global major        %nil
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Emulation of SCOPE_EXIT construct from C++
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
BuildArch:      noarch
%if %{with_tests}
%global phpunit %{_bindir}/phpunit10
%endif
Requires:       php(language)
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit10
# /oreon:deps
%description
This simple class provides an implementation of C++'s SCOPE_EXIT, or GoLang's
defer.

To use, assign an instance of this object to a local variable. When that
variable falls out of scope (or is explicitly unset), the callback passed
to the constructor will be invoked. This is useful, for example, to aid
cleanup at the end of a function.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{pk_project}-autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

%{_bindir}/phpab -t fedora -o src/%{pk_project}-autoload.php src
%install
: Library
mkdir -p      %{buildroot}%{_datadir}/php
cp -pr src    %{buildroot}%{_datadir}/php/%{ns_vendor}
%oreon_autofiles main

%check

%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{pk_project}-autoload.php';
class_alias('PHPUnit\\Framework\\TestCase', 'PHPUnit_Framework_TestCase');
EOF
ret=0
for cmd in php php81 php82 php83; do
   if which $cmd; then
      $cmd %{phpunit} \
         --do-not-cache-result \
         --no-coverage \
         --no-configuration \
         . || ret=1
   fi
done
exit $ret
%else
: Test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
