%global source0_hash 2bb51441f83950d7c2cf0748cf4f36d9506aa2c4df54e56ed289219a6a46c673
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name XML_SVG
Name:           php-pear-XML-SVG
Version:        1.1.0
Release:        28%{?dist}
Summary:        API for building SVG documents
License:        LGPL-3.0-only
URL:            http://pear.php.net/package/%{pear_name}
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz
BuildArch:      noarch
Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php-pear(PEAR)
Provides:       php-pear(%{pear_name}) = %{version}
# oreon:deps
BuildRequires:  php-pear(PEAR)
# /oreon:deps
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
%install
rm -rf %{buildroot}
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml
rm -rf %{buildroot}%{pear_metadir}/.??*
install -Dpm 644 %{name}.xml %{buildroot}%{pear_xmldir}/%{name}.xml
%oreon_autofiles main

%post

%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :
%postun

if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        pear.php.net/%{pear_name} >/dev/null || :
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
