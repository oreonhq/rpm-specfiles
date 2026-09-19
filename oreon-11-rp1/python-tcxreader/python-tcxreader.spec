%global source0_hash none

Name:           python-tcxreader
Version:        0.4.11
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        tcxreader is a reader for Garmin’s TCX file format. It also works well with missing data!

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/alenrajsp/tcxreader
Source:         %{pypi_source tcxreader}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'tcxreader' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-tcxreader
Summary:        %{summary}

%description -n python3-tcxreader %_description


%prep
%autosetup -p1 -n tcxreader-%{version}


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


%files -n python3-tcxreader -f %{pyproject_files}

%changelog
%autochangelog
