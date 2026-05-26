# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 e68023b0bfdb8cf6d9436f850029900964e9977305763ba12be9c3474ea13175
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global srcname jwcrypto

Name:           python-%{srcname}
Version:        1.4.2
Release:        %autorelease
Summary:        Implements JWK, JWS, JWE specifications using python-cryptography

License:        LGPL-3.0-or-later
URL:            https://github.com/latchset/%{srcname}
Source0:        https://github.com/latchset/%{srcname}/releases/download/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-cryptography >= 2.3
BuildRequires:  python%{python3_pkgversion}-pytest
%if %{undefined rhel}
BuildRequires:  python%{python3_pkgversion}-deprecated
%endif

%description
Implements JWK, JWS, JWE specifications using python-cryptography


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Implements JWK, JWS, JWE specifications using python-cryptography
Requires:       python%{python3_pkgversion}-cryptography >= 2.3
%if %{undefined rhel}
Requires:       python%{python3_pkgversion}-deprecated
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Implements JWK, JWS, JWE specifications using python-cryptography


%prep
%oreon_verify_sources
%setup -q -n %{srcname}-%{version}
%if %{defined rhel}
# avoid python-deprecated dependency
sed -i -e '/deprecated/d' setup.py %{srcname}.egg-info/requires.txt
sed -i -e '/^from deprecated/d' -e '/@deprecated/d' %{srcname}/*.py
%endif


%build
%py3_build


%check
%{__python3} -bb -m pytest %{srcname}/test*.py


%install
%py3_install

rm -rf %{buildroot}%{_docdir}/%{srcname}
rm -rf %{buildroot}%{python3_sitelib}/%{srcname}/tests{,-cookbook}.py*
rm -rf %{buildroot}%{python3_sitelib}/%{srcname}/__pycache__/tests{,-cookbook}.*.py*


%files -n python%{python3_pkgversion}-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.2-1
- Prepare for Oreon 11 (RP1)
