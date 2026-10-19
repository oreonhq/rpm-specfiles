%global source0_hash 3691afdc87ad836b09b4def7f7116f64349f8eff7e787cd9df90050186877322
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name HTTP_Request
Name:           php-pear-HTTP-Request
Version:        1.4.4
Release:        1%{?dist}
Summary:        Provides an easy way to perform HTTP requests
License:        LicenseRef-Callaway-BSD
URL:            http://pear.php.net/package/HTTP_Request
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz
BuildArch:      noarch
Requires:       php-pear(PEAR) >= 1.4.3
Requires:       php-pear(Net_URL) >= 1.0.12
Requires:       php-pear(Net_Socket) >= 1.0.7
Requires(post): %{__pear}
Requires(postun): %{__pear}
Provides:       php-pear(%{pear_name}) = %{version}
# oreon:deps
BuildRequires:  php-pear
# /oreon:deps
%description
Supports GET/POST/HEAD/TRACE/PUT/DELETE, Basic authentication, Proxy,
Proxy Authentication, SSL, file uploads etc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc
cd %{pear_name}-%{version}
# Package.xml is V2
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
sed -i 's/\r//' $RPM_BUILD_ROOT%{pear_docdir}/%{pear_name}/docs/example.php
sed -i 's/\r//' $RPM_BUILD_ROOT%{pear_docdir}/%{pear_name}/docs/download-progress.php
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
