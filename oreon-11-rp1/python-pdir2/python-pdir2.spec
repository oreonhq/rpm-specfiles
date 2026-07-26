%global source0_hash 7d278172b32f44956c3dc750e7c6cfbe2d53098021e96e2b619bf796b469ecdd

Name:           python-pdir2
Version:        1.1.0
Release:        7%{?dist}
Summary:        Pretty dir() printing with joy

License:        MIT
URL:            https://github.com/laike9m/pdir2
Source0:        %{pypi_source pdir2}

# https://github.com/laike9m/pdir2/issues/78
Patch0:         python313.patch

BuildArch:      noarch

BuildRequires:  python3-devel python3-pip python3-pdm-pep517
BuildRequires:  python3-typing-extensions
BuildRequires:  pytest

%global _description %{expand:
An improved version of dir() with better output.  Attributes are grouped by
types/functionalities, with beautiful colors.  Supports ipython, ptpython,
bpython, and Jupyter Notebook.}

%description %_description

%package -n python3-pdir2
Summary: %{summary}

%description -n python3-pdir2 %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pdir2-%{version} -p 1
# We can’t respect preemptive upper bounds on dependency versions. At least
# convert them into lower bounds. Also turn invalid version specifiers (.*)
# into valid ones, see: https://fedoraproject.org/wiki/Changes/Update_python-packaging_to_version_22_plus
sed -r -i 's/=(=[[:digit:]\.]+)\.\*/>\1/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pdir

%check
%pytest

%files -n python3-pdir2 -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
