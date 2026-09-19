%global source0_hash none

Name:           python-fsleyes-props
Version:        1.13.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        _wx_Python event programming framework

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://git.fmrib.ox.ac.uk/fsl/fsleyes/props
Source:         %{pypi_source fsleyes_props}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'fsleyes-props' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-fsleyes-props
Summary:        %{summary}

%description -n python3-fsleyes-props %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-fsleyes-props doc,style,test


%prep
%autosetup -p1 -n fsleyes_props-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x doc,style,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-fsleyes-props -f %{pyproject_files}

%changelog
%autochangelog
