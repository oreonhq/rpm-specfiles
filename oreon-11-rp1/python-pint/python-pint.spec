%global source0_hash none

Name:           python-pint
Version:        0.26.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Physical quantities module

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/hgrecco/pint
Source:         %{pypi_source pint}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pint' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pint
Summary:        %{summary}

%description -n python3-pint %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-pint all,babel,codspeed,dask,docs,matplotlib,numpy,optype,pandas,scipy,test,test-all,test-mpl,uncertainties,xarray


%prep
%autosetup -p1 -n pint-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,babel,codspeed,dask,docs,matplotlib,numpy,optype,pandas,scipy,test,test-all,test-mpl,uncertainties,xarray


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-pint -f %{pyproject_files}
%{_bindir}/pint-convert

%changelog
%autochangelog
