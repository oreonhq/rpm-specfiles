%global source0_hash 136ac4f35140aab0a632fb108b508040d60f566a726f6b547e09d4ecd005809a
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name MDB2_Driver_pgsql
%global prever    b4
Name:           php-pear-MDB2-Driver-pgsql
Version:        1.5.0
%if 0%{?prever:1}
Release:        1%{?dist}
%else
Release:        1%{?dist}
%endif
Summary:        PostgreSQL MDB2 driver
License:        LicenseRef-Callaway-BSD
URL:            http://pear.php.net/package/MDB2_Driver_pgsql
Source0:        http://pear.php.net/get/%{pear_name}-%{version}%{prever}.tgz
BuildArch:      noarch
Requires:       php-common >= 5.2.0
Requires:       php-pcre
Requires:       php-pgsql
Requires:       php-pear(PEAR) >= 1.9.1
Requires:       php-pear(MDB2) >= 2.5.0%{?prever}
Requires(post): %{__pear}
Requires(postun): %{__pear}
Provides:       php-pear(%{pear_name}) = %{version}%{?prever}
# oreon:deps
BuildRequires:  php-pear(PEAR)
# /oreon:deps
%description
This is the PostgreSQL MDB2 driver.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc
cd %{pear_name}-%{version}%{?prever}
# package.xml is V2
mv ../package.xml %{name}.xml

%build

cd %{pear_name}-%{version}%{?prever}
%install
rm -rf $RPM_BUILD_ROOT docdir
cd %{pear_name}-%{version}%{?prever}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml
rm -rf $RPM_BUILD_ROOT%{pear_metadir}/.??*
install -d $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}
%oreon_autofiles main

%post

%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :
%postun

if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
