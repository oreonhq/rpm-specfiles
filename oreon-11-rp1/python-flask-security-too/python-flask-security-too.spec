%global source0_hash none

Name:           python-flask-security-too
Version:        5.8.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Quickly add security features to your Flask application.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pallets-eco/flask-security
Source:         %{pypi_source flask_security_too}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'flask-security-too' generated automatically by pyp2spec.}

Patch0:         python-flask-security-too_testdeps.patch
Patch1:         python-flask-security-too_phonenumbers.patch
Patch2:         python-flask-security-too_no-sqla-utils.patch
Patch3:         python-flask-security-too_flask-sqla.patch
Patch4:         python-flask-security-too_no-libpass.patch

%description %_description

%package -n     python3-flask-security-too
Summary:        %{summary}

%description -n python3-flask-security-too %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-flask-security-too babel,common,fsqla,low,mfa


%prep
%autosetup -p1 -n flask_security_too-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x babel,common,fsqla,low,mfa


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-flask-security-too -f %{pyproject_files}

%changelog
%autochangelog
