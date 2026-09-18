%global source0_hash none

Name:           python-virtualbmc
Version:        3.3.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Create virtual BMCs for controlling virtual instances via IPMI

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://docs.openstack.org/virtualbmc/latest/
Source:         %{pypi_source virtualbmc}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'virtualbmc' generated automatically by pyp2spec.}

Patch0: %{name}-3.2.0_multiprocess_fork.patch

%description %_description

%package -n     python3-virtualbmc
Summary:        %{summary}

%description -n python3-virtualbmc %_description


%prep
%autosetup -p1 -n virtualbmc-%{version}


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


%files -n python3-virtualbmc -f %{pyproject_files}
%{_bindir}/vbmc
%{_bindir}/vbmcd

%changelog
%autochangelog
