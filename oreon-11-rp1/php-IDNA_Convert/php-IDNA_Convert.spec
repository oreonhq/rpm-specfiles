%global source0_hash 77e269773835429dd8366af8ba411fe44223a77d5e7ea9180e06762a42c8efcc

Name:		php-IDNA_Convert
Version:	4.2.1
Release:	2%{?dist}
Summary:	Provides conversion of internationalized strings to UTF8

License:	LGPL-2.1-or-later
URL:		https://github.com/algo26-matthias/idna-convert
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

Requires:	php-iconv
Requires:	php-mbstring
Requires:	php-pcre
Requires:	php-spl
Requires:	php-xml

%description
This converter allows you to transfer domain names between the encoded 
(Punycode) notation and the decoded (UTF-8) notation. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc

%build
#empty build string to placate rpmlint

%install
%{__mkdir} -p %{buildroot}/%{_datadir}/php/IDNA_Convert
cp -a idna-convert-%{version}/src/* %{buildroot}/%{_datadir}/php/IDNA_Convert/

%files
%{_datadir}/php/IDNA_Convert/
%license idna-convert-%{version}/LICENSE
%doc idna-convert-%{version}/README.md

%changelog
%autochangelog
