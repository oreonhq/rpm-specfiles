%global source0_hash none

Name:           python-binaryornot
Version:        0.6.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Ultra-lightweight pure Python package to check if a file is binary or text.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/binaryornot/binaryornot
Source:         %{pypi_source binaryornot}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'binaryornot' generated automatically by pyp2spec.}

Patch:              38dee57986c6679d99.patch

%description %_description

%package -n     python3-binaryornot
Summary:        %{summary}

%description -n python3-binaryornot %_description


%prep
%autosetup -p1 -n binaryornot-%{version}


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


%files -n python3-binaryornot -f %{pyproject_files}
%{_bindir}/binaryornot

%changelog
%autochangelog
