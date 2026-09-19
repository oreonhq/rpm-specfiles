%global source0_hash none

Name:           python-construct-classes
Version:        0.2.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Parse your binary structs into dataclasses

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/matejcik/construct-classes
Source:         %{pypi_source construct_classes}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'construct-classes' generated automatically by pyp2spec.}

Patch0:    https://patch-diff.githubusercontent.com/raw/matejcik/construct-classes/pull/2.patch#/only-include-license-documentation-for-sdist.patch

%description %_description

%package -n     python3-construct-classes
Summary:        %{summary}

%description -n python3-construct-classes %_description


%prep
%autosetup -p1 -n construct_classes-%{version}


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


%files -n python3-construct-classes -f %{pyproject_files}

%changelog
%autochangelog
