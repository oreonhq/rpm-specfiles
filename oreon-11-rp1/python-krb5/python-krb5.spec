%global source0_hash none

Name:           python-krb5
Version:        0.10.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Kerberos API bindings for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/jborean93/pykrb5
Source:         %{pypi_source krb5}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'krb5' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-krb5
Summary:        %{summary}

%description -n python3-krb5 %_description


%prep
%autosetup -p1 -n krb5-%{version}


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


%files -n python3-krb5 -f %{pyproject_files}

%changelog
%autochangelog
