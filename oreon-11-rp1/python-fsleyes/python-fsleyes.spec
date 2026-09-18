%global source0_hash none

Name:           python-fsleyes
Version:        1.20.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        FSLeyes, the FSL image viewer

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://git.fmrib.ox.ac.uk/fsl/fsleyes/fsleyes/
Source:         %{pypi_source fsleyes}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'fsleyes' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-fsleyes
Summary:        %{summary}

%description -n python3-fsleyes %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-fsleyes darwin,doc,extra,style,test


%prep
%autosetup -p1 -n fsleyes-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x darwin,doc,extra,style,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-fsleyes -f %{pyproject_files}
%{_bindir}/render

%changelog
%autochangelog
