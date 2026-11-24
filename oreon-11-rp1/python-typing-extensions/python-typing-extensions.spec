# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash dc983d19a509c94dba722ee6abd33940f7c05a89e243c47e907eb4db6f1a43e5
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           python-typing-extensions
Version:        4.16.0
Release:        1%{?dist}
Summary:        Backported and Experimental Type Hints for Python

License:        PSF-2.0
URL:            https://pypi.org/project/typing-extensions/
Source0:        %{pypi_source typing_extensions}

Patch:          https://github.com/python/typing_extensions/commit/79c903c7d9ec4cfa30b7ca38a795adc1c100b45a.patch
Patch:          https://github.com/python/typing_extensions/commit/a2024556ab75799fbd2f41d1c2d114dd6372de12.patch

BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-test

%global _description %{expand:
The typing_extensions module serves two related purposes:

- Enable use of new type system features on older Python versions. For example,
  typing.TypeGuard is new in Python 3.10, but typing_extensions allows users on
  previous Python versions to use it too.

- Enable experimentation with new type system PEPs before they are accepted and
  added to the typing module.

typing_extensions is treated specially by static type checkers such as mypy and
pyright. Objects defined in typing_extensions are treated the same way as
equivalent forms in typing.}

%description %_description

%package -n python3-typing-extensions
Summary:       %{summary}

%description -n python3-typing-extensions %_description

%prep
%oreon_sha256
%autosetup -p1 -n typing_extensions-%{version}

%pyproject_patch_dependency flit_core:set_upper:5

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l typing_extensions

%check
cd src
%{py3_test_envvars} %{python3} -m unittest discover

%files -n python3-typing-extensions -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md

%changelog
%autochangelog
