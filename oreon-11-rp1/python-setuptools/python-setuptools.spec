%global source0_hash none

Name:           python-setuptools
Version:        84.0.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Most extensible Python build backend with support for C/C++ extension modules

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pypa/setuptools
Source:         %{pypi_source setuptools}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'setuptools' generated automatically by pyp2spec.}

Patch:        https://github.com/pypa/setuptools/pull/5194.patch
Patch:        https://github.com/pypa/setuptools/pull/5194.patch
Patch:        https://github.com/pypa/setuptools/pull/5194.patch
Patch:          https://github.com/pypa/setuptools/pull/5194.patch

%description %_description

%package -n     python3-setuptools
Summary:        %{summary}

%description -n python3-setuptools %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-setuptools certs,check,core,cover,doc,enabler,ssl,test,type


%prep
%autosetup -p1 -n setuptools-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x certs,check,core,cover,doc,enabler,ssl,test,type


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-setuptools -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 80.10.2-1
- Prepare for Oreon 11 (RP1)
