%global source0_hash 03d5c68fb5be3782fc27d7f6249b2d532cf9129620d08c57eba7c8f668563e6d
%global gh_commit    b5f37dbff9a8ad360ca341f3240dc1c168b45447
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     felixfbecker
%global gh_project   php-advanced-json-rpc
%global pk_vendor    %{gh_owner}
%global pk_project   advanced-json-rpc
%global ns_vendor    %nil
%global ns_project   AdvancedJsonRpc
%global major        3
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.2.1
Release:        1%{?dist}
Summary:        A more advanced JSONRPC implementation
License:        ISC
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with_tests}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
%else
%endif
%endif
Requires:       php(language) >= 7.1
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
Requires:       (php-composer(netresearch/jsonmapper)            >= 1.0    with php-composer(netresearch/jsonmapper)            <  5)
Requires:       (php-composer(phpdocumentor/reflection-docblock) >= 4.3.4  with php-composer(phpdocumentor/reflection-docblock) <  6)
%else
Requires:       php-netresearch-jsonmapper
Requires:       php-phpdocumentor-reflection-docblock4
%endif
Requires:       php-reflection
Requires:       php-json
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(netresearch/jsonmapper) >= 1.0 with php-composer(netresearch/jsonmapper) < 5)
BuildRequires:  (php-composer(phpdocumentor/reflection-docblock) >= 4.3.4 with php-composer(phpdocumentor/reflection-docblock) < 6)
BuildRequires:  php(language)
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  php-json
BuildRequires:  php-reflection
BuildRequires:  phpunit8
# /oreon:deps
%description
Advanced JSONRPC

Provides basic classes for requests and responses in JSONRPC and a
Dispatcher class that can decode a JSONRPC request and call appropiate
methods on a target, coercing types of parameters by type-hints and
@param tags.

Supports nested targets:
If the method is something like myNestedTarget->theMethod, the dispatcher
will look for a myNestedTarget property on the target and call theMethod
on it.

The delimiter is configurable and defaults to the PHP object operator ->.

Autoloader: %{php_home}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

cat << 'EOF' | tee lib/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '/usr/share/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_project}\\', __DIR__);
\Fedora\Autoloader\Dependencies::required([
    [
        '%{php_home}/phpDocumentor/Reflection/DocBlock5/autoload.php',
        '%{php_home}/phpDocumentor/Reflection/DocBlock4/autoload.php',
    ],
    '%{php_home}/netresearch/jsonmapper/autoload.php',
]);
EOF

%build

%install
: Library
mkdir -p    %{buildroot}%{php_home}
cp -pr lib  %{buildroot}%{php_home}/%{ns_project}%{major}
%oreon_autofiles main

%check

%if %{with_tests}
cat << 'EOF' | tee bootstrap.php
<?php
require '%{buildroot}%{php_home}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_project}\\Tests\\', __DIR__ . '/tests');
EOF
ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit8 \
      --do-not-cache-result \
      --no-coverage \
      --bootstrap bootstrap.php \
      --verbose tests || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
