%global source0_hash acfdeb2a8147a7a82766d1e2fa9cf6b43bd80ef6e86696012ab87332bb6cc8cb
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name Date
Name:           php-pear-Date
Version:        1.4.7
Release:        1%{?dist}
Summary:        Date and Time Zone Classes
License:        LicenseRef-Callaway-BSD
URL:            http://pear.php.net/package/Date
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz
BuildArch:      noarch
Requires:       php-pear(PEAR)
Requires(post): %{__pear}
Requires(postun): %{__pear}
Provides:       php-pear(%{pear_name}) = %{version}
# oreon:deps
BuildRequires:  php-pear
# /oreon:deps
%description
Generic classes for representation and manipulation of dates, times and time
zones without the need of timestamps, which is a huge limitation for php
programs. Includes time zone data, time zone conversions and many date/time
conversions.  It does not rely on 32-bit system date stamps, so you can display
calendars and compare dates that date pre 1970 and post 2038. This package also
provides a class to convert date strings between Gregorian and Human calendar
formats.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc
cd %{pear_name}-%{version}
# Package is V2
mv ../package.xml %{name}.xml

%build

cd %{pear_name}-%{version}
%install
rm -rf $RPM_BUILD_ROOT
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml
rm -rf $RPM_BUILD_ROOT%{pear_metadir}/.??*
install -d $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}
sed -i 's/\r//' $RPM_BUILD_ROOT%{pear_docdir}/%{pear_name}/docs/TODO
%oreon_autofiles main

%post

%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null ||:
%postun

if [ "$1" -eq "0" ]; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null ||:
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
