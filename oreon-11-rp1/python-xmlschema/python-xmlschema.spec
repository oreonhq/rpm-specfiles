%global source0_hash none

Name:           python-xmlschema
Version:        4.3.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        An XML Schema validator and decoder

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/sissaschool/xmlschema
Source:         %{pypi_source xmlschema}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'xmlschema' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-xmlschema
Summary:        %{summary}

%description -n python3-xmlschema %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-xmlschema codegen,dev,docs


%prep
%autosetup -p1 -n xmlschema-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x codegen,dev,docs


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-xmlschema -f %{pyproject_files}
%{_bindir}/xmlschema-json2xml
%{_bindir}/xmlschema-validate
%{_bindir}/xmlschema-xml2json

%changelog
%autochangelog
