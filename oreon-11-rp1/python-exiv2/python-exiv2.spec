%global source0_hash none

Name:           python-exiv2
Version:        0.19.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python interface to libexiv2

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-3.0-or-later
URL:            https://github.com/jim-easterbrook/python-exiv2
Source:         %{pypi_source exiv2}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'exiv2' generated automatically by pyp2spec.}

Patch:          https://github.com/jim-easterbrook/python-exiv2/commit/fe98ad09ff30f1b6cc5fd5dcc0769f9505c09166.patch
Patch:          https://github.com/jim-easterbrook/python-exiv2/commit/e0a5284620e8d020771bf8c1fa73d6113e662ebf.patch

%description %_description

%package -n     python3-exiv2
Summary:        %{summary}

%description -n python3-exiv2 %_description


%prep
%autosetup -p1 -n exiv2-%{version}


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


%files -n python3-exiv2 -f %{pyproject_files}

%changelog
%autochangelog
