%global source0_hash none

Name:           python-click-man
Version:        0.5.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Generate man pages for click based CLI applications

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/click-contrib/click-man
Source:         %{pypi_source click_man}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'click-man' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-click-man
Summary:        %{summary}

%description -n python3-click-man %_description


%prep
%autosetup -p1 -n click_man-%{version}


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


%files -n python3-click-man -f %{pyproject_files}
%{_bindir}/click-man

%changelog
%autochangelog
