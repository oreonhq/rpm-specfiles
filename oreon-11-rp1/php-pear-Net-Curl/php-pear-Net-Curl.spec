%global source0_hash d460c7fbe578ae86a7c591e2db700d81f7809106fe94dc6832153d307f87e55b
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name Net_Curl
Name:           php-pear-Net-Curl
Version:        1.2.5
Release:        35%{?dist}
Summary:        OO interface to PHP's cURL extension
License:        LicenseRef-Callaway-BSD
URL:            http://pear.php.net/package/Net_Curl
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
Provides an Object-Oriented interface to PHP's curl extension.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc
cd %{pear_name}-%{version}
# Package is V2
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
    %{pear_xmldir}/%{name}.xml >/dev/null ||:
%postun

if [ "$1" -eq "0" ]; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null ||:
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
