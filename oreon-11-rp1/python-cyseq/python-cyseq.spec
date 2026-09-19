%global source0_hash none

Name:           python-cyseq
Version:        0.1.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        _A Cython version of ScanCode-toolkit_s licensedcode.seq_

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/aboutcode-org/cyseq
Source:         %{pypi_source cyseq}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cyseq' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-cyseq
Summary:        %{summary}

%description -n python3-cyseq %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-cyseq dev


%prep
%autosetup -p1 -n cyseq-%{version}


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


%files -n python3-cyseq -f %{pyproject_files}

%changelog
%autochangelog
