%global source0_hash e7cf927c583cdb5f7a2fd5f5d850fa8117fa1e4b62c2a6c62f557fdf877d6e6c
%global gh_commit    5024d623c1a057dcd2d076d25b7d270a1d0d55f3
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     michelf
%global gh_project   php-markdown
Name:        php-markdown
Version:     2.0.0
Release:        1%{?dist}
Summary:        Markdown implementation in PHP
License:     BSD-3-Clause
URL:         https://michelf.ca/projects/php-markdown/
Source0:        https://github.com/michelf/php-markdown/archive/%{version}/%{name}-%{version}.tar.gz
Source1:     makesrc.sh
BuildArch:   noarch
Requires:    php(language) >= 7.4
Requires:    php-pcre
Requires:    php-composer(fedora/autoloader)
Provides:    php-composer(michelf/php-markdown) = %{version}
# oreon:deps
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit10
# /oreon:deps
%description
This is a PHP implementation of John Gruber's Markdown.
It is almost completely compliant with the reference implementation.

Autoloader: %{_datadir}/php/Michelf/markdown-autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
mv License.md LICENSE

%build

: Generate simple autoloader
%{_bindir}/phpab \
    --template fedora \
    --output Michelf/markdown-autoload.php \
    Michelf
cat Michelf/markdown-autoload.php
%install
install -d %{buildroot}%{_datadir}/php/
cp -pr Michelf %{buildroot}%{_datadir}/php/Michelf
%oreon_autofiles main

%check

php -r '
require_once "%{buildroot}%{_datadir}/php/Michelf/markdown-autoload.php";
  $ver = Michelf\Markdown::MARKDOWNLIB_VERSION;
  echo "Version=$ver, expected=%{version}\n";
  return (version_compare($ver, "%{version}", "=") ? 0 : 1);
'
cat << 'EOF' | tee bs.php
<?php
require "%{buildroot}%{_datadir}/php/Michelf/markdown-autoload.php";
require "test/bootstrap.php";
EOF
ret=0
for php in php php74 php81 php82 php83
do
  if which $php
  then
    $php %{_bindir}/phpunit10 --bootstrap bs.php || ret=1
  fi
done
exit $ret
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
