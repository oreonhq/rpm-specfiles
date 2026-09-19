%global source0_hash 8aa47d579d009278ade0e06bb39124500da18b1eb02c2776f58d6a20cc0b8dac

Name:           php-manual-en
Summary:        Documentation for the PHP programming language
Version:        20250109
Release:        4%{?dist}
License:        CC-BY-3.0
URL:            https://www.php.net/download-docs.php
Source0:        https://www.php.net/distributions/manual/php_manual_en.tar.gz
BuildArch:      noarch

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

%files
%license LICENSE
%doc %{_defaultdocdir}/php-manual

%changelog
%autochangelog
