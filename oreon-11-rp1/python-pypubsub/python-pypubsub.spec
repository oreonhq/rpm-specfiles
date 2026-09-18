%global source0_hash none

Name:           python-pypubsub
Version:        4.0.7
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python Publish-Subscribe Package

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-2-Clause
URL:            https://github.com/schollii/pypubsub
Source:         %{pypi_source pypubsub}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pypubsub' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pypubsub
Summary:        %{summary}

%description -n python3-pypubsub %_description


%prep
%autosetup -p1 -n pypubsub-%{version}


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


%files -n python3-pypubsub -f %{pyproject_files}

%changelog
%autochangelog
