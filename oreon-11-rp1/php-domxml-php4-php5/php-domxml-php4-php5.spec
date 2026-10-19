%global source0_hash f98f3b5b7d8a419cd43cf157ab5072172759f9c451f289a87d445cc23179343f
%global libname domxml-php4-php5
Name:           php-%{libname}
Version:        1.21.2
Release:        1%{?dist}
Summary:        XML transition from PHP4 domxml to PHP5 dom module
Summary(fr):    Transition du XML de PHP4 domxml à PHP5 dom
License:        LGPL-3.0-or-later
URL:            http://alexandre.alapetite.fr/doc-alex/domxml-php4-php5/
Source0:        %{libname}-%{version}.tar.gz
BuildArch:      noarch
Requires:       php-xml >= 5.1
# oreon:deps

# /oreon:deps
%description
XML transition from PHP4 domxml to PHP5 dom module.

%description -l fr
Transition du XML de PHP4 domxml à PHP5 dom.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc

%{__sed} -i -e 's/\r//' *.php

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_datadir}/php/%{libname}
%{__install} -pm 0644 *.php $RPM_BUILD_ROOT%{_datadir}/php/%{libname}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
