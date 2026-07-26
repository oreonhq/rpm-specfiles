%global source0_hash 32c6bf1bffdb1101f17498eea557f2aa2a6a3358bd49357618583c3e4207027a

# spec file for php-pear-Console-Getargs
#
# Copyright (c) 2006-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name Console_Getargs

Name:           php-pear-Console-Getargs
Version:        1.4.0
Release:        19%{?dist}
Summary:        Command-line arguments and parameters parser

License:        PHP-3.01
URL:            http://pear.php.net/package/Console_Getargs
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

Patch0:         %{pear_name}-php8.patch
Patch1:         %{pear_name}-tests.patch

BuildArch:      noarch
BuildRequires:  php-pear
# For test suite
BuildRequires:  phpunit9

Requires:       php-pear(PEAR)
Requires(post): %{__pear}
Requires(postun): %{__pear}

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/console_getargs) = %{version}

%description
The Console_Getargs package implements a Command Line arguments and
parameters parser for your CLI applications. It performs some basic
arguments validation and automatically creates a formatted help text,
based on the given configuration.
 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c -q
cd %{pear_name}-%{version}
%patch -P0 -p1
%patch -P1 -p0

# package.xml is V2
sed -e '/README/s/role="data"/role="doc"/' \
    -e 's/md5sum.*name/name/' \
    ../package.xml >%{name}.xml

%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.

%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml

# Clean up unnecessary files
rm -rf $RPM_BUILD_ROOT%{pear_metadir}/.??*

# Install XML package description
mkdir -p $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}

%check
cd %{pear_name}-%{version}
%{_bindir}/phpunit9 \
   --do-not-cache-result \
   --include-path=$RPM_BUILD_ROOT%{pear_phpdir} \
   tests

%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi

%files
%doc %{pear_docdir}/%{pear_name}
%doc %{pear_testdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/Console/Getargs.php

%changelog
%autochangelog
