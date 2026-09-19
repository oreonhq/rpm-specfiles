%global source0_hash none

Name:           python-unicode-segmentation-rs
Version:        0.3.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Unicode segmentation and width for Python using Rust

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://weblate.org/
Source:         %{pypi_source unicode_segmentation_rs}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'unicode-segmentation-rs' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-unicode-segmentation-rs
Summary:        %{summary}

%description -n python3-unicode-segmentation-rs %_description


%prep
%autosetup -p1 -n unicode_segmentation_rs-%{version}


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


%files -n python3-unicode-segmentation-rs -f %{pyproject_files}

%changelog
%autochangelog
