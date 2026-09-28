%global source0_hash 66b07ef7315a31bfe1089cd3d71a7de781c9dca986762d0b4fe7c0ef17465d10
%bcond_with extras

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

%description %_description

%package -n     python3-pandas
Summary:        %{summary}

%description -n python3-pandas %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%if %{with extras}
%pyproject_extras_subpkg -n python3-pandas all,aws,clipboard,compression,computation,excel,feather,fss,gcp,hdf5,html,iceberg,mysql,output-formatting,parquet,performance,plot,postgresql,pyarrow,spss,sql-other,test,timezone,xml
%endif


%prep
%autosetup -p1 -n pandas-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%if %{with extras}
%pyproject_buildrequires -p -x all,aws,clipboard,compression,computation,excel,feather,fss,gcp,hdf5,html,iceberg,mysql,output-formatting,parquet,performance,plot,postgresql,pyarrow,spss,sql-other,test,timezone,xml
%else
%pyproject_buildrequires -p
%endif


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
