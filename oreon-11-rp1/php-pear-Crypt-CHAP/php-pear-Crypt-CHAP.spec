%global source0_hash 1293a59cb93cd32dbde8b0b4a4e094d7021cd88184791075a6771852e4c48da9
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name Crypt_CHAP
Name:           php-pear-Crypt-CHAP
Version:        1.5.0
Release:        32%{?dist}
Summary:        Class to generate CHAP packets
License:        LicenseRef-Callaway-BSD
URL:            http://pear.php.net/package/Crypt_CHAP
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz
Patch0:         %{pear_name}-php8.patch
BuildArch:      noarch
Requires:       php-pear(PEAR) 
Requires:       php-mcrypt
Requires(post): %{__pear}
Requires(postun): %{__pear}
Provides:       php-pear(%{pear_name}) = %{version}
# oreon:deps
BuildRequires:  php-mcrypt
BuildRequires:  php-pear
# /oreon:deps
%description
This package provides Classes for generating CHAP packets.  
Currently these types of CHAP are supported: 
- CHAP-MD5, 
- MS-CHAPv1, 
- MS-CHAPv2. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc
cd %{pear_name}-%{version}
%patch -P0 -p1 -b .php8
sed -e "s/md5sum=.*name/name/" ../package.xml >%{name}.xml

%build

cd %{pear_name}-%{version}
%install
cd %{pear_name}-%{version}
rm -rf $RPM_BUILD_ROOT docdir
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml
rm -rf $RPM_BUILD_ROOT%{pear_metadir}/.??*
mkdir -p $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}
%oreon_autofiles main

%check

cd %{pear_name}-%{version}
%{__pear} run-tests \
   -i "-d include_path=%{buildroot}%{pear_phpdir}:%{pear_phpdir}" \
   tests
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
