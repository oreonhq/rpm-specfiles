%global source0_hash none

Name:           python-jsonschema-specifications
Version:        2025.9.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The JSON Schema meta-schemas and vocabularies, exposed as a Registry

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/python-jsonschema/jsonschema-specifications
Source:         %{pypi_source jsonschema_specifications}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jsonschema-specifications' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-jsonschema-specifications
Summary:        %{summary}

%description -n python3-jsonschema-specifications %_description


%prep
%autosetup -p1 -n jsonschema_specifications-%{version}


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


%files -n python3-jsonschema-specifications -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2024.10.1-7
- Prepare for Oreon 11 (RP1)
