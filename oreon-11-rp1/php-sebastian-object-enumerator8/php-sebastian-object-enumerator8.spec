%global source0_hash 745bde2fb18354da301937e99ca791ea4942bb40e432d15ba3c112a35433f943
%bcond_with          tests
%global gh_commit    b39ab125fd9a7434b0ecbc4202eebce11a98cfc5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   object-enumerator
%global gh_date      2026-02-06
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global ns_vendor    SebastianBergmann
%global ns_project   ObjectEnumerator
%global major        8
%global php_home     %{_datadir}/php
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        8.0.0
Release:        1%{?dist}
Summary:        Traverses array and object to enumerate all referenced objects, version 8
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 8.3
Requires:       (php-composer(%{pk_vendor}/object-reflector) >= 6.0   with php-composer(%{pk_vendor}/object-reflector) < 7)
Requires:       (php-composer(sebastian/recursion-context)   >= 8.0   with php-composer(sebastian/recursion-context)   < 9)
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(sebastian/object-reflector) >= 6.0 with php-composer(sebastian/object-reflector) < 7)
BuildRequires:  (php-composer(sebastian/recursion-context) >= 8.0 with php-composer(sebastian/recursion-context) < 9)
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit13
# /oreon:deps
%description
Traverses array structures and object graphs to enumerate all
referenced objects.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

%{_bindir}/phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{ns_vendor}/ObjectReflector6/autoload.php',
    '%{php_home}/%{ns_vendor}/RecursionContext8/autoload.php',
]);
EOF
%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main

%check

%if %{with tests}
mkdir vendor
%{_bindir}/phpab --template fedora --output vendor/autoload.php tests/_fixture
: Run upstream test suite
ret=0
for cmd in php php84 php85; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     %{_bindir}/phpunit13 --bootstrap vendor/autoload.php || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
