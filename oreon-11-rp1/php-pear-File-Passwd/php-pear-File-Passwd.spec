%global source0_hash e590579b3cdcd012f3e4882bee7590be3cb60145b4ccea689d28403c1b0b9173
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name File_Passwd
Name:           php-pear-File-Passwd
Version:        1.1.7
Release:        1%{?dist}
Summary:        Manipulate many kinds of password files
License:        PHP-3.01
URL:            http://pear.php.net/package/File_Passwd
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz
BuildArch:      noarch
Requires:       php-pear(PEAR)
Requires(post): %{__pear}
Requires(postun): %{__pear}
Provides:       php-pear(%{pear_name}) = %{version}
Requires: php-pear(Crypt_CHAP) >= 1.0.0
# oreon:deps
BuildRequires:  php-pear
# /oreon:deps
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
%install
rm -rf $RPM_BUILD_ROOT
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml
rm -rf $RPM_BUILD_ROOT%{pear_metadir}/.??*
install -d $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}
%oreon_autofiles main

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
