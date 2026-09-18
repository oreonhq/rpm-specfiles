%global source0_hash none

Name:           python-buildman
Version:        0.0.7
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Buildman build tool for U-Boot

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-2.0-or-later
URL:            https://docs.u-boot.org/en/latest/build/buildman.html
Source:         %{pypi_source buildman}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'buildman' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-buildman
Summary:        %{summary}

%description -n python3-buildman %_description


%prep
%autosetup -p1 -n buildman-%{version}


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


%files -n python3-buildman -f %{pyproject_files}
%{_bindir}/buildman

%changelog
%autochangelog
