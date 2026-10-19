%global source0_hash 71bf24a209ecf0e69092ff29660bdc8b681db42732c15ce4901dca6f315bf8f5
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name Console_Table
Name:           php-pear-Console-Table
Version:        1.3.1
Release:        1%{?dist}
Summary:        Class that makes it easy to build console style tables
License:        LicenseRef-Callaway-BSD
URL:            http://pear.php.net/package/Console_Table
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz
Patch0:         %{pear_name}-php8.patch
BuildArch:      noarch
Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php-pcre
Requires:       php-pear(PEAR)
Requires:       php-mbstring
Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/console_table) = %{version}
# oreon:deps
BuildRequires:  php-mbstring
BuildRequires:  php-pear
# /oreon:deps
%description
Provides methods such as addRow(), insertRow(), addCol() etc. to build
console tables with or without headers and with user defined table rules
and padding.
 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

cd %{pear_name}-%{version}
%patch -P0 -p1 -b .php8
sed -e '/Table.php/s/md5sum=.*name/name/' ../package.xml >%{name}.xml

%build

cd %{pear_name}-%{version}
%install
cd %{pear_name}-%{version}
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
        %{pear_name} >/dev/null || :
fi
%check

cd %{pear_name}-%{version}
%{__pear} \
   run-tests \
   -i "-d include_path=%{buildroot}%{pear_phpdir}:%{pear_phpdir}" \
   tests | tee ../tests.log
if grep -q "FAILED TESTS" ../tests.log; then
  for fic in tests/*.diff; do
    cat $fic; echo -e "\n"
  done
  exit 1
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
