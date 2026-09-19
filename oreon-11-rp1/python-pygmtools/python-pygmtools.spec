%global source0_hash none

Name:           python-pygmtools
Version:        0.6.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        pygmtools provides graph matching solvers in Python API and supports numpy and pytorch backends. pygmtools also provides dataset API for standard graph matching benchmarks.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MulanPSL-2.0
URL:            https://pygmtools.readthedocs.io/
Source:         %{pypi_source pygmtools}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pygmtools' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pygmtools
Summary:        %{summary}

%description -n python3-pygmtools %_description


%prep
%autosetup -p1 -n pygmtools-%{version}


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


%files -n python3-pygmtools -f %{pyproject_files}

%changelog
%autochangelog
