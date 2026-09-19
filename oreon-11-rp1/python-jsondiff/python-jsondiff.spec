%global source0_hash 5c82ec30ead6519e00f07487bb5391b9c6a620b372a642de7efc006720b44177

# tests are enabled by default
%bcond_without  tests

%global         srcname     jsondiff
%global         forgeurl    https://github.com/xlwings/jsondiff
Version:        2.2.1
%global         tag         %{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Diff JSON and JSON-like structures in Python

License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
Diff JSON and JSON-like structures in Python}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -r

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%if %{with tests}
%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_check_import
%pytest
%endif

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files jsondiff

# Remove the jsondiff binary to avoid conflict with python-jsonpatch.
# See BZ 1967775 for more details.
rm -f %{buildroot}%{_bindir}/%{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md
%{_bindir}/jdiff

%changelog
%autochangelog
