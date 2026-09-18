%global source0_hash none

Name:           python-h2
Version:        4.4.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Pure-Python HTTP/2 protocol implementation

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/python-hyper/h2/
Source:         %{pypi_source h2}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'h2' generated automatically by pyp2spec.}

Patch0:         0001-Fedora-tox-adjustments.patch

%description %_description

%package -n     python3-h2
Summary:        %{summary}

%description -n python3-h2 %_description


%prep
%autosetup -p1 -n h2-%{version}


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


%files -n python3-h2 -f %{pyproject_files}

%changelog
%autochangelog
