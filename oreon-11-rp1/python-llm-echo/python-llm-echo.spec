%global source0_hash none

Name:           python-llm-echo
Version:        0.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Debug plugin for LLM

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/simonw/llm-echo
Source:         %{pypi_source llm_echo}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'llm-echo' generated automatically by pyp2spec.}

Patch:          python-llm-0.3a3-format-fix.patch

%description %_description

%package -n     python3-llm-echo
Summary:        %{summary}

%description -n python3-llm-echo %_description


%prep
%autosetup -p1 -n llm_echo-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-llm-echo -f %{pyproject_files}

%changelog
%autochangelog
