%global source0_hash 07fd3a9fafb586588e771831fbfc8f6597050181d0c3b45e039d18b8fdc1aab5
Name:           python-grpc-google-iam-v1
Version:        0.14.5
Release:        1%{?dist}
Summary:        IAM API client library
License:        ...
URL:            https://github.com/googleapis/google-cloud-python
Source0:        https://files.pythonhosted.org/packages/source/g/grpc_google_iam_v1/grpc_google_iam_v1-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-grpc-google-iam-v1 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-grpc-google-iam-v1
Summary:        IAM API client library
# oreon:reqs
Requires:       python3dist(googleapis-common-protos[grpc]) < 2.0.0
Requires:       python3dist(googleapis-common-protos[grpc]) >= 1.69.2
Requires:       python3dist(grpcio) < 2.0.0
Requires:       python3dist(grpcio) >= 1.59.0
Requires:       python3dist(protobuf) < 8.0.0
Requires:       python3dist(protobuf) >= 6.33.5
# /oreon:reqs
%description -n python3-grpc-google-iam-v1

%prep
%global oreon_srcdir grpc_google_iam_v1-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-grpc-google-iam-v1 usr/lib/python3*/site-packages/grpc_google_iam_v1* usr/lib64/python3*/site-packages/grpc_google_iam_v1* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/grpc_google_iam_v1* usr/lib64/python3*/site-packages/grpc_google_iam_v1* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-grpc-google-iam-v1 -f %{oreon_filedir}/python3-grpc-google-iam-v1.list

%changelog

%autochangelog
