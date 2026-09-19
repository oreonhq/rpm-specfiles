%global source0_hash none

Name:           python-colored-traceback
Version:        0.4.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Automatically color uncaught exception tracebacks

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ISC
URL:            https://www.github.com/staticshock/colored-traceback.py
Source:         %{pypi_source colored-traceback}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'colored-traceback' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-colored-traceback
Summary:        %{summary}

%description -n python3-colored-traceback %_description


%prep
%autosetup -p1 -n colored-traceback-%{version}


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


%files -n python3-colored-traceback -f %{pyproject_files}

%changelog
%autochangelog
