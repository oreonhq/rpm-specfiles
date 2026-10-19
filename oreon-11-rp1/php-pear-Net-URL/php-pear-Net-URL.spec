%global source0_hash 349a183b82535283fd02c70e25053e9821d47d1e81384fd24b9c56d65e4dad29
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name Net_URL
Name:           php-pear-Net-URL
Version:        1.0.15
Release:        1%{?dist}
Summary:        Easy parsing of URLs
License:        LicenseRef-Callaway-BSD
URL:            http://pear.php.net/package/Net_URL
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz
BuildArch:      noarch
Requires:       php-pear(PEAR)
Requires(post): %{__pear}
Requires(postun): %{__pear}
Provides:       php-pear(%{pear_name}) = %{version}
# oreon:deps
BuildRequires:  php-pear
# /oreon:deps
%description
Provides easy parsing of URLs and their constituent parts.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc

cd %{pear_name}-%{version}
# Package is V2
mv ../package.xml %{name}.xml

%build

cd %{pear_name}-%{version}
%install
cd %{pear_name}-%{version}
rm -rf $RPM_BUILD_ROOT docdir
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
