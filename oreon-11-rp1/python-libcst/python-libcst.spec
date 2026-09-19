%global source0_hash none

Name:           python-libcst
Version:        1.9.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A concrete syntax tree with AST-like properties for Python 3.0 through 3.15 programs.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/Instagram/LibCST
Source:         %{pypi_source libcst}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'libcst' generated automatically by pyp2spec.}

Patch:          libcst-fix-metadata.diff
Patch:          One-pyyaml-to-rule-them-all.patch

%description %_description

%package -n     python3-libcst
Summary:        %{summary}

%description -n python3-libcst %_description


%prep
%autosetup -p1 -n libcst-%{version}


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


%files -n python3-libcst -f %{pyproject_files}

%changelog
%autochangelog
