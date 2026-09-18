%global source0_hash none

Name:           python-pandas
Version:        3.0.6
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Powerful data structures for data analysis, time series, and statistics

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://pandas.pydata.org
Source:         %{pypi_source pandas}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pandas' generated automatically by pyp2spec.}

Patch:          0001-TST-Ensure-Matplotlib-is-always-cleaned-up.patch
Patch:          0003-TST-Fix-IntervalIndex-constructor-tests-on-big-endia.patch
Patch:          0004-TST-Fix-test_str_encode-on-big-endian-machines.patch
Patch:          0005-Use-zoneinfo-instead-of-pytz.patch
Patch:          0006-Adjust-test-to-accomodate-changes-in-Python.patch
Patch:          0007-Replace-deprecated-xarray.cftime_range.patch
Patch:          0008-Fix-Cython-3.2-build.patch
Patch:          0009-TST-numexpr-2.13-bool-arith-warning.patch
Patch:          0010-FIX-mpl-3.10-pandas-userwarnings.patch

%description %_description

%package -n     python3-pandas
Summary:        %{summary}

%description -n python3-pandas %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-pandas all,aws,clipboard,compression,computation,excel,feather,fss,gcp,hdf5,html,iceberg,mysql,output-formatting,parquet,performance,plot,postgresql,pyarrow,spss,sql-other,test,timezone,xml


%prep
%autosetup -p1 -n pandas-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,aws,clipboard,compression,computation,excel,feather,fss,gcp,hdf5,html,iceberg,mysql,output-formatting,parquet,performance,plot,postgresql,pyarrow,spss,sql-other,test,timezone,xml


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-pandas -f %{pyproject_files}

%changelog
%autochangelog
