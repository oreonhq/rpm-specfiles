%global source0_hash none

Name:           python-falcon
Version:        4.3.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The ultra-reliable, fast ASGI+WSGI framework for building data plane APIs at scale.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://falconframework.org
Source:         %{pypi_source falcon}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'falcon' generated automatically by pyp2spec.}

Patch:          0001-Remove-coverage-test-requirement.patch

%description %_description

%package -n     python3-falcon
Summary:        %{summary}

%description -n python3-falcon %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-falcon test


%prep
%autosetup -p1 -n falcon-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-falcon -f %{pyproject_files}
%{_bindir}/falcon-bench
%{_bindir}/falcon-inspect-app
%{_bindir}/falcon-print-routes

%changelog
%autochangelog
