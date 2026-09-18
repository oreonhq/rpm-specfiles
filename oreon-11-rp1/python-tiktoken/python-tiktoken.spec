%global source0_hash none

Name:           python-tiktoken
Version:        0.14.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        tiktoken is a fast BPE tokeniser for use with OpenAI_s models

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/openai/tiktoken
Source:         %{pypi_source tiktoken}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'tiktoken' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-tiktoken
Summary:        %{summary}

%description -n python3-tiktoken %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-tiktoken blobfile


%prep
%autosetup -p1 -n tiktoken-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x blobfile


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-tiktoken -f %{pyproject_files}

%changelog
%autochangelog
