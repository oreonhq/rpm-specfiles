%global source0_hash 1512ee9574be5229c13b4ac19a2b33cf0d15acd84f0e31aad43ebfda23f0b48f

# remirepo/fedora spec file for php-pear-Net-SMTP
#
# SPDX-FileCopyrightText:  Copyright 2006-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name Net_SMTP

Name:           php-pear-Net-SMTP
Version:        1.12.2
Release:        2%{?dist}
Summary:        Provides an implementation of the SMTP protocol

License:        BSD-2-Clause
URL:            http://pear.php.net/package/Net_SMTP
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php-pear

Requires(post): %{__pear}
Requires(postun): %{__pear}
# From package.xml
Requires:       php(language) >= 5.4
Requires:       php-pear(PEAR) >= 1.10.1
Requires:       php-pear(Net_Socket)
Requires:       php-pear(Auth_SASL)
# From phpcompatinfo report for version 1.9.0
Requires:       php-openssl
# Optional
%if 0%{?fedora} >= 29 || 0%{?rhel} >= 8
Recommends:     php-krb5
%endif

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/net_smtp) = %{version}

%description
Provides an implementation of the SMTP protocol using PEAR's Net_Socket class.

php-pear-Net-SMTP can optionally use package "php-pear-Auth-SASL".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
cd %{pear_name}-%{version}
# package.xml is V2
mv ../package.xml %{name}.xml

%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.

%install
cd %{pear_name}-%{version}

%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
install -Dpm 644 %{name}.xml %{buildroot}%{pear_xmldir}/%{name}.xml

%check
# For documentation purpose only
# After install, as root :
# cd /usr/share/tests/pear/Net_SMTP/tests/
# cp config.php.dist config.php
# vi config.php # you should use a working mail account
# pear run-tests -p Net_SMTP
# Should return 
# 3 PASSED TESTS
# 0 SKIPPED TESTS

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
%{pear_phpdir}/Net/*
%{pear_testdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml

%changelog
%autochangelog
