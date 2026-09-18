%global source0_hash none

Name:           python-superqt
Version:        0.8.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Missing widgets and components for PyQt/PySide

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/pyapp-kit/superqt
Source:         %{pypi_source superqt}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'superqt' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-superqt
Summary:        %{summary}

%description -n python3-superqt %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-superqt cmap,font-fa5,font-fa6,font-mi6,font-mi7,iconify,pyqt5,pyqt6,pyside6,quantity


%prep
%autosetup -p1 -n superqt-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x cmap,font-fa5,font-fa6,font-mi6,font-mi7,iconify,pyqt5,pyqt6,pyside6,quantity


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-superqt -f %{pyproject_files}

%changelog
%autochangelog
