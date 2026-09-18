%global source0_hash none

Name:           python-nh3
Version:        0.3.7
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python binding to Ammonia HTML sanitizer Rust crate

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/messense/nh3
Source:         %{pypi_source nh3}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'nh3' generated automatically by pyp2spec.}

Patch:          generate-import-lib-dep.patch

%description %_description

%package -n     python3-nh3
Summary:        %{summary}

%description -n python3-nh3 %_description


%prep
%autosetup -p1 -n nh3-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-nh3 -f %{pyproject_files}

%changelog
%autochangelog
