%global source0_hash none

Name:           python-reportlab
Version:        5.0.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The Reportlab Toolkit

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://www.reportlab.com/
Source:         %{pypi_source reportlab}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'reportlab' generated automatically by pyp2spec.}

Patch0:         %{name}-fix_python_3.15.patch

%description %_description

%package -n     python3-reportlab
Summary:        %{summary}

%description -n python3-reportlab %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-reportlab accel,bidi,pycairo,shaping


%prep
%autosetup -p1 -n reportlab-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x accel,bidi,pycairo,shaping


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-reportlab -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.4.10-1
- Prepare for Oreon 11 (RP1)
