%global source0_hash a6e684a64b0d25cfac1e7cce5de29db663c8cb14ddfb919a6a8bb28bc08cc637

%bcond tests 1

%global         srcname pycomposefile

Name:           python-%{srcname}
Version:        0.0.34
Release:        %autorelease
Summary:        Structured deserialization of Docker Compose files

License:        MIT
URL:            https://github.com/smurawski/pycomposefile
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(timeout-decorator)
%endif

%global _description %{expand:
Structured deserialization of Docker Compose files}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}
# For reasons I can't begin to guess they set the version to not-the-right-version.
sed -i 's/version = "0.0.1a1"/version = "%{version}"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Remove the installed tests.
rm -rf %{buildroot}%{python3_sitelib}/tests

%pyproject_save_files %{srcname}

%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
