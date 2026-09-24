%global source0_hash none

Name:           python-wcwidth
Version:        0.9.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Measures the displayed width of unicode strings in a terminal

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/jquast/wcwidth
Source:         %{pypi_source wcwidth}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'wcwidth' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-wcwidth
Summary:        %{summary}

%description -n python3-wcwidth %_description


%prep
%autosetup -p1 -n wcwidth-%{version}


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


%files -n python3-wcwidth -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.0-1
- Prepare for Oreon 11 (RP1)
