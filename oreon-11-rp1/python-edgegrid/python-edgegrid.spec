%global source0_hash 4f3284ab357f4aae61f48f92023b4ed0b4ddfd966a3c6f569aa7ec0502d8cc4f

Name:           python-edgegrid
Version:        2.0.1
Release:        %autorelease
Summary:        Akamai EdgeGrid authentication handler for requests
License:        Apache-2.0
URL:            https://github.com/akamai/AkamaiOPEN-edgegrid-python
BuildArch:      noarch
# PyPI tarball is missing testcases.json
# https://github.com/akamai/AkamaiOPEN-edgegrid-python/pull/94
Source:         %{url}/archive/v%{version}/edgegrid-python-%{version}.tar.gz

%global _description %{expand:
This library implements an Authentication handler for HTTP requests using the
Akamai EdgeGrid Authentication scheme for Python.}

%description %_description

%package -n python3-edgegrid
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-edgegrid %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n AkamaiOPEN-edgegrid-python-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l akamai

%check
%pytest -v

%files -n python3-edgegrid -f %{pyproject_files}
%doc README.md HISTORY.rst
%{python3_sitelib}/edgegrid_python-%{version}-py%{python3_version}-nspkg.pth

%changelog
%autochangelog
