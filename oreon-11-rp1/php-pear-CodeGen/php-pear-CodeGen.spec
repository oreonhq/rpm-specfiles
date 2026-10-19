%global source0_hash 53841e81dc9e14c9d137bd8f3ab927a1d6d22038685672fca0b05166a4574c0e
%{!?__pear: %global __pear %{_bindir}/pear}
%global pear_name CodeGen
Summary:        Framework to create code generators that operate on XML descriptions
Name:              php-pear-%{pear_name}
Version:           1.0.7
Release:        1%{?dist}
License:           PHP-3.01
URL:               https://pear.php.net/package/%{pear_name}
Source0:        https://pear.php.net/get/%{pear_name}-%{version}.tgz
Patch0:            php-pear-CodeGen-1.0.7-php54.patch
Requires:          php-xml >= 5.4.0
Requires:          php-pear(PEAR)
Requires:          php-pear(Console_Getopt) >= 1.0
Requires(post):    %{__pear}
Requires(postun):  %{__pear}
Provides:          php-pear(%{pear_name}) = %{version}
BuildArch:         noarch
# oreon:deps
BuildRequires:  php-pear
BuildRequires:  php-pear(Console_Getopt)
# /oreon:deps
%description
Provides the base framework to create code generators that operate on XML
descriptions like CodeGen_PECL and CodeGen_MySqlUDF.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
%patch -P0 -p0 -b .php54

# Package is V2
cd %{pear_name}-%{version}
mv -f ../package.xml %{name}.xml

%build

cd %{pear_name}-%{version}
%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml
rm -rf $RPM_BUILD_ROOT%{pear_metadir}/.??*
install -D -p -m 0644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}/%{name}.xml
%oreon_autofiles main

%check

find . -name "*.php" -type f -print0 | xargs -n 1 -0 php -l
%post

%{__pear} install --nodeps --soft --force --register-only %{pear_xmldir}/%{name}.xml > /dev/null || :
%postun

if [ $1 -eq 0 ]; then
  %{__pear} uninstall --nodeps --ignore-errors --register-only %{pear_name} > /dev/null || :
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
