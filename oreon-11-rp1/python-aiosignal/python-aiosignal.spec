%global source0_hash f47eecd9468083c2029cc99945502cb7708b082c232f9aca65da147157b251c7

Name:           python-aiosignal
Version:        1.4.0
Release:        %autorelease
Summary:        List of registered asynchronous callbacks

License:        Apache-2.0
URL:            https://github.com/aio-libs/aiosignal
Source:         %{pypi_source aiosignal}

# Downstream-only: do not fail on warnings
# This is too strict for downstream packaging.
Patch:          0001-Downstream-only-patch-out-coverage-options.patch
# Downstream-only: patch out coverage options
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0002-Downstream-only-do-not-fail-on-warnings.patch


BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)

%global common_description %{expand:
A project to manage callbacks in asyncio projects.}

%description %{common_description}

%package -n python3-aiosignal
Summary:        %{summary}

Obsoletes:      python-aiosignal-doc < 1.3.1-15

%description -n python3-aiosignal %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n aiosignal-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l aiosignal

%check
%pytest

%files -n python3-aiosignal -f %{pyproject_files}
%doc CHANGES.rst
%doc CONTRIBUTORS.txt
%doc README.rst

%changelog
%autochangelog
