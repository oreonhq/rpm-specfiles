%global source0_hash adf8b1e984dd90d0589aa4c736edd4730efab272357e204cf7185b87dcf49973

%global srcname winrm

Name:           python-%{srcname}
Version:        0.5.0
Release:        7%{?dist}
Summary:        Python libraries for interacting with windows remote management

License:        MIT
URL:            https://pypi.python.org/pypi/pywinrm
Source0:        https://github.com/diyan/pywinrm/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Drop mock requirement
Patch0:         https://github.com/diyan/pywinrm/pull/385.patch
# Cleanup tests
Patch1:         https://github.com/diyan/pywinrm/pull/388.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
This has the python libraries for interacting with Windows Remote Management.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pywinrm-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l winrm

%check
%python3 -m pytest -vv winrm/tests

%files -n python3-%{srcname} -f %pyproject_files
#license LICENSE
%doc README.md CHANGELOG.md
#{python3_sitelib}/pywinrm-*.egg-info/
#{python3_sitelib}/winrm/

%changelog
%autochangelog
