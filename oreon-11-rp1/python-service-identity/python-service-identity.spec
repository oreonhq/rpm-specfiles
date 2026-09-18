%global source0_hash none

Name:           python-service-identity
Version:        26.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Service identity verification for pyOpenSSL _ cryptography.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pyca/service-identity
Source:         %{pypi_source service_identity}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'service-identity' generated automatically by pyp2spec.}

Patch:          0001-Remove-coverage-toml-test-dependency.patch
Patch:          0002-Remove-hatch-fancy-pypi-readme-build-system-dependency.patch

%description %_description

%package -n     python3-service-identity
Summary:        %{summary}

%description -n python3-service-identity %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-service-identity idna


%prep
%autosetup -p1 -n service_identity-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x idna


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-service-identity -f %{pyproject_files}

%changelog
%autochangelog
