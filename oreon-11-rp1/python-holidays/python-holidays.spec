%global source0_hash faea731dacb71fc3f364246a35d0aa68f2af500f9bd65bcf8f28f747ca28b79f

Name:           python-holidays
Version:        0.93
Release:        %autorelease
Summary:        Generate and work with holidays in Python

License:        MIT
URL:            https://github.com/vacanza/holidays
Source0:        %{url}/archive/v%{version}/holidays-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A fast, efficient Python library for generating country, province and state 
specific sets of holidays on the fly. It aims to make determining whether a
specific date is a holiday as fast and flexible as possible.}

%description %_description

%package -n     python3-holidays
Summary:        %{summary}

%description -n python3-holidays %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n holidays-%{version}

# remove coverage options from pytest
sed -i '/--cov-fail-under=100/ d' pyproject.toml
%if %{fedora} <= 42
# correct license declaration: errors on F42
sed -i -e '/^license/ d' pyproject.toml
%endif

# sanitize test requirements, unpin
sed -i -e '/coverage/ d' \
    -e '/pytest-cov/ d' \
    -e 's/pytest>.*"/pytest"/' \
    -e 's/pytest-xdist>.*"/pytest"/' \
    pyproject.toml

cat pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -g tests,build

%build
%{python3} scripts/l10n/generate_mo_files.py

%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l holidays

%check
%pyproject_check_import

%if %{fedora} <= 42
%pytest -v -k "not test_metadata" .
%else
%pytest -v -k .
%endif

%files -n python3-holidays -f %{pyproject_files}
%doc README.md CHANGES.md CONTRIBUTORS

%changelog
%autochangelog
