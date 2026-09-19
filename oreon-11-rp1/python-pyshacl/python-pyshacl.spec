%global source0_hash none

Name:           python-pyshacl
Version:        0.40.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python SHACL Validator

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/RDFLib/pySHACL
Source:         %{pypi_source pyshacl}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyshacl' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pyshacl
Summary:        %{summary}

%description -n python3-pyshacl %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-pyshacl dev-coverage,dev-lint,dev-type-checking,http,js,oxigraph


%prep
%autosetup -p1 -n pyshacl-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev-coverage,dev-lint,dev-type-checking,http,js,oxigraph


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-pyshacl -f %{pyproject_files}
%{_bindir}/pyshacl
%{_bindir}/pyshacl_rules
%{_bindir}/pyshacl_server
%{_bindir}/pyshacl_validate

%changelog
%autochangelog
