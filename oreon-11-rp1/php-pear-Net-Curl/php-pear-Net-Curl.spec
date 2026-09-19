%global source0_hash 97185c4c0e138091228a3ef97c9e26986e4e09dd8008a54acd8ae1f6311b3040

%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name Net_Curl

Name:           php-pear-Net-Curl
Version:        1.2.5
Release:        35%{?dist}
Summary:        OO interface to PHP's cURL extension

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://pear.php.net/package/Net_Curl
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php-pear
Requires:       php-pear(PEAR)
Requires(post): %{__pear}
Requires(postun): %{__pear}
Provides:       php-pear(%{pear_name}) = %{version}

%description
Provides an Object-Oriented interface to PHP's curl extension.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc
cd %{pear_name}-%{version}
# Package is V2
mv ../package.xml %{name}.xml

%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.

%install
rm -rf $RPM_BUILD_ROOT
cd %{pear_name}-%{version}
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
%{pear_phpdir}/Net
%{pear_phpdir}/Net/Curl.php

%changelog
%autochangelog
