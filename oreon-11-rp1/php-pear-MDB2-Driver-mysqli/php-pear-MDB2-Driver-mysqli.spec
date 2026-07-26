%global source0_hash d5d4d24a1b263f32686d257a5563797460e589311f3c571094b35f1c87fbbaf5

%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name MDB2_Driver_mysqli
%global prever    b4

Name:           php-pear-MDB2-Driver-mysqli
Version:        1.5.0
%if 0%{?prever:1}
Release:        0.33.%{prever}%{?dist}
%else
Release:        26%{?dist}
%endif
Summary:        MySQL Improved MDB2 driver

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://pear.php.net/package/MDB2_Driver_mysqli
Source0:        http://pear.php.net/get/%{pear_name}-%{version}%{?prever}.tgz

BuildArch:      noarch
BuildRequires:  php-pear(PEAR) >= 1.9.1

Requires:       php-common >= 5.2.0
Requires:       php-mysqli
Requires:       php-pcre
Requires:       php-pear(PEAR)
Requires:       php-pear(MDB2) >= 2.5.0%{?prever}
Requires(post): %{__pear}
Requires(postun): %{__pear}
Provides:       php-pear(%{pear_name}) = %{version}%{?prever}

%description
This is the MySQL Improved MDB2 driver.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc
cd %{pear_name}-%{version}%{?prever}
# package.xml is V2
mv ../package.xml %{name}.xml

%build
cd %{pear_name}-%{version}%{?prever}
# Empty build section, most likely nothing required.

%install
rm -rf $RPM_BUILD_ROOT docdir
cd %{pear_name}-%{version}%{?prever}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml

# Clean up unnecessary files
rm -rf $RPM_BUILD_ROOT%{pear_metadir}/.??*

# Install XML package description
install -d $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}

%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi

%files
%{pear_xmldir}/%{name}.xml
%{pear_testdir}/%{pear_name}
%{pear_phpdir}/MDB2/Driver/*/mysqli.php
%{pear_phpdir}/MDB2/Driver/mysqli.php
# packager stuff, not need, could probably be removed
%{pear_datadir}/%{pear_name}

%changelog
%autochangelog
