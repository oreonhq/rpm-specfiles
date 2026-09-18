%global source0_hash none

Name:           python-openai
Version:        3.14.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The official Python library for the openai API

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/openai/openai-python
Source:         %{pypi_source openai}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'openai' generated automatically by pyp2spec.}

Patch1:         0001-Relax-hatchling-requirement.patch

%description %_description

%package -n     python3-openai
Summary:        %{summary}

%description -n python3-openai %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-openai aiohttp,bedrock,datalib,realtime,voice-helpers


%prep
%autosetup -p1 -n openai-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x aiohttp,bedrock,datalib,realtime,voice-helpers


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-openai -f %{pyproject_files}

%changelog
%autochangelog
