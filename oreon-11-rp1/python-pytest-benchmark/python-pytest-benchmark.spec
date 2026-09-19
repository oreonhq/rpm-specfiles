%global source0_hash none

Name:           python-pytest-benchmark
Version:        5.3.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A __pytest__ fixture for benchmarking code. It will group the tests into rounds that are calibrated to the chosen timer.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-2-Clause
URL:            https://pytest-benchmark.readthedocs.io/en/latest/changelog.html
Source:         %{pypi_source pytest_benchmark}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pytest-benchmark' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pytest-benchmark
Summary:        %{summary}

%description -n python3-pytest-benchmark %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-pytest-benchmark aspect,elasticsearch,histogram


%prep
%autosetup -p1 -n pytest_benchmark-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x aspect,elasticsearch,histogram


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-pytest-benchmark -f %{pyproject_files}
%{_bindir}/py.test-benchmark
%{_bindir}/pytest-benchmark

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1.0-5
- Prepare for Oreon 11 (RP1)
