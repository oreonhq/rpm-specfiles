%global source0_hash none

Name:           python-mkdocs-autorefs
Version:        1.4.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Automatically link across pages in MkDocs.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ISC
URL:            https://mkdocstrings.github.io/autorefs
Source:         %{pypi_source mkdocs_autorefs}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'mkdocs-autorefs' generated automatically by pyp2spec.}

Patch:          https://github.com/mkdocstrings/autorefs/pull/60.patch
Patch100:       mkdocs_autorefs-revert-license-fields.diff

%description %_description

%package -n     python3-mkdocs-autorefs
Summary:        %{summary}

%description -n python3-mkdocs-autorefs %_description


%prep
%autosetup -p1 -n mkdocs_autorefs-%{version}


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


%files -n python3-mkdocs-autorefs -f %{pyproject_files}

%changelog
%autochangelog
