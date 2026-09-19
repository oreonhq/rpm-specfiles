%global source0_hash none

Name:           python-hacking
Version:        8.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        OpenStack Hacking Guideline Enforcement

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://docs.openstack.org/hacking/latest
Source:         %{pypi_source hacking}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'hacking' generated automatically by pyp2spec.}

Patch1:         test-requirements.txt.patch

%description %_description

%package -n     python3-hacking
Summary:        %{summary}

%description -n python3-hacking %_description


%prep
%autosetup -p1 -n hacking-%{version}


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


%files -n python3-hacking -f %{pyproject_files}

%changelog
%autochangelog
