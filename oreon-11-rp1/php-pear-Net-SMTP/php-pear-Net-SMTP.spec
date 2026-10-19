%global source0_hash 1512ee9574be5229c13b4ac19a2b33cf0d15acd84f0e31aad43ebfda23f0b48f
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name Net_SMTP
Name:           php-pear-Net-SMTP
Version:        1.12.2
Release:        1%{?dist}
Summary:        Provides an implementation of the SMTP protocol
License:        BSD-2-Clause
URL:            http://pear.php.net/package/Net_SMTP
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz
BuildArch:      noarch
Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php(language) >= 5.4
Requires:       php-pear(PEAR) >= 1.10.1
Requires:       php-pear(Net_Socket)
Requires:       php-pear(Auth_SASL)
Requires:       php-openssl
%if 0%{?fedora} >= 29 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
Recommends:     php-krb5
%endif
Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/net_smtp) = %{version}
# oreon:deps
BuildRequires:  php-pear
# /oreon:deps
%description
Provides an implementation of the SMTP protocol using PEAR's Net_Socket class.

php-pear-Net-SMTP can optionally use package "php-pear-Auth-SASL".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
cd %{pear_name}-%{version}
# package.xml is V2
mv ../package.xml %{name}.xml

%build

cd %{pear_name}-%{version}
%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml
rm -rf %{buildroot}%{pear_metadir}/.??*
install -Dpm 644 %{name}.xml %{buildroot}%{pear_xmldir}/%{name}.xml
%oreon_autofiles main

%check

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
