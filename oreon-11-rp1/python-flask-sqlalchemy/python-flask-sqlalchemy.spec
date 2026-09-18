%global source0_hash none

Name:           python-flask-sqlalchemy
Version:        3.1.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Add SQLAlchemy support to your Flask application.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/pallets-eco/flask-sqlalchemy/
Source:         %{pypi_source flask_sqlalchemy}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'flask-sqlalchemy' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-flask-sqlalchemy
Summary:        %{summary}

%description -n python3-flask-sqlalchemy %_description


%prep
%autosetup -p1 -n flask_sqlalchemy-%{version}


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


%files -n python3-flask-sqlalchemy -f %{pyproject_files}

%changelog
%autochangelog
