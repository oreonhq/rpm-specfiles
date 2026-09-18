%global source0_hash none

Name:           python-sqlacodegen
Version:        4.0.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Automatic model code generator for SQLAlchemy

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/agronholm/sqlacodegen
Source:         %{pypi_source sqlacodegen}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sqlacodegen' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-sqlacodegen
Summary:        %{summary}

%description -n python3-sqlacodegen %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-sqlacodegen citext,geoalchemy2,pgvector,sqlmodel


%prep
%autosetup -p1 -n sqlacodegen-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x citext,geoalchemy2,pgvector,sqlmodel


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-sqlacodegen -f %{pyproject_files}
%{_bindir}/sqlacodegen

%changelog
%autochangelog
