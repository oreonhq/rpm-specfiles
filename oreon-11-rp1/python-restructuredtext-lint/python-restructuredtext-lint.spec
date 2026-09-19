%global source0_hash dd25209b9e0b726929d8306339faf723734a3137db382bcf27294fa18a6bc52b

%global pkg_name restructuredtext-lint
%global pypi_name restructuredtext_lint
%global desc Lint reStructuredText linter files with an API or a CLI.\
It reports errors and warning including:\
- Unknown directives\
- Wrong usage of directives\
- Inconsistencies in title levels\
- Unexpected unindent

Name:           python-%{pkg_name}
Version:        2.0.2
Release:        2%{?dist}
Summary:        reStructuredText linter

License:        Unlicense
URL:            https://pypi.python.org/pypi/restructuredtext_lint
Source0:        %{pypi_source}
Source1:        pytest.ini

BuildArch:      noarch

%description
%{desc}

%package -n     python3-%{pkg_name}
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-PyYAML >= 3.11
BuildRequires:  python3-docutils >= 0.11
BuildRequires:  python3-docutils < 1.0
Requires:       python3-docutils >= 0.11
Requires:       python3-docutils < 1.0

%description -n python3-%{pkg_name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1
cp -a %{SOURCE1} .
# Remove pyc files from source
find -name '*.pyc' -delete

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import

PYTHONPATH="$(pwd)" pytest-%{python3_version} -v

%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.rst
%license UNLICENSE
%{_bindir}/rst-lint
%{_bindir}/restructuredtext-lint

%changelog
%autochangelog
