%global source0_hash none

Name:           python-nitime
Version:        0.12.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Nitime: timeseries analysis for neuroscience data

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            http://nipy.org/nitime
Source:         %{pypi_source nitime}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'nitime' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-nitime
Summary:        %{summary}

%description -n python3-nitime %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-nitime full


%prep
%autosetup -p1 -n nitime-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x full


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-nitime -f %{pyproject_files}

%changelog
%autochangelog
