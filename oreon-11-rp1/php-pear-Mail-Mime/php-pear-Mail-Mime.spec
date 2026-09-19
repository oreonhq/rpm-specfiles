%global source0_hash da4add41ae3fa5e8444962f6d88690e5001ebd3000abfb792c85a0e418dc82d5

# spec file for php-pear-Mail-Mime
#
# Copyright (c) 2009-2024 Remi Collet
# Copyright (c) 2006-2008 Brandon Holbrook
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name Mail_Mime

Name:           php-pear-Mail-Mime
Version:        1.10.12
Release:        5%{?dist}
Summary:        Classes to create MIME messages

License:        BSD-3-Clause
URL:            http://pear.php.net/package/Mail_Mime
Source0:        http://pear.php.net/get/Mail_Mime-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php-pear(PEAR) >= 1.6.0
BuildRequires:  php-mbstring

Requires:       php-pear(PEAR) >= 1.6.0
Requires:       php-date
Requires:       php-mbstring
Requires:       php-pcre
Requires(post): %{__pear}
Requires(postun): %{__pear}

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/mail_mime) = %{version}

%description
Mail_Mime provides classes to deal with the creation and manipulation 
of MIME messages. It allows people to create e-mail messages consisting of:
* Text Parts
* HTML Parts
* Inline HTML Images
* Attachments
* Attached messages

It supports big messages, base64 and quoted-printable encoding and
non-ASCII characters in file names, subjects, recipients, etc. encoded
using RFC2047 and/or RFC2231.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c 
cd %{pear_name}-%{version}
mv ../package.xml %{name}.xml

%build
# Empty build section, nothing required

%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}

%check
cd %{pear_name}-%{version}
%{__pear} \
   run-tests \
   -i "-d include_path=%{buildroot}%{pear_phpdir}:%{pear_phpdir}" \
   tests | tee ../tests.log
grep "FAILED TESTS" ../tests.log && exit 1
exit 0

%post
%{__pear} install --nodeps --soft --force --register-only %{pear_xmldir}/%{name}.xml >/dev/null ||:

%postun
# if refcount = 0 then package has been removed (not upgraded)
if [ "$1" -eq "0" ]; then
   %{__pear} uninstall --nodeps --ignore-errors --register-only %{pear_name} >/dev/null ||:
fi

%files
%doc %{pear_testdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/Mail

%changelog
%autochangelog
