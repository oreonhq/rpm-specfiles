# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 393f0d516af101304390da79f702e2a4e03da50d0b0c5bacdb17e81ddc816148
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if 0%{?oreon}
%bcond tests 0
%else
%bcond tests %{undefined rhel}
%endif

Name:           python-fasteners
Version:        0.20
Release:        %{autorelease}
Summary:        A python package that provides useful locks

License:        Apache-2.0
URL:            https://github.com/harlowja/fasteners
Source0:        %{url}/archive/%{version}/fasteners-%{version}.tar.gz

BuildSystem:    pyproject
%if %{with tests}
BuildOption(generate_buildrequires): --dependency-groups test
%endif
BuildOption(install): --assert-license fasteners
BuildOption(check): --exclude 'fasteners.pywin32*'

BuildArch:      noarch

%global common_description %{expand:
Cross platform locks for threads and processes}

%description %{common_description}

%package -n python3-fasteners
Summary:        A python package that provides useful locks

%description -n python3-fasteners %{common_description}

%prep -a
%pyproject_patch_dependency eventlet:ignore

%check -a
%pyproject_verify_license

%if %{with tests}
ignore="${ignore-} --ignore=tests/test_eventlet.py"

%pytest ${ignore-} -rs --verbose
%endif

%files -n python3-fasteners -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md

%changelog
%autochangelog
