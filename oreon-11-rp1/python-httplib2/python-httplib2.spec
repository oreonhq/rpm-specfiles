%global source0_hash none

Name:           python-httplib2
Version:        0.32.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A comprehensive HTTP client library.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/httplib2/httplib2
Source:         %{pypi_source httplib2}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'httplib2' generated automatically by pyp2spec.}

Patch1:         python-%{srcname}.certfile.patch

%description %_description

%package -n     python3-httplib2
Summary:        %{summary}

%description -n python3-httplib2 %_description


%prep
%autosetup -p1 -n httplib2-%{version}


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


%files -n python3-httplib2 -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.22.0-8
- Prepare for Oreon 11 (RP1)
