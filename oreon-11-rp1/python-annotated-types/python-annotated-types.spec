%global source0_hash none

Name:           python-annotated-types
Version:        0.8.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Reusable constraint types to use with typing.Annotated

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/annotated-types/annotated-types
Source:         %{pypi_source annotated_types}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'annotated-types' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-annotated-types
Summary:        %{summary}

%description -n python3-annotated-types %_description


%prep
%autosetup -p1 -n annotated_types-%{version}


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


%files -n python3-annotated-types -f %{pyproject_files}

%changelog
%autochangelog
