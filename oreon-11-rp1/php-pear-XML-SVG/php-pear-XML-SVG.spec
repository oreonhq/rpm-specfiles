%global source0_hash 50f48e23b784a83e3ebfe6f07749067523101c4d74d51745532d6387702b5c1a

%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name XML_SVG

Name:           php-pear-XML-SVG
Version:        1.1.0
Release:        28%{?dist}
Summary:        API for building SVG documents

# https://pear.php.net/bugs/19690 - Please Provides LICENSE file
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            http://pear.php.net/package/%{pear_name}
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php-pear(PEAR)

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php-pear(PEAR)

Provides:       php-pear(%{pear_name}) = %{version}

%description
This package provides an object-oriented API for building SVG documents.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
cd %{pear_name}-%{version}

# https://pear.php.net/bugs/19718 - README is Doc
sed -e '/README/s/role="data"/role="doc"/' \
    ../package.xml >%{name}.xml

%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.

%install
rm -rf %{buildroot}

cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
install -Dpm 644 %{name}.xml %{buildroot}%{pear_xmldir}/%{name}.xml

%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        pear.php.net/%{pear_name} >/dev/null || :
fi

%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%dir %{pear_phpdir}/XML
%{pear_phpdir}/XML/SVG.php
%{pear_phpdir}/XML/SVG

%changelog
%autochangelog
