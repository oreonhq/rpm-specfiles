%global source0_hash 350cb71a4fbd58e037c7182cafa14e6f6df952126869205918fcc9ec5798e2fa
%global pecl_name        gmagick
%global ini_name         40-%{pecl_name}.ini
%global upstream_version 2.0.6
%global upstream_prever  RC1
%global sources          %{pecl_name}-%{upstream_version}%{?upstream_prever}
Summary:        Provides a wrapper to the GraphicsMagick library
Name:           php-pecl-%{pecl_name}
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        1%{?dist}
License:        PHP-3.01
Source0:        https://pecl.php.net/get/%{pecl_name}-%{upstream_version}%{upstream_prever}.tgz
Source1:        %{pecl_name}.ini
Patch0:         %{pecl_name}-php81.patch
Patch1:         %{pecl_name}-build.patch
Patch2:         %{pecl_name}-php85.patch
URL:            https://pecl.php.net/package/%{pecl_name}
ExcludeArch:    %{ix86}
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Provides:       php-pecl(%{pecl_name}) = %{version}
Conflicts:      php-pecl-imagick
Conflicts:      php-magickwand
# oreon:deps
BuildRequires:  GraphicsMagick-devel
BuildRequires:  php-devel
BuildRequires:  php-pear
# /oreon:deps
%description
%{pecl_name} is a php extension to create, modify and obtain meta information of
images using the GraphicsMagick API.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc
cd %{sources}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build

cd %{sources}
%{__phpize}
%{configure} --with-%{pecl_name} --with-php-config=%{__phpconfig}
make %{?_smp_mflags}
%install
cd %{sources}
make install INSTALL_ROOT=%{buildroot}
install -m 0755 -d %{buildroot}%{pecl_xmldir}
install -m 0664 ../package.xml %{buildroot}%{pecl_xmldir}/%{pecl_name}.xml
install -d %{buildroot}%{_sysconfdir}/php.d/
install -m 0664 %{SOURCE1} %{buildroot}%{_sysconfdir}/php.d/%{ini_name}
%oreon_autofiles main

%check

php --no-php-ini \
    --define extension_dir=%{buildroot}%{php_extdir} \
    --define extension=gmagick.so \
    --modules | grep '^%{pecl_name}$'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
