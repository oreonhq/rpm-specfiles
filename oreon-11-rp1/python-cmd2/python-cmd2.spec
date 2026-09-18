%global source0_hash none

Name:           python-cmd2
Version:        4.2.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        cmd2 - quickly build feature-rich and user-friendly interactive command line applications in Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            ...
Source:         %{pypi_source cmd2}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cmd2' generated automatically by pyp2spec.}

Patch0:           python-cmd2-2.5.11-disable-cov-tests.patch
Patch1:           Add-support-for-Python-3.14-and-remove-for-Python-3.8.patch

%description %_description

%package -n     python3-cmd2
Summary:        %{summary}

%description -n python3-cmd2 %_description


%prep
%autosetup -p1 -n cmd2-%{version}


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


%files -n python3-cmd2 -f %{pyproject_files}

%changelog
%autochangelog
