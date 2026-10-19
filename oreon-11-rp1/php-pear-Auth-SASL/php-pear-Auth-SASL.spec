%global source0_hash 6efa4c01031d8e04dfde91988f2694b3505c24337046725f590cc1a89a30d254
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name Auth_SASL
Summary:        Abstraction of various SASL mechanism responses
Name:        php-pear-Auth-SASL
Version:     1.2.0
Release:        1%{?dist}
License:     BSD-3-Clause
URL:         http://pear.php.net/package/Auth_SASL
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz
BuildArch:        noarch
Requires:         php(language) >= 5.4
Requires:         php-pear(PEAR) >= 1.10.1
Requires:         php-pcre
Requires(post):   %{__pear}
Requires(postun): %{__pear}
Provides:         php-pear(%{pear_name}) = %{version}
Provides:         php-composer(pear/auth_sasl) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-pear
# /oreon:deps
%description
Provides code to generate responses to common SASL mechanisms, including:
o Digest-MD5
o CramMD5
o Plain
o Anonymous
o Login (Pseudo mechanism)

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c -q
mv package.xml %{pear_name}-%{version}/%{name}.xml

%build

%install
rm -rf %{buildroot}
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml
rm -rf %{buildroot}%{pear_metadir}/.??*
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}
%oreon_autofiles main

%post

%{__pear} install --nodeps --soft --force --register-only %{pear_xmldir}/%{name}.xml >/dev/null || :
%postun

if [ "$1" -eq "0" ]; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only  %{pear_name} >/dev/null || :
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
