%global source0_hash e96ca277544e9dc35b3b4bf35802765c9afd2820cb786fd4346bd854268dabdf

%{!?__pear: %global __pear %{_bindir}/pear}
%global pear_name  Net_IDNA2

%global with_tests 0%{!?_without_tests:1}

%if 0%{?fedora} > 38 || 0%{?epel}
%global with_tests 0
%endif

Summary:         PHP library for punycode encoding and decoding
Name:            php-pear-Net-IDNA2
Version:         0.2.0
Release:         25%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:         LicenseRef-Callaway-LGPLv2+
URL:             http://pear.php.net/package/Net_IDNA2/
Source0:         http://download.pear.php.net/package/Net_IDNA2-%{version}.tgz
Patch0:          Net_IDNA2-php8.patch
BuildArch:       noarch
BuildRequires:   php(language) >= 5.4
BuildRequires:   php-pear(PEAR) >= 1.10.1
%if %{with_tests}
BuildRequires:   phpunit
%endif
Requires:        php(language) >= 5.4
Requires:        php-pear(PEAR) >= 1.10.1
Requires(post):  %{__pear}
Requires(postun): %{__pear}
Provides:        php-pear(%{pear_name}) = %{version}
%description
This package helps you to encode and decode punycode strings easily in
PHP.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
cd %{pear_name}-%{version}
%autopatch -p1
sed -e "s/md5sum=.*name/name/" ../package.xml >%{name}.xml

%build
# Nothing to build

%install
pushd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
install -D -p -m 0644 %{name}.xml %{buildroot}%{pear_xmldir}/%{name}.xml

%if %{with_tests}
%check
cd %{pear_name}-%{version}%{?prever}
%{_bindir}/phpunit \
   --include-path %{buildroot}%{pear_phpdir} \
   --verbose tests
%endif

%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null ||:

%postun
if [ "$1" -eq "0" ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null ||:
fi

%files
%dir %{pear_phpdir}/Net/
%{pear_phpdir}/Net/IDNA2
%{pear_phpdir}/Net/IDNA2.php
%{pear_testdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml

%changelog
%autochangelog
