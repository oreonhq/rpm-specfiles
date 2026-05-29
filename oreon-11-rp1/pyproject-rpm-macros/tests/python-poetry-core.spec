%global source0_hash d145ae121cf79118a8901b60f2c951c4edcc16f55eb8aaefc156aa33aa921f07

Name:           python-poetry-core
Version:        1.1.0
Release:        0%{?dist}
Summary:        Poetry PEP 517 Build Backend

License:        MIT
URL:            https://pypi.org/project/poetry-core/
Source0:        https://files.pythonhosted.org/packages/source/p/poetry-core/poetry-core-1.1.0.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
Test a build with pyproject.toml backend-path = [.]
poetry-core builds with poetry-core.


%package -n python3-poetry-core
Summary:        %{summary}

%description -n python3-poetry-core
...


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n poetry-core-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# the license is not marked as License-File by poetry-core, hence -L
%pyproject_save_files -L poetry

# internal check for our macros, -l must fail:
%pyproject_save_files -l poetry && exit 1 || true

%files -n python3-poetry-core -f %{pyproject_files}
%doc README.md
%license LICENSE
