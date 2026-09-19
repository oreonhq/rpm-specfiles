%global source0_hash none

Name:           python-esbonio
Version:        2.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A language server for sphinx/docutils based documentation projects.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/swyddfa/esbonio
Source:         %{pypi_source esbonio}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'esbonio' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-esbonio
Summary:        %{summary}

%description -n python3-esbonio %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-esbonio typecheck


%prep
%autosetup -p1 -n esbonio-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x typecheck


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-esbonio -f %{pyproject_files}
%{_bindir}/esbonio

%changelog
%autochangelog
