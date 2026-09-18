%global source0_hash none

Name:           python-justbases
Version:        0.15.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        conversion of ints and rationals to any base

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LGPL-2.1-or-later
URL:            https://github.com/mulkieran/justbases
Source:         %{pypi_source justbases}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'justbases' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-justbases
Summary:        %{summary}

%description -n python3-justbases %_description


%prep
%autosetup -p1 -n justbases-%{version}


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


%files -n python3-justbases -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.15.2-1
- Prepare for Oreon 11 (RP1)
