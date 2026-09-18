%global source0_hash none

Name:           python-xarray-einstats
Version:        0.11.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Stats, linear algebra and einops for xarray

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/arviz-devs/xarray-einstats
Source:         %{pypi_source xarray_einstats}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'xarray-einstats' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-xarray-einstats
Summary:        %{summary}

%description -n python3-xarray-einstats %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-xarray-einstats doc,einops,numba,test


%prep
%autosetup -p1 -n xarray_einstats-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x doc,einops,numba,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-xarray-einstats -f %{pyproject_files}

%changelog
%autochangelog
