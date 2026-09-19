%global source0_hash none

Name:           python-xnat
Version:        0.8.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        An XNAT client that exposes the XNAT REST interface as python objects. Part of the interface is automatically generated based on the servers data model as defined by the xnat schema.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://gitlab.com/radiology/infrastructure/xnatpy
Source:         %{pypi_source xnat}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'xnat' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-xnat
Summary:        %{summary}

%description -n python3-xnat %_description


%prep
%autosetup -p1 -n xnat-%{version}


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


%files -n python3-xnat -f %{pyproject_files}
%{_bindir}/xnat
%{_bindir}/xnat_cp_project
%{_bindir}/xnat_data_integrity-check

%changelog
%autochangelog
