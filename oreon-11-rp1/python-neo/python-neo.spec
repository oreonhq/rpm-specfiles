%global source0_hash none

Name:           python-neo
Version:        0.14.5
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Neo is a package for representing electrophysiology data in Python, together with support for reading a wide range of neurophysiology file formats

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://neuralensemble.org/neo
Source:         %{pypi_source neo}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'neo' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-neo
Summary:        %{summary}

%description -n python3-neo %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-neo all,biocam,ced,dev,docs,edf,igorproio,iocache,kwikio,maxwell,med,neomatlabio,neuralynx,nixio,nwb,plexon2,test,tiffio


%prep
%autosetup -p1 -n neo-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,biocam,ced,dev,docs,edf,igorproio,iocache,kwikio,maxwell,med,neomatlabio,neuralynx,nixio,nwb,plexon2,test,tiffio


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-neo -f %{pyproject_files}

%changelog
%autochangelog
