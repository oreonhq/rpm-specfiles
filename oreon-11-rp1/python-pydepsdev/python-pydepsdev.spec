%global source0_hash c009e35eeb1f33632044ac23597ada38221fdac27d075be1cab73914317e4eef

%global pypi_name pydepsdev

Name:           python-%{pypi_name}
Version:        0.2.3
Release:        %autorelease
Summary:        Python library for interacting with Open Source Insights API (deps.dev)

License:        Apache-2.0
URL:            https://codeberg.org/eclipseo/pydepsdev
Source:         %{pypi_source %{pypi_name}}

BuildArch:      noarch
BuildRequires:  python3-devel

%global common_description %{expand:
A Python library for interacting with Open Source Insights API (deps.dev).
Easily fetch package, version, and project data from the API.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}
# Because these use an older version than python-setuptools 77
%if 0%{?fedora} <= 42 || 0%{?rhel} <= 10
sed -i 's|license = "Apache-2.0"|license = {text = "Apache-2.0"}|;/^license-files = /d' pyproject.toml
%endif

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{pypi_name}

%check
%tox

%files -n python3-pydepsdev -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
