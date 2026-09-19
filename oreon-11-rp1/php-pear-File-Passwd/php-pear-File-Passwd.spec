%global source0_hash 64cf846ab3739caa6f0abdb399847a637082a5c754010a7948a9bfeb5fbfb5a2

%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name File_Passwd

Name:           php-pear-File-Passwd
Version:        1.1.7
Release:        33%{?dist}
Summary:        Manipulate many kinds of password files

# Automatically converted from old format: PHP - review is highly recommended.
License:        PHP-3.01
URL:            http://pear.php.net/package/File_Passwd
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch

BuildRequires:  php-pear
Requires:       php-pear(PEAR)
Requires(post): %{__pear}
Requires(postun): %{__pear}
Provides:       php-pear(%{pear_name}) = %{version}

Requires: php-pear(Crypt_CHAP) >= 1.0.0

%description
Provides methods to manipulate and authenticate against standard Unix,
SMB server, AuthUser (.htpasswd), AuthDigest (.htdigest), CVS pserver
and custom formatted password files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc
cd %{pear_name}-%{version}
# package.xml is V2
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
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi

%files
%{pear_xmldir}/%{name}.xml
%{pear_testdir}/%{pear_name}
%dir %{pear_phpdir}/File
%{pear_phpdir}/File/Passwd*

%changelog
%autochangelog
