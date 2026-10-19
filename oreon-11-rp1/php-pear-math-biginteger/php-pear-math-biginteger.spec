%global source0_hash ad0873c77fc2387e24984f4bad1c48b29442299aad9cdbeea1d2da23fbf796ef
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name Math_BigInteger
Name:           php-pear-math-biginteger
Version:        1.0.3
Release:        1%{?dist}
Summary:        Pure-PHP arbitrary precision integer arithmetic library
License:        MIT
URL:            http://pear.php.net/package/%{pear_name}
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz
BuildArch:      noarch
Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php-pear(PEAR)
Requires:       php-pcre
Requires:       php-openssl
Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-composer(pear/math_biginteger) = %{version}
%if 0%{?fedora} < 26 && 0%{?rhel} < 8 && 0%{?oreon} < 11
Conflicts:      php-phpseclib-math-biginteger < 2
%else
Obsoletes:      php-phpseclib-math-biginteger < 2
Provides:       php-phpseclib-math-biginteger = 1:%{version}
Provides:       php-pear(phpseclib.sourceforge.net/%{pear_name}) = %{version}
%endif
# oreon:deps
BuildRequires:  php-pear(PEAR)
# /oreon:deps
%description
Supports base-2, base-10, base-16, and base-256 numbers. Uses the GMP or
BCMath extensions, if available, and an internal implementation, otherwise.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
cd %{pear_name}-%{version}
# See https://github.com/pear/Math_BigInteger/pull/5
sed -e '/demo/s/role="php"/role="doc"/' \
    -e '/demo/s/baseinstalldir="[^"]*" //' \
    -e '/benchmark/s/md5sum="[^"]*" //' \
    ../package.xml | tee %{name}.xml | grep '<file'

sed -e 's/\r//' -i demo/benchmark.php

%build

cd %{pear_name}-%{version}
%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml
rm -rf %{buildroot}%{pear_metadir}/.??*
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}
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
