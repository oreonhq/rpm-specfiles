%global source0_hash 68d35a8bdd4bdf84c35f5475f5ee94280825d3af2caa748d7824b7b1f91791a7
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name OLE
%global prever    RC2
Name:           php-pear-OLE
Version:        1.0.0
Release:        1%{?dist}
Summary:        Package for reading and writing OLE containers
License:        PHP-3.01
URL:            http://pear.php.net/package/OLE
Source0:        http://pear.php.net/get/%{pear_name}-%{version}%{prever}.tgz
BuildArch:      noarch
Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php-pear(PEAR)
Requires:       php-date
Provides:       php-pear(%{pear_name}) = %{version}
# oreon:deps
BuildRequires:  php-pear
# /oreon:deps
%description
This package allows reading and writing of OLE (Object Linking and
Embedding) compound documents. This format is used as container for Excel
(.xls), Word (.doc) and other Microsoft file formats.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
cd %{pear_name}-%{version}%{?prever}
mv ../package.xml %{name}.xml

%build

cd %{pear_name}-%{version}%{?prever}
%install
cd %{pear_name}-%{version}%{?prever}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml
rm -rf $RPM_BUILD_ROOT%{pear_metadir}/.??*
mkdir -p $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}
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
