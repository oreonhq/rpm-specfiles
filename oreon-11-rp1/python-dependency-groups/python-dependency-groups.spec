%global source0_hash 5b9751d5d98fbd6dfd038a560a69c8382e41afcbf7ffdbcc28a2a3f85498830f

Name:           python-dependency-groups
Version:        1.3.0
Release:        %autorelease
Summary:        An implementation of Dependency Groups (PEP 735)
License:        MIT
URL:            https://pypi.org/project/dependency-groups/
Source:         %{pypi_source dependency_groups}

BuildArch:      noarch
BuildRequires:  python3-devel
# Upstream test deps contains coverage
BuildRequires:  python3-pytest

%global _description %{expand:
An implementation of Dependency Groups (PEP 735).
This is a library which is able to parse dependency groups,
following includes, and provide that data as output.}

%description %_description

%package -n     python3-dependency-groups
Summary:        %{summary}

%description -n python3-dependency-groups %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n dependency_groups-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files dependency_groups

%check
%pytest

%files -n python3-dependency-groups -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst CHANGELOG.rst
%{_bindir}/dependency-groups
%{_bindir}/lint-dependency-groups
%{_bindir}/pip-install-dependency-groups

%changelog
%autochangelog
