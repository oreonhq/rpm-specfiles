%global source0_hash 57c435ac2c68b108999b6db075d9053e4d7a936ba57b4a3d45667b1346f1738a
Name:           python-googleapis-common-protos
Version:        1.75.3
Release:        1%{?dist}
Summary:        Common protobufs used in Google APIs
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/googleapis-common-protos
Source0:        https://files.pythonhosted.org/packages/source/g/googleapis_common_protos/googleapis_common_protos-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{url}/pull/212.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-googleapis-common-protos = %{version}-%{release}
# /oreon:deps
%package -n       python3-googleapis-common-protos+grpc
Summary:        Metapackage for python3-googleapis-common-protos grpc extras
Requires:       python3-googleapis-common-protos = %{version}-%{release}
Requires:       python3dist(grpcio) >= 1.59.0
Requires:       python3dist(grpcio) < 2.0.0
Provides:       python3dist(googleapis-common-protos[grpc]) = %{version}-%{release}

%description -n python3-googleapis-common-protos+grpc
Metapackage for python3-googleapis-common-protos grpc extras.

%description

%package -n     python3-googleapis-common-protos
Summary:        Common protobufs used in Google APIs
# oreon:reqs
Requires:       python3dist(protobuf) < 8.0.0
Requires:       python3dist(protobuf) >= 6.33.5
# /oreon:reqs
%description -n python3-googleapis-common-protos

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir googleapis_common_protos-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-googleapis-common-protos usr/lib/python3*/site-packages/googleapis_common_protos* usr/lib64/python3*/site-packages/googleapis_common_protos* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/googleapis_common_protos* usr/lib64/python3*/site-packages/googleapis_common_protos* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-googleapis-common-protos -f %{oreon_filedir}/python3-googleapis-common-protos.list

%changelog

%autochangelog
