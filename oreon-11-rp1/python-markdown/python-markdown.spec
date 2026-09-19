%global source0_hash none

Name:           python-markdown
Version:        3.10.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python implementation of John Gruber_s Markdown.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://Python-Markdown.github.io/
Source:         %{pypi_source markdown}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'markdown' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-markdown
Summary:        %{summary}

%description -n python3-markdown %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-markdown docs,testing


%prep
%autosetup -p1 -n markdown-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,testing


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-markdown -f %{pyproject_files}
%{_bindir}/markdown_py

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.10.2-1
- Prepare for Oreon 11 (RP1)
