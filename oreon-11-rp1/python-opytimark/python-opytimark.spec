%global source0_hash none

Name:           python-opytimark
Version:        3.0.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python Optimization Benchmarking Functions

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/gugarosa/opytimark
Source:         %{pypi_source opytimark}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'opytimark' generated automatically by pyp2spec.}

Patch:          %{url}/pull/2.patch
Patch:          %{url}/commit/7f5f97e9d042d9b9d9acf1cdcc9738fe99c792c5.patch
Patch:          %{url}/commit/25d9adb743c8483c0f2ae41f56c8872fdd44977f.patch
Patch:          %{url}/pull/4.patch

%description %_description

%package -n     python3-opytimark
Summary:        %{summary}

%description -n python3-opytimark %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-opytimark tests


%prep
%autosetup -p1 -n opytimark-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x tests


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-opytimark -f %{pyproject_files}

%changelog
%autochangelog
