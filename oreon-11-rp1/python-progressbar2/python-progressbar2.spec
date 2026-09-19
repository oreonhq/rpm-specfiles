%global source0_hash none

Name:           python-progressbar2
Version:        4.6.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A Python Progressbar library to provide visual _yet text based_ progress to long running operations.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/wolph/python-progressbar/
Source:         %{pypi_source progressbar2}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'progressbar2' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-progressbar2
Summary:        %{summary}

%description -n python3-progressbar2 %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-progressbar2 docs,docs-tests,fast,tests


%prep
%autosetup -p1 -n progressbar2-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,docs-tests,fast,tests


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-progressbar2 -f %{pyproject_files}
%{_bindir}/progressbar

%changelog
%autochangelog
