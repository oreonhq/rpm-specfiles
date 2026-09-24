%global source0_hash none

Name:           python-pymongo
Version:        4.18.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        PyMongo - the Official MongoDB Python driver

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://www.mongodb.org
Source:         %{pypi_source pymongo}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pymongo' generated automatically by pyp2spec.}

Patch0:         pymongo-nonfatal-warnings.patch

%description %_description

%package -n     python3-pymongo
Summary:        %{summary}

%description -n python3-pymongo %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-pymongo aws,docs,encryption,gssapi,ocsp,snappy,test,zstd


%prep
%autosetup -p1 -n pymongo-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x aws,docs,encryption,gssapi,ocsp,snappy,test,zstd


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-pymongo -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.13.2-4
- Prepare for Oreon 11 (RP1)
