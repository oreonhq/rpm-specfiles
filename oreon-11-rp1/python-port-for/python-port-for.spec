%global source0_hash none

Name:           python-port-for
Version:        1.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Utility that helps with local TCP ports management. It can find an unused TCP localhost port and remember the association.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/fizyk/port-for/
Source:         %{pypi_source port_for}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'port-for' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-port-for
Summary:        %{summary}

%description -n python3-port-for %_description


%prep
%autosetup -p1 -n port_for-%{version}


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


%files -n python3-port-for -f %{pyproject_files}
%{_bindir}/port-for

%changelog
%autochangelog
