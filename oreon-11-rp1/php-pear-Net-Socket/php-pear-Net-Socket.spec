%global source0_hash 1f971cf0f80fa6a7bbbebb8695917293eaede976680718413847177633a41689

# fedora/remirepo spec file for php-pear-Net-Socket
#
# Copyright (c) 2006-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%{!?__pear: %global __pear %{_bindir}/pear}
%global pear_name Net_Socket

Name:           php-pear-Net-Socket
Version:        1.2.2
Release:        21%{?dist}
Summary:        Network Socket Interface

License:        BSD-2-Clause
URL:            http://pear.php.net/package/Net_Socket
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php(language) >= 5.4
BuildRequires:  php-pear >= 1:1.10.1

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php(language) >= 5.4
Requires:       php-pear(PEAR) >= 1.10.1
Requires:       php-date

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/net_socket) = %{version}

%description
Net_Socket is a class interface to TCP sockets.  It provides blocking
and non-blocking operation, with different reading and writing modes
(byte-wise, block-wise, line-wise and special formats like network
byte-order ip addresses).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
cd %{pear_name}-%{version}
# package.xml is V2
mv ../package.xml %{name}.xml

%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.

%install
cd Net_Socket-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}

%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi

%files
%{pear_phpdir}/Net
%{pear_xmldir}/%{name}.xml
%{pear_docdir}/%{pear_name}

%changelog
%autochangelog
