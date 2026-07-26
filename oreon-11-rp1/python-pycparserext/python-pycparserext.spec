%global source0_hash 39b16d90ad595070069b5c9020f10fc433fa1a31a8ace346e0ae6a462d1f4e3b

Name:           python-pycparserext
Version:        2024.1
Release:        %autorelease
Summary:        Extensions for pycparser

License:        MIT
URL:            https://github.com/inducer/pycparserext
# PyPI sources do not have tests
Source:         %{url}/archive/v%{version}/pycparserext-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# Tests
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Extended functionality for Eli Bendersky's pycparser, in particular support
for parsing GNU extensions and OpenCL.}

%description %_description

%package -n     python3-pycparserext
Summary:        %{summary}

%description -n python3-pycparserext %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pycparserext-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pycparserext

%check
%pyproject_check_import
%pytest

%files -n python3-pycparserext -f %{pyproject_files}

%changelog
%autochangelog
