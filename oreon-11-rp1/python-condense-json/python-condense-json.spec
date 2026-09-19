%global source0_hash none

Name:           python-condense-json
Version:        1.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python function for condensing JSON using replacement strings

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/simonw/condense-json
Source:         %{pypi_source condense_json}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'condense-json' generated automatically by pyp2spec.}

Patch:          python-condense-json-0.1.3-toml.patch

%description %_description

%package -n     python3-condense-json
Summary:        %{summary}

%description -n python3-condense-json %_description


%prep
%autosetup -p1 -n condense_json-%{version}


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


%files -n python3-condense-json -f %{pyproject_files}

%changelog
%autochangelog
