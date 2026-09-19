%global source0_hash none

Name:           python-resolvelib
Version:        1.2.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Resolve abstract dependencies into concrete ones

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ISC
URL:            https://github.com/sarugaku/resolvelib
Source:         %{pypi_source resolvelib}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'resolvelib' generated automatically by pyp2spec.}

Patch:        https://github.com/sarugaku/resolvelib/pull/141.patch#/remove-commentjson-dep.patch
Patch:          remove-wheel-dep.patch
Patch:          packaging-26-fix.patch

%description %_description

%package -n     python3-resolvelib
Summary:        %{summary}

%description -n python3-resolvelib %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-resolvelib lint,release,test


%prep
%autosetup -p1 -n resolvelib-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x lint,release,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-resolvelib -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.1-13
- Prepare for Oreon 11 (RP1)
