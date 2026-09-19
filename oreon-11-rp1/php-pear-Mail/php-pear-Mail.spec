%global source0_hash 07002af5e62a81fc1e533887c17a81ed773b73d0234f82437f12c91f797dcffa

# remirepo/fedora spec file for php-pear-Net-SMTP
#
# Copyright (c) 2006-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name Mail

Name:           php-pear-Mail
Version:        2.0.0
Release:        7%{?dist}
Summary:        Class that provides multiple interfaces for sending emails

License:        BSD-3-Clause
URL:            http://pear.php.net/package/Mail
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php-pear(PEAR) >= 1.5.6

Requires:       php(language) >= 5.2.1
Requires:       php-pear(PEAR) >= 1.5.6 
Requires:       php-pear(Net_SMTP) >= 1.4.1
Requires(post): %{__pear}
Requires(postun): %{__pear}

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/mail) = %{version}

%description
PEAR's Mail package defines an interface for implementing mailers under the
PEAR hierarchy.  It also provides supporting functions useful to multiple
mailer backends.  Currently supported backends include: PHP's native
mail() function, sendmail, and SMTP.  This package also provides a RFC822
email address list validation utility class.
 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
mv package.xml %{pear_name}-%{version}/%{name}.xml

%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.

%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}

%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi

%files
%{pear_phpdir}/Mail.php
%{pear_phpdir}/Mail
%{pear_testdir}/Mail
%{pear_xmldir}/%{name}.xml
%{pear_docdir}/%{pear_name}

%changelog
%autochangelog
