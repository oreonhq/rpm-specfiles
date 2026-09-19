%global source0_hash f98f3b5b7d8a419cd43cf157ab5072172759f9c451f289a87d445cc23179343f

%global libname domxml-php4-php5

Name:           php-%{libname}
Version:        1.21.2
Release:        30%{?dist}
Summary:        XML transition from PHP4 domxml to PHP5 dom module
Summary(fr):    Transition du XML de PHP4 domxml à PHP5 dom

License:        LGPL-3.0-or-later
URL:            http://alexandre.alapetite.fr/doc-alex/domxml-php4-php5/
# wget -N http://alexandre.alapetite.fr/doc-alex/domxml-php4-php5/domxml-php4-to-php5.php.txt -O domxml-php4-to-php5.php
# grep Version domxml-php4-to-php5.php
# tar czf domxml-php4-php5-1.21.2.tar.gz domxml-php4-to-php5.php
Source0:        %{libname}-%{version}.tar.gz
BuildArch:      noarch

Requires:       php-xml >= 5.1

%description
XML transition from PHP4 domxml to PHP5 dom module.

%description -l fr
Transition du XML de PHP4 domxml à PHP5 dom.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc

%{__sed} -i -e 's/\r//' *.php

%build
# nothing to build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_datadir}/php/%{libname}
%{__install} -pm 0644 *.php $RPM_BUILD_ROOT%{_datadir}/php/%{libname}

%files
%{_datadir}/php/%{libname}

%changelog
%autochangelog
