%global source0_hash none

Name:           python-cyclopts
Version:        4.25.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Intuitive, easy CLIs based on type hints.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/BrianPugh/cyclopts
Source:         %{pypi_source cyclopts}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cyclopts' generated automatically by pyp2spec.}

Patch:          patch-docs-conf-for-downstream-build.diff
Patch1:         exclude-init-members-from-exception-class.diff

%description %_description

%package -n     python3-cyclopts
Summary:        %{summary}

%description -n python3-cyclopts %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-cyclopts debug,dev,docs,mkdocs,toml,trio,yaml


%prep
%autosetup -p1 -n cyclopts-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x debug,dev,docs,mkdocs,toml,trio,yaml


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-cyclopts -f %{pyproject_files}
%{_bindir}/cyclopts

%changelog
%autochangelog
