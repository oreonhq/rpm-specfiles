%global source0_hash none

Name:           python-google-genai
Version:        2.24.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        GenAI Python SDK

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/googleapis/python-genai
Source:         %{pypi_source google_genai}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'google-genai' generated automatically by pyp2spec.}

Patch1:         0001-add-build-backend-to-key-to-be-complient-with-PEP517.patch

%description %_description

%package -n     python3-google-genai
Summary:        %{summary}

%description -n python3-google-genai %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-google-genai aiohttp,local-tokenizer,pyopenssl


%prep
%autosetup -p1 -n google_genai-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x aiohttp,local-tokenizer,pyopenssl


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-google-genai -f %{pyproject_files}

%changelog
%autochangelog
