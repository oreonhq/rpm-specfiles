%global source0_hash none

Name:           python-fixit
Version:        2.2.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A lint framework that writes better Python code for you.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/Instagram/Fixit
Source:         %{pypi_source fixit}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'fixit' generated automatically by pyp2spec.}

Patch:          %{name}-pregenerate_version.diff
Patch:          %{name}-rm-unused-inventories.diff

%description %_description

%package -n     python3-fixit
Summary:        %{summary}

%description -n python3-fixit %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-fixit dev,docs,lsp,pretty


%prep
%autosetup -p1 -n fixit-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,docs,lsp,pretty


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-fixit -f %{pyproject_files}
%{_bindir}/fixit

%changelog
%autochangelog
