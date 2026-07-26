%global source0_hash d2d4e4787672911b48350df02ed3fa3fffdc2f2e8ca06dd6afdf34189b76a9dd

Name:           python-multidict
Version:        6.6.4
Release:        %autorelease
Summary:        MultiDict implementation

License:        Apache-2.0
URL:            https://github.com/aio-libs/multidict
Source:         %{pypi_source multidict}

BuildRequires:  gcc

%global _description %{expand:
Multidict is dict-like collection of key-value pairs where key might occur more
than once in the container.}

%description %_description

%package -n python3-multidict
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-cython
BuildRequires:  python3-pytest
BuildRequires:  python3-psutil

%description -n python3-multidict %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n multidict-%{version}
sed -e "/--cov/d" \
    -e "/-p pytest_cov/d" \
    -i pytest.ini

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l multidict

%check
# circular import tests fail in mock
# benchmark tests require pytest_codspeed which isn't packaged yet
# leaks & isolated tests require objgraph which isn't packaged yet
%pytest \
    --verbose \
    -m "not leaks" \
    --ignore tests/test_circular_imports.py \
    --ignore tests/test_multidict_benchmarks.py \
    --ignore tests/test_views_benchmarks.py \
    --ignore tests/isolated/multidict_extend_dict.py \
    --ignore tests/isolated/multidict_extend_multidict.py \
    --ignore tests/isolated/multidict_extend_tuple.py \
    --ignore tests/isolated/multidict_update_multidict.py \
    tests

%files -n python3-multidict -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
