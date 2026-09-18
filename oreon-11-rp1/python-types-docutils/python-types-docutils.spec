%global source0_hash none

Name:           python-types-docutils
Version:        0.23.0.20260917
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Typing stubs for docutils

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source:         %{pypi_source types_docutils}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'types-docutils' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-types-docutils
Summary:        %{summary}

%description -n python3-types-docutils %_description


%prep
%autosetup -p1 -n types_docutils-%{version}


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


%files -n python3-types-docutils -f %{pyproject_files}

%changelog
%autochangelog
