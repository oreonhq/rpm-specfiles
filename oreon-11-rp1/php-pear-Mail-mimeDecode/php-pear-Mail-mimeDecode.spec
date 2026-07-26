%global source0_hash 8323344fb2e3266339675adee6b373dcb9a41c730f34f4141ffe891f2c9818f7

%{!?__pear: %global __pear %{_bindir}/pear}

%global pear_name Mail_mimeDecode
Name:           php-pear-Mail-mimeDecode
Version:        1.5.6
Release:        23%{?dist}
Summary:        Class to decode mime messages

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://pear.php.net/package/Mail_mimeDecode
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

Patch0:         %{pear_name}-php8.patch

BuildArch:      noarch
BuildRequires:  php-pear >= 1:1.6.0
# BR for tests
BuildRequires:  php-pear(Mail_Mime) > 1.4.0

Requires:       php-pear(PEAR) >= 1.6.0
Requires:       php-pear(Mail_Mime) > 1.4.0
Requires(post): %{__pear}
Requires(postun): %{__pear}
Provides:       php-pear(%{pear_name}) = %{version}

%description
Provides a class to deal with the decoding and interpreting of mime messages.
This package used to be part of the Mail_Mime package, but has been split off.

To run post-installation tests, execute:
pear run-tests -p Mail_mimeDecode

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
cd %{pear_name}-%{version}
%patch -P0 -p1

# Package.xml is V2
sed -e '/mimeDecode/s/md5sum.*name/name/'  ../package.xml >%{name}.xml

# Empty build section, nothing required
%build

%install
rm -rf %{buildroot} docdir

cd %{pear_name}-%{version}
%{__pear} install \
   --nodeps \
   --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}

%check
cd %{pear_name}-%{version}

# Test suite
pear run-tests \
   -i "-d include_path=%{buildroot}%{pear_phpdir}:%{pear_phpdir}" \
   tests | tee ../tests.log
if grep "FAILED TESTS" ../tests.log
then
  for fic in tests/*diff
  do
    cat $fic
    :
  done
  exit 1
fi

%post
%{__pear} install --nodeps --soft --force --register-only %{pear_xmldir}/%{name}.xml >/dev/null ||:

%postun
# if refcount = 0 then package has been removed (not upgraded)
if [ "$1" -eq "0" ]; then
 %{__pear} uninstall --nodeps --ignore-errors --register-only %{pear_name} >/dev/null ||:
fi

%files
%{pear_xmldir}/%{name}.xml
%{pear_testdir}/%{pear_name}
%{pear_datadir}/%{pear_name}
%{pear_phpdir}/Mail/mimeDecode.php

%changelog
%autochangelog
