%global source0_hash 1b590bdd6d8e8743b9d0e580d7d36e9e6e2769c3682ae17721d7e78199f90638

# spec file for php-pear-Net-IMAP
#
# Copyright (c) 2013-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#
%{!?__pear:       %global __pear       %{_bindir}/pear}
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}

%global pear_channel pear.php.net
%global pear_name    Net_IMAP

# Cannot run test suite which requires a valid IMAP account

Name:           php-pear-Net-IMAP
Version:        1.1.4
Release:        5%{?dist}
Summary:        Provides an implementation of the IMAP protocol

License:        PHP-3.01
URL:            http://%{pear_channel}/package/%{pear_name}
Source0:        http://%{pear_channel}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php-pear(PEAR)

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php-date
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-pear(PEAR)
Requires:       php-pear(Net_Socket) >= 1.0.8
# Optional
Requires:       php-pear(Auth_SASL) >= 1.0.2

Provides:       php-pear(%{pear_name}) = %{version}

%description
Provides an implementation of the IMAP4Rev1 protocol using PEAR's
Net_Socket and the optional Auth_SASL class.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

cd %{pear_name}-%{version}
cp ../package.xml %{name}.xml

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
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}

%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_channel}/%{pear_name} >/dev/null || :
fi

%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/Net/IMAP*
%{pear_testdir}/%{pear_name}
%{pear_datadir}/%{pear_name}

%changelog
%autochangelog
