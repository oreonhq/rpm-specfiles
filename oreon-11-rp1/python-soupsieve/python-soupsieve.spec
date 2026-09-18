%global source0_hash none

Name:           python-soupsieve
Version:        2.9.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A modern CSS selector implementation for Beautiful Soup.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/facelessuser/soupsieve
Source:         %{pypi_source soupsieve}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'soupsieve' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-soupsieve
Summary:        %{summary}

%description -n python3-soupsieve %_description


%prep
%autosetup -p1 -n soupsieve-%{version}


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


%files -n python3-soupsieve -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.8.3-1
- Prepare for Oreon 11 (RP1)
