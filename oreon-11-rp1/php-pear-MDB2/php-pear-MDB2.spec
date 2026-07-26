%global source0_hash c4ab3cf8cea4aacff02d729998b0ac80b4f92c2cc8055956079b323a406d985b

%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name MDB2
%global prever    b5

Name:           php-pear-MDB2
Version:        2.5.0
%if 0%{?prever:1}
Release:        0.34.%{?prever}%{?dist}
%else
Release:        29%{?dist}
%endif
Summary:        Database Abstraction Layer

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://pear.php.net/package/MDB2
Source0:        http://pear.php.net/get/%{pear_name}-%{version}%{?prever}.tgz

BuildArch:      noarch
BuildRequires:  php-pear(PEAR) >= 1.9.1

Requires:       php-common >= 5.2.0
Requires:       php-pear(PEAR) >= 1.9.1
# phpci detected required extension
Requires:       php-date
Requires:       php-pcre
Requires:       php-spl
Requires(post): %{__pear}
Requires(postun): %{__pear}

Provides:       php-pear(%{pear_name}) = %{version}%{?prever}

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
# Empty build section, most likely nothing required.

%install
rm -rf $RPM_BUILD_ROOT
cd %{pear_name}-%{version}%{?prever}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml

# Clean up unnecessary files
rm -rf $RPM_BUILD_ROOT%{pear_metadir}/.??*

# Install XML package description
install -d $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}

%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null ||:

%postun
if [ "$1" -eq "0" ]; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null ||:
fi

%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_testdir}/%{pear_name}
%{pear_phpdir}/%{pear_name}
%{pear_phpdir}/MDB2.php

%changelog
%autochangelog
