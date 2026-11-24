# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ae0ef90b90f6af38b54f1fe6d58662ec33b3cb4b8391958a62416d654231727b
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond tests 1

Name:           python-wcwidth
Version:        0.9.2
Release:        %{autorelease}
Summary:        Measures number of Terminal column cells of wide-character codes

License:        MIT AND HPND-Markus-Kuhn
URL:            https://github.com/jquast/wcwidth
Source0:        wcwidth-%{version}.tar.gz

%description
This API is mainly for Terminal Emulator implementors, or those writing programs
that expect to interpreted by a terminal emulator and wish to determine the
printable width of a string on a Terminal.

%package -n     python3-wcwidth
Summary:        %{summary}
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description -n python3-wcwidth
This API is mainly for Terminal Emulator implementors, or those writing programs
that expect to interpreted by a terminal emulator and wish to determine the
printable width of a string on a Terminal.

%prep
%oreon_sha256
%autosetup -p1 -n wcwidth-%{version}
sed -i -e 's|--cov[^[:space:]]*||g' tox.ini

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l wcwidth

%check
%pyproject_check_import
%if %{with tests}
export PYTHONSAFEPATH=1
%pytest -v --import-mode=importlib tests
%endif
%{py3_test_envvars} %{python3} -c "import wcwidth; assert wcwidth.HAS_C_EXTENSION"

%files -n python3-wcwidth -f %{pyproject_files}
%doc docs/*.rst

%changelog
%autochangelog
