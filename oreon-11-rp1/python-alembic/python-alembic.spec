%global source0_hash none

Name:           python-alembic
Version:        1.20.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A database migration tool for SQLAlchemy.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://alembic.sqlalchemy.org
Source:         %{pypi_source alembic}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'alembic' generated automatically by pyp2spec.}

Patch:            python-alembic-1.15.2-no-tzdata-pkg.patch

%description %_description

%package -n     python3-alembic
Summary:        %{summary}

%description -n python3-alembic %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-alembic tz


%prep
%autosetup -p1 -n alembic-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x tz


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-alembic -f %{pyproject_files}
%{_bindir}/alembic

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.18.4-1
- Prepare for Oreon 11 (RP1)
