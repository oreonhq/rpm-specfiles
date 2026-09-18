%global source0_hash none

Name:           python-numpoly
Version:        1.3.9
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Polynomials as a numpy datatype

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-2-Clause
URL:            https://pypi.org/project/numpoly/
Source:         %{pypi_source numpoly}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'numpoly' generated automatically by pyp2spec.}

Patch:      %{forgeurl}/pull/127.patch

%description %_description

%package -n     python3-numpoly
Summary:        %{summary}

%description -n python3-numpoly %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-numpoly dev


%prep
%autosetup -p1 -n numpoly-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-numpoly -f %{pyproject_files}

%changelog
%autochangelog
