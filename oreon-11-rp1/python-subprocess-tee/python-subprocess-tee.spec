%global source0_hash none

Name:           python-subprocess-tee
Version:        0.4.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        subprocess-tee

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pycontribs/subprocess-tee
Source:         %{pypi_source subprocess_tee}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'subprocess-tee' generated automatically by pyp2spec.}

Patch:          0001-Remove-unnecessary-test-deps.patch

%description %_description

%package -n     python3-subprocess-tee
Summary:        %{summary}

%description -n python3-subprocess-tee %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-subprocess-tee docs,test


%prep
%autosetup -p1 -n subprocess_tee-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-subprocess-tee -f %{pyproject_files}

%changelog
%autochangelog
