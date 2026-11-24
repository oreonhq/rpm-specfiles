# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c7a866fc34ed29a3b10af627a4b9b1dc2433313ca6e959f0ae4feb132047ed72
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond tests 1

%if 0%{?oreon}
%bcond_with bootstrap
%else
%endif

Name:           python-googleapis-common-protos
Version:        1.75.5
Release:        %{autorelease}
Summary:        Common protobufs used in Google APIs

License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python
Source0:        %{pypi_source googleapis-common-protos}
BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel

BuildSystem:    pyproject
BuildOption(install):  -l google
%if %{without bootstrap}
BuildOption(generate_buildrequires): -x grpc
%endif

%if 0%{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global common_description %{expand:
%{summary}.}

%description %{common_description}

%package -n python3-googleapis-common-protos
Summary:        %{summary}

%description -n python3-googleapis-common-protos %{common_description}

%if %{without bootstrap}
%pyproject_extras_subpkg -n python3-googleapis-common-protos grpc
%endif

%check
%if %{with bootstrap}
%pyproject_check_import -e "google.longrunning.operations_grpc*" -e "google.longrunning.operations_pb2_grpc"
%else
%pyproject_check_import
%endif
%if %{with tests}
PYTHONUSERBASE=%{buildroot}%{_prefix} \
    %pytest tests/unit %{?with_bootstrap:--ignore=tests/unit/test_operations.py}
%endif

%files -n python3-googleapis-common-protos -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
