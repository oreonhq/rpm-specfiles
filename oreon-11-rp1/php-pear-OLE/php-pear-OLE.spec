%global source0_hash a0f3ad85845801ad8f7c6cf1695e048c960a72b183946613ddbca4567fed9164

%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name OLE
%global prever    RC2

Name:           php-pear-OLE
Version:        1.0.0
Release:        0.34.%{prever}%{?dist}
Summary:        Package for reading and writing OLE containers

# Automatically converted from old format: PHP - review is highly recommended.
License:        PHP-3.01
URL:            http://pear.php.net/package/OLE
Source0:        http://pear.php.net/get/%{pear_name}-%{version}%{?prever}.tgz

BuildArch:      noarch
BuildRequires:  php-pear

Requires(post): %{__pear}
Requires(postun): %{__pear}
# from phpcompatinfo report
Requires:       php-pear(PEAR)
Requires:       php-date

Provides:       php-pear(%{pear_name}) = %{version}

%description
This package allows reading and writing of OLE (Object Linking and
Embedding) compound documents. This format is used as container for Excel
(.xls), Word (.doc) and other Microsoft file formats.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
cd %{pear_name}-%{version}%{?prever}
mv ../package.xml %{name}.xml

%build
cd %{pear_name}-%{version}%{?prever}
# Empty build section, most likely nothing required.

%install
cd %{pear_name}-%{version}%{?prever}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml

# Clean up unnecessary files
rm -rf $RPM_BUILD_ROOT%{pear_metadir}/.??*

# Install XML package description
mkdir -p $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}

%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        pear.php.net/%{pear_name} >/dev/null || :
fi

%files
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/OLE
%{pear_phpdir}/OLE.php

%changelog
%autochangelog
