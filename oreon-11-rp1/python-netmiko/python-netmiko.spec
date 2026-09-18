%global source0_hash none

Name:           python-netmiko
Version:        4.7.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Multi-vendor library to simplify legacy CLI connections to network devices

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/ktbyers/netmiko
Source:         %{pypi_source netmiko}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'netmiko' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-netmiko
Summary:        %{summary}

%description -n python3-netmiko %_description


%prep
%autosetup -p1 -n netmiko-%{version}


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


%files -n python3-netmiko -f %{pyproject_files}
%{_bindir}/netmiko-bulk-encrypt
%{_bindir}/netmiko-cfg
%{_bindir}/netmiko-encrypt
%{_bindir}/netmiko-grep
%{_bindir}/netmiko-show

%changelog
%autochangelog
