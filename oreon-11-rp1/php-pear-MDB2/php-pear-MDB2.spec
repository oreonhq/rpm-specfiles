%global source0_hash 385a2c9c2341fc8c37f9de165c7137d2f13dcfe3b89a57290f6cb8e38ded2871
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name MDB2
%global prever    b5
Name:           php-pear-MDB2
Version:        2.5.0
%if 0%{?prever:1}
Release:        1%{?dist}
%else
Release:        1%{?dist}
%endif
Summary:        Database Abstraction Layer
License:        LicenseRef-Callaway-BSD
URL:            http://pear.php.net/package/MDB2
Source0:        http://pear.php.net/get/%{pear_name}-%{version}%{prever}.tgz
BuildArch:      noarch
Requires:       php-common >= 5.2.0
Requires:       php-pear(PEAR) >= 1.9.1
Requires:       php-date
Requires:       php-pcre
Requires:       php-spl
Requires(post): %{__pear}
Requires(postun): %{__pear}
Provides:       php-pear(%{pear_name}) = %{version}%{?prever}
# oreon:deps
BuildRequires:  php-pear(PEAR)
# /oreon:deps
%description
PEAR::MDB2 is a merge of the PEAR::DB and Metabase php database abstraction
layers.

It provides a common API for all supported RDBMS. The main difference to most
other DB abstraction packages is that MDB2 goes much further to ensure
portability.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc
cd %{pear_name}-%{version}%{?prever}
# package.xml is V2
sed -e '/LICENSE/s/role="data"/role="doc"/' <../package.xml >%{name}.xml

%build

cd %{pear_name}-%{version}%{?prever}
%install
rm -rf $RPM_BUILD_ROOT
cd %{pear_name}-%{version}%{?prever}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml
rm -rf $RPM_BUILD_ROOT%{pear_metadir}/.??*
install -d $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}
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
