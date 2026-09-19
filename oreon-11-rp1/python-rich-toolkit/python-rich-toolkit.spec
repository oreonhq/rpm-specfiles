%global source0_hash none

Name:           python-rich-toolkit
Version:        0.20.5
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Rich toolkit for building command-line applications

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            ...
Source:         %{pypi_source rich_toolkit}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'rich-toolkit' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-rich-toolkit
Summary:        %{summary}

%description -n python3-rich-toolkit %_description


%prep
%autosetup -p1 -n rich_toolkit-%{version}


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


%files -n python3-rich-toolkit -f %{pyproject_files}

%changelog
%autochangelog
