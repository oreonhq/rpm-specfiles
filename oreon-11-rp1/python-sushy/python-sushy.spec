%global source0_hash none

Name:           python-sushy
Version:        5.13.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Sushy is a small Python library to communicate with Redfish based systems

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://docs.openstack.org/sushy/latest/
Source:         %{pypi_source sushy}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sushy' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-sushy
Summary:        %{summary}

%description -n python3-sushy %_description


%prep
%autosetup -p1 -n sushy-%{version}


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


%files -n python3-sushy -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.2.0-7
- Prepare for Oreon 11 (RP1)
