%global source0_hash cec596316640f2b394b8f0daa0ea61a8eae82d017b620b9f202befb972a59ea4

Name:           python-matplotlib
Version:        3.11.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python plotting package

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        PSF-2.0
URL:            https://matplotlib.org
Source:         %{pypi_source matplotlib}

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(raqm)
BuildRequires:  qhull-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'matplotlib' generated automatically by pyp2spec.}

Patch1001:      0001-matplotlibrc-path-search-fix.patch

%description %_description

%package -n     python3-matplotlib
Summary:        %{summary}

%description -n python3-matplotlib %_description


%prep
%autosetup -p1 -n matplotlib-%{version}


%generate_buildrequires
%pyproject_buildrequires -p


%build
%pyproject_wheel -Csetup-args=-Dsystem-freetype=true -Csetup-args=-Dsystem-libraqm=true -Csetup-args=-Dsystem-qhull=true


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-matplotlib -f %{pyproject_files}

%changelog
%autochangelog
