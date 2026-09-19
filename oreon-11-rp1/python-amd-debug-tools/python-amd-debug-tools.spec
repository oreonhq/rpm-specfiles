%global source0_hash none

Name:           python-amd-debug-tools
Version:        0.2.21
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        debug tools for AMD systems

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://web.git.kernel.org/pub/scm/linux/kernel/git/superm1/amd-debug-tools.git/
Source:         %{pypi_source amd_debug_tools}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'amd-debug-tools' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-amd-debug-tools
Summary:        %{summary}

%description -n python3-amd-debug-tools %_description


%prep
%autosetup -p1 -n amd_debug_tools-%{version}


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


%files -n python3-amd-debug-tools -f %{pyproject_files}
%{_bindir}/amd-bios
%{_bindir}/amd-pstate
%{_bindir}/amd-s2idle
%{_bindir}/amd-ttm

%changelog
%autochangelog
