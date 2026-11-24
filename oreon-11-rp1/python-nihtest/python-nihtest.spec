# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash a890cd28e2ce5197d7b67b804c0275dcd6e76f4ba88d8813dddd89799516f626
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global pypi_name nihtest
%global forgeurl https://github.com/nih-at/nihtest
%bcond_without tests

Name:           python-%{pypi_name}
Version:        1.12.0
Release:        %{autorelease}
Summary:        A testing tool for command line utilities
License:        BSD-3-Clause
URL:            https://github.com/nih-at/nihtest
Source0:        https://github.com/nih-at/nihtest/archive/v%{version}/nihtest-%{version}.tar.gz
Patch:          run_tests_using_cmake_and_ctest.patch

BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires:  python3-devel
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  mandoc
%if %{with tests}
BuildRequires:  cmake
%endif

%global _description %{expand:
This is nihtest, a testing tool for command line utilities.

Tests are run in a sandbox directory to guarantee a clean separation of
the test.

It checks that exit code, standard and error outputs are as expected
and compares the files in the sandbox after the run with the expected
results.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
Provides:       nihtest = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{pypi_name} %_description

%prep
%oreon_sha256
%autosetup -p1 -n %{pypi_name}-%{version} -S git

echo -e '\n[tool.setuptools]\npackages = ["nihtest"]\n' >> pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

pushd manpages
make %{?_smp_mflags}
popd

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

mkdir -p %{buildroot}/%{_mandir}/man{1,5}
mv manpages/nihtest.man manpages/nihtest.1
mv manpages/nihtest-case.man manpages/nihtest-case.5
mv manpages/nihtest.conf.man manpages/nihtest.conf.5
cp -a manpages/*.1 %{buildroot}/%{_mandir}/man1
cp -a manpages/*.5 %{buildroot}/%{_mandir}/man5

%check
%pyproject_check_import

%if %{with tests}
  touch check.sh
  echo "PATH=%{buildroot}%{_bindir}:${PATH} PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}:${PYTHONPATH} %{python3} %{buildroot}%{_bindir}/nihtest -v \$1 " >> check.sh
  sed -i 's|${NIHTEST}|bash %{_builddir}/%{pypi_name}-%{version}/check.sh|g' tests/CMakeLists.txt
  sed -i 's|ENVIRONMENT "PATH=${path}"|ENVIRONMENT "PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}:$ENV{PYTHONPATH}"|g' tests/CMakeLists.txt
  echo "PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}" >> tests/nihtest.conf.in
  %cmake
  %cmake_build
  %ctest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.*
%doc manpages/*.html
%{_bindir}/%{pypi_name}
%{_mandir}/man1/%{pypi_name}.1*
%{_mandir}/man5/%{pypi_name}*.5*

%changelog
%autochangelog
