%global source0_hash 41faf1f90e2ca5cd577fa07ffefe90286e432df51ccef2822d0de6d013922f04

%global srcname sphinx-hoverxref
%global sum Sphinx extension to add tooltips on cross references

Name:           python-%{srcname}
Version:        1.4.1
Release:        %autorelease
Summary:        %{sum}
BuildArch:      noarch

License:        MIT
Url:            https://%{srcname}.readthedocs.io/en/latest/
Source:         https://github.com/readthedocs/%{srcname}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
# drop references to .
# drop dependency on pdbpp, it requires a lot of unpackaged modules and pyrepl is broken and inactive upstream
Patch:          sphinx-hoverxref-fix_tox_ini.diff

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools

%global _description %{expand:
Sphinx extension to show a floating window (tooltips or modal dialogues) on the
cross references of the documentation embedding the content of the linked
section on them. With sphinx-hoverxref, you don’t need to click a link to see
what’s in there.}

%description %_description

%package -n python3-%{srcname}
Requires:       python3-sphinx
BuildRequires:  python3-sphinx
Summary:        %{sum}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
# remove superfluous files
rm -rf %{buildroot}%{python3_sitelib}/tests/

%pyproject_save_files hoverxref

%check
# exclude intersphinx tests, they don't work offline
%pytest -v tests/ -k "not test_intersphinx_default_configs and not test_intersphinx_python_mapping and not test_intersphinx_all_mappings"

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
