%global source0_hash bbf20363beb2a2cae920b174cfae6297140d3cc536ea3dd00258f59340af1600

%{!?__pear: %global __pear %{_bindir}/pear}
%global pear_name CodeGen_PECL

Summary:           Tool to generate PECL extensions from an XML description
Name:              php-pear-CodeGen-PECL
Version:           1.1.3
Release:           35%{?dist}
License:           PHP-3.01
URL:               https://pear.php.net/package/%{pear_name}
Source0:           https://pear.php.net/get/%{pear_name}-%{version}.tgz
Patch0:            php-pear-CodeGen-PECL-1.1.3-php54.patch
Requires:          php-common >= 5.4.0
Requires:          php-pear(CodeGen) >= 1.0.7
Requires(post):    %{__pear}
Requires(postun):  %{__pear}
Provides:          php-pear(%{pear_name}) = %{version}
BuildRequires:     php-pear >= 1:1.4.9-1.2
BuildRequires:     php-pear(CodeGen) >= 1.0.7
BuildArch:         noarch

%description
CodeGen_PECL (formerly known as PECL_Gen) is a pure PHP replacement for
the ext_skel shell script that comes with the PHP 4 source. It reads in
configuration options, function prototypes and code fragments from an
XML description file and then generates a complete ready-to-compile PECL
extension.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
%patch -P0 -p0 -b .php54

# Package is V2
cd %{pear_name}-%{version}
mv -f ../package.xml %{name}.xml

%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.

%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml

# Clean up unnecessary files
rm -rf $RPM_BUILD_ROOT%{pear_metadir}/.??*

# Install XML package description
install -D -p -m 0644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}/%{name}.xml

%check
find . -name "*.php" -type f -print0 | xargs -n 1 -0 php -l

%post
%{__pear} install --nodeps --soft --force --register-only %{pear_xmldir}/%{name}.xml > /dev/null || :

%postun
if [ $1 -eq 0 ]; then
  %{__pear} uninstall --nodeps --ignore-errors --register-only %{pear_name} > /dev/null || :
fi

%files
%doc %{pear_docdir}/%{pear_name}
%{_bindir}/pecl-gen
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/CodeGen/PECL/

%changelog
%autochangelog
