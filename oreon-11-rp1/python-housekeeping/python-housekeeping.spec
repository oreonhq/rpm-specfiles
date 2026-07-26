%global source0_hash 75e71f1cc501885406f6be81410c9b05361871a3ecccde3891336da1e92426b5

Name:           python-housekeeping
Version:        1.1
Release:        %autorelease
Summary:        Python utilities for helping deprecate and remove code

License:        MIT
URL:            https://pypi.org/project/housekeeping/
Source:         %{pypi_source housekeeping}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Housekeeping is a Python package designed to make it easy for projects to mark
consumed code as deprecated or pending deprecation, with helpful instructions
for consumers using deprecated functionality.}

%description %_description

%package -n     python3-housekeeping
Summary:        %{summary}

%description -n python3-housekeeping %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n housekeeping-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l housekeeping

%check
%pyproject_check_import
%pytest

%files -n python3-housekeeping -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
