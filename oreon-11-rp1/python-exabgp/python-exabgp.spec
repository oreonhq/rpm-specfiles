%global source0_hash none

Name:           python-exabgp
Version:        5.0.13
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        BGP swiss army knife

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/Exa-Networks/exabgp
Source:         %{pypi_source exabgp}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'exabgp' generated automatically by pyp2spec.}

Patch0100:      0100-Adjust-python-versions.patch

%description %_description

%package -n     python3-exabgp
Summary:        %{summary}

%description -n python3-exabgp %_description


%prep
%autosetup -p1 -n exabgp-%{version}


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


%files -n python3-exabgp -f %{pyproject_files}
%{_bindir}/exabgp
%{_bindir}/exabgp-cli
%{_bindir}/exabgp-healthcheck

%changelog
%autochangelog
