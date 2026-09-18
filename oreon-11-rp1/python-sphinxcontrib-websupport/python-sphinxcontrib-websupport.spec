%global source0_hash none

Name:           python-sphinxcontrib-websupport
Version:        2.0.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        sphinxcontrib-websupport provides a Python API to easily integrate Sphinx documentation into your Web application

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://www.sphinx-doc.org/
Source:         %{pypi_source sphinxcontrib_websupport}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sphinxcontrib-websupport' generated automatically by pyp2spec.}

Patch:          https://github.com/sphinx-doc/sphinxcontrib-websupport/pull/91.patch

%description %_description

%package -n     python3-sphinxcontrib-websupport
Summary:        %{summary}

%description -n python3-sphinxcontrib-websupport %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-sphinxcontrib-websupport lint,test,whoosh


%prep
%autosetup -p1 -n sphinxcontrib_websupport-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x lint,test,whoosh


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-sphinxcontrib-websupport -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.7-1
- Prepare for Oreon 11 (RP1)
