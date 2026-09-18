%global source0_hash none

Name:           python-sphinx
Version:        9.1.0~rc2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python documentation generator

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-2-Clause
URL:            https://www.sphinx-doc.org/
Source:         %{pypi_source sphinx 9.1.0rc2}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sphinx' generated automatically by pyp2spec.}

Patch:        https://github.com/sphinx-doc/sphinx/pull/13883.patch
Patch:      https://github.com/sphinx-doc/sphinx/commit/8962398b761c3d85a.patch
Patch:      https://github.com/sphinx-doc/sphinx/commit/e01e42f5fc738815b.patch
Patch:      https://github.com/sphinx-doc/sphinx/pull/13527.patch
Patch:      https://github.com/sphinx-doc/sphinx/pull/13610.patch

%description %_description

%package -n     python3-sphinx
Summary:        %{summary}

%description -n python3-sphinx %_description


%prep
%autosetup -p1 -n sphinx-9.1.0rc2


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


%files -n python3-sphinx -f %{pyproject_files}
%{_bindir}/sphinx-apidoc
%{_bindir}/sphinx-autogen
%{_bindir}/sphinx-build
%{_bindir}/sphinx-quickstart

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:8.2.3-1
- Import
