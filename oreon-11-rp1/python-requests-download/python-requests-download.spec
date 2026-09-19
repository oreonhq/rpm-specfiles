%global source0_hash 92d895a6ca51ea51aa42bab864bddaee31b5601c7e7e1ade4c27b0eb6695d846

%global pypi_name requests_download
Name:           python-requests-download
Version:        0.1.2
Release:        %autorelease
Summary:        Download files using requests and save them to a target path

License:        MIT
URL:            https://www.github.com/takluyver/requests_download
Source0:        %{pypi_source}

# Switch build-backend to flit_core , proposed upstream
Patch:          https://github.com/takluyver/requests_download/pull/3.patch#/switch-build-backend-to-flit_core.patch

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
A convenient function to download to a file using requests.

Basic usage:

    url = "https://github.com/takluyver/requests_download/archive/master.zip"
    download(url, "requests_download.zip")

An optional headers= parameter is passed through to requests.}

%description %_description

%package -n     python3-requests-download
Summary:        %{summary}
%{?python_provide:%python_provide python3-requests-download}

%description -n python3-requests-download  %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%check
# as of 0.1.2, upstream has no tests :(
export PYTHONPATH=%{buildroot}%{python3_sitelib}
%{python3} -c 'import sys; sys.path.remove(""); import requests_download'

%files -n python3-requests-download
%license LICENSE
%doc README.rst
%pycached %{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
%autochangelog
