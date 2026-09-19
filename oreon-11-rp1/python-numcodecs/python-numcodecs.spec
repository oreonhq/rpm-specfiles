%global source0_hash none

Name:           python-numcodecs
Version:        0.17.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A Python package providing buffer compression and transformation codecs for use in data storage and communication applications.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/zarr-developers/numcodecs
Source:         %{pypi_source numcodecs}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'numcodecs' generated automatically by pyp2spec.}

Patch:          0001-Unbundle-blosc.patch
Patch:          0002-Unbundle-zstd.patch
Patch:          0003-Unbundle-lz4.patch
Patch:          0004-Re-add-Snappy-to-tests.patch
Patch:          0005-Fix-testing-setup-for-Fedora.patch
Patch:          0006-Reduce-numpy-build-requirement.patch

%description %_description

%package -n     python3-numcodecs
Summary:        %{summary}

%description -n python3-numcodecs %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-numcodecs crc32c,docs,google-crc32c,msgpack,pcodec,test,test-extras,zfpy


%prep
%autosetup -p1 -n numcodecs-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x crc32c,docs,google-crc32c,msgpack,pcodec,test,test-extras,zfpy


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-numcodecs -f %{pyproject_files}

%changelog
%autochangelog
