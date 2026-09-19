%global source0_hash none

Name:           python-telnetlib3
Version:        5.0.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python Telnet server and client CLI and Protocol library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ISC
URL:            https://github.com/jquast/telnetlib3
Source:         %{pypi_source telnetlib3}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'telnetlib3' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-telnetlib3
Summary:        %{summary}

%description -n python3-telnetlib3 %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-telnetlib3 docs,extras


%prep
%autosetup -p1 -n telnetlib3-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,extras


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-telnetlib3 -f %{pyproject_files}
%{_bindir}/telnetlib3-client
%{_bindir}/telnetlib3-fingerprint
%{_bindir}/telnetlib3-fingerprint-server
%{_bindir}/telnetlib3-server

%changelog
%autochangelog
