%global source0_hash none

Name:           python-myrepos-utils
Version:        0.0.4.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Additional utilities for myrepos

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-2.0-or-later
URL:            https://git.sr.ht/~michel-slm/myrepos-utils
Source:         %{pypi_source myrepos_utils}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'myrepos-utils' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-myrepos-utils
Summary:        %{summary}

%description -n python3-myrepos-utils %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-myrepos-utils dev,release,test


%prep
%autosetup -p1 -n myrepos_utils-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,release,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-myrepos-utils -f %{pyproject_files}
%{_bindir}/mr-utils

%changelog
%autochangelog
