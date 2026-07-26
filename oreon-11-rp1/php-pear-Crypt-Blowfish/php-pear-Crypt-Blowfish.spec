%global source0_hash ad6f8984f83317b901a47c1c715ab88d477d5257c8f31a660cd0ac2aae566fe8

%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%define pear_name Crypt_Blowfish
%define beta RC2

Name:           php-pear-Crypt-Blowfish
Version:        1.1.0
Release:        0.35.rc2%{?dist}
Summary:        Quick two-way blowfish encryption

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://pear.php.net/package/Crypt_Blowfish
Source0:        http://pear.php.net/get/%{pear_name}-%{version}%{?beta}.tgz

BuildArch:      noarch
BuildRequires:  php-pear >= 1:1.4.9-1.2
Requires:       php-pear(PEAR)
Requires(post): %{__pear}
Requires(postun): %{__pear}
Provides:       php-pear(%{pear_name}) = %{version}

%description
This package allows you to perform two-way blowfish encryption on the fly using
only PHP. This package does not require the MCrypt PHP extension to work,
although it can make use of it if available.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
[ -f package2.xml ] || mv package.xml package2.xml
mv package2.xml %{pear_name}-%{version}%{?beta}/%{name}.xml
cd %{pear_name}-%{version}%{?beta}

%build
cd %{pear_name}-%{version}%{?beta}
# Empty build section, most likely nothing required.

%install
cd %{pear_name}-%{version}%{?beta}
rm -rf $RPM_BUILD_ROOT docdir
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml

# Clean up unnecessary files
rm -rf $RPM_BUILD_ROOT%{pear_metadir}/.??*

# Install XML package description
mkdir -p $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}

%check
# For documentation purpose only
# After install, as root :
# cd /usr/share/pear/test/Crypt_Blowfish/tests
# pear run-tests -p Crypt_Blowfish
# Should return 
# 2 PASSED TESTS
# 0 SKIPPED TESTS

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
%{pear_phpdir}/Crypt

%changelog
%autochangelog
