%global source0_hash 6a2e57e0b324bd2fbb04cb164b87b60a2d20c9471a9d08624afa00a09a223bf1

%global pypi_name urlpy

Name:           python-%{pypi_name}
Version:        0.5.0
Release:        %autorelease
Summary:        URL Transformation, Sanitization

License:        MIT
URL:            https://github.com/aboutcode-org/urlpy
Source:         %url/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
# Remove useless shebang lines
# https://github.com/aboutcode-org/urlpy/pull/12
Patch:          0001-Remove_shebangs.patch
# Update project references
# https://github.com/aboutcode-org/urlpy/commit/d701df560c8367f3ff8f9de1123d8888e1de0be5
Patch:          0002-Update_link_references_of_ownership_from_nexB_to_aboutcode-org.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global common_description %{expand:
urlpy is a small library for URL parsing, cleanup, canonicalization and
equivalence.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires requirements-tests.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# https://github.com/aboutcode-org/urlpy/issues/11
%pytest -k "not test_unknown_protocol"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
