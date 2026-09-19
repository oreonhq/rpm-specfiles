%global source0_hash none

Name:           python-fsspec
Version:        2026.9.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        File-system specification

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/fsspec/filesystem_spec
Source:         %{pypi_source fsspec}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'fsspec' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-fsspec
Summary:        %{summary}

%description -n python3-fsspec %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-fsspec abfs,adl,arrow,dask,dev,doc,dropbox,entrypoints,full,fuse,gcs,git,github,gs,gui,hdfs,http,libarchive,oci,s3,sftp,smb,ssh,test,test-downstream,test-full,tqdm


%prep
%autosetup -p1 -n fsspec-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x abfs,adl,arrow,dask,dev,doc,dropbox,entrypoints,full,fuse,gcs,git,github,gs,gui,hdfs,http,libarchive,oci,s3,sftp,smb,ssh,test,test-downstream,test-full,tqdm


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-fsspec -f %{pyproject_files}

%changelog
%autochangelog
