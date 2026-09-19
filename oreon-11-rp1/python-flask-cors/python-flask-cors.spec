%global source0_hash none

Name:           python-flask-cors
Version:        6.0.5
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A Flask extension simplifying CORS support

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://corydolphin.github.io/flask-cors/
Source:         %{pypi_source flask_cors}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'flask-cors' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-flask-cors
Summary:        %{summary}

%description -n python3-flask-cors %_description


%prep
%autosetup -p1 -n flask_cors-%{version}


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


%files -n python3-flask-cors -f %{pyproject_files}

%changelog
%autochangelog
