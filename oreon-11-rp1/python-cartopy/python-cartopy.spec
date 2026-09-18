%global source0_hash none

Name:           python-cartopy
Version:        0.26.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A Python library for cartographic visualizations with Matplotlib

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/SciTools/cartopy
Source:         %{pypi_source cartopy}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cartopy' generated automatically by pyp2spec.}

Patch:          0001-Reduce-numpy-build-dependency.patch
Patch:          0002-Increase-tolerance-for-new-FreeType.patch

%description %_description

%package -n     python3-cartopy
Summary:        %{summary}

%description -n python3-cartopy %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-cartopy doc,ows,plotting,speedups,srtm,test


%prep
%autosetup -p1 -n cartopy-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x doc,ows,plotting,speedups,srtm,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-cartopy -f %{pyproject_files}
%{_bindir}/cartopy_feature_download

%changelog
%autochangelog
