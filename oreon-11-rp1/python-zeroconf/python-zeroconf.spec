%global source0_hash none

Name:           python-zeroconf
Version:        0.151.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A pure python implementation of multicast DNS service discovery

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LGPL-2.1-or-later
URL:            https://github.com/python-zeroconf/python-zeroconf
Source:         %{pypi_source zeroconf}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'zeroconf' generated automatically by pyp2spec.}

Patch:          cython-3.2.patch

%description %_description

%package -n     python3-zeroconf
Summary:        %{summary}

%description -n python3-zeroconf %_description


%prep
%autosetup -p1 -n zeroconf-%{version}


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


%files -n python3-zeroconf -f %{pyproject_files}

%changelog
%autochangelog
