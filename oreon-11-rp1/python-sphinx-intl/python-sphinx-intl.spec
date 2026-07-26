%global source0_hash 04b0d8ea04d111a7ba278b17b7b3fe9625c58b6f8ffb78bb8a1dd1288d88c1c7

%global pypi_name sphinx-intl
%global srcname sphinx_intl
%global cmdname sphinx-intl
%global project_owner sphinx-doc
%global github_name sphinx-intl
%global desc sphinx-intl is a utility tool that provides several features that make it easy \
to translate and to apply translation to Sphinx generated document. Optional: \
support the Transifex service for translation with Sphinx (not packaged yet).

Name:           python-%{pypi_name}
Version:        2.3.2
Release:        5%{?dist}
Summary:        Sphinx utility that make it easy to translate and to apply translation

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %pypi_source

BuildArch:      noarch

%description
%desc

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-click
BuildRequires:  python%{python3_pkgversion}-babel
BuildRequires:  python%{python3_pkgversion}-sphinx
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}-click
Requires:       python%{python3_pkgversion}-babel
Requires:       python%{python3_pkgversion}-sphinx
Conflicts:      python2-%{pypi_name} < 0.9.11-6

%description -n python%{python3_pkgversion}-%{pypi_name}
%desc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sphinx_intl-%{version} -p1
# Correct line encoding in README.rst
sed -i 's/\r$//' README.rst

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinx_intl
pushd %{buildroot}%{_bindir}
mv %{cmdname} %{cmdname}-%{python3_version}
ln -s %{cmdname}-%{python3_version} %{cmdname}-3
ln -s %{cmdname}-3 %{cmdname}
popd

%check
%pyproject_check_import
# Transifex is not packaged. Remove tests that depens on it.
rm tests/test_*transifex*.py
# Too many things are not included in the source to run the tests correctly.
#pytest -v tests

%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/%{cmdname}-3*
%{_bindir}/%{cmdname}

%changelog
%autochangelog
