%global source0_hash none

Name:           python-xstatic-angular-uuid
Version:        0.0.4.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Angular-UUID 0.0.4 _XStatic packaging standard_

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/munkychop/angular-uuid
Source:         %{pypi_source xstatic_angular_uuid}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'xstatic-angular-uuid' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-xstatic-angular-uuid
Summary:        %{summary}

%description -n python3-xstatic-angular-uuid %_description


%prep
%autosetup -p1 -n xstatic_angular_uuid-%{version}


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


%files -n python3-xstatic-angular-uuid -f %{pyproject_files}

%changelog
%autochangelog
