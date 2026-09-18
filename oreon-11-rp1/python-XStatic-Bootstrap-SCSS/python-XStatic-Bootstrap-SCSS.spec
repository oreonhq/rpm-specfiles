%global source0_hash none

Name:           python-xstatic-bootstrap-scss
Version:        3.4.1.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Bootstrap-SCSS 3.4.1 _XStatic packaging standard_

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/twbs/bootstrap-sass
Source:         %{pypi_source xstatic_bootstrap_scss}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'xstatic-bootstrap-scss' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-xstatic-bootstrap-scss
Summary:        %{summary}

%description -n python3-xstatic-bootstrap-scss %_description


%prep
%autosetup -p1 -n xstatic_bootstrap_scss-%{version}


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


%files -n python3-xstatic-bootstrap-scss -f %{pyproject_files}

%changelog
%autochangelog
