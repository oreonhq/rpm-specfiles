%global source0_hash d15a62336dff9bf959bc56f3e0ca25e461557943676da03a646a570ef1915b3a
Name:           php-manual-en
Summary:        Documentation for the PHP programming language
Version:        20250109
Release:        1%{?dist}
License:        CC-BY-3.0
URL:            https://www.php.net/download-docs.php
Source0:        https://www.php.net/distributions/manual/php_manual_en.tar.gz
BuildArch:      noarch
# oreon:deps

# /oreon:deps
%description
English-language documentation for the PHP programming language.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%install
mkdir -p %{buildroot}/%{_defaultdocdir}/php-manual/en
cp -pr php-chunked-xhtml %{buildroot}/%{_defaultdocdir}/php-manual/en/html
cat >LICENSE <<EOF
For licensing information please see:
%{_defaultdocdir}/php-manual/en/html/copyright.html
EOF
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
