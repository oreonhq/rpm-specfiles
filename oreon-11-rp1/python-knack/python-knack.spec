%global source0_hash 0cccf9024bb1c59fa0c497e84bd87013707e646845126d754530087bccb29012

# tests are enabled by default
%bcond_without  tests

%global         srcname     knack
%global         forgeurl    https://github.com/microsoft/knack
Version:        0.12.0
Epoch:          1
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        A Command-Line Interface framework

License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
A Command-Line Interface framework}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files knack

%if %{with tests}
%check
%pytest -k "not test_nargs_parameter" 
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc *.rst

%changelog
%autochangelog
