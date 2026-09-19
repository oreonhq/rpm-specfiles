%global source0_hash none

Name:           python-prometheus-client
Version:        0.26.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python client for the Prometheus monitoring system.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0 AND BSD-2-Clause
URL:            https://github.com/prometheus/client_python
Source:         %{pypi_source prometheus_client}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'prometheus-client' generated automatically by pyp2spec.}

Patch0001:      0001-Remove-the-bundled-decorator-package.patch

%description %_description

%package -n     python3-prometheus-client
Summary:        %{summary}

%description -n python3-prometheus-client %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-prometheus-client aiohttp,django,twisted


%prep
%autosetup -p1 -n prometheus_client-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x aiohttp,django,twisted


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-prometheus-client -f %{pyproject_files}

%changelog
%autochangelog
