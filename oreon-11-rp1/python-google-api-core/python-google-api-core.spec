%global source0_hash 31e326eafa31b34f1db7a715f50f61dbca7e6e37277762f252ed90e6ce94c246
Name:           python-google-api-core
Version:        2.38.0
Release:        1%{?dist}
Summary:        Google API client core library
License:        ...
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-api-core
Source0:        https://files.pythonhosted.org/packages/source/g/google_api_core/google_api_core-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-google-api-core = %{version}-%{release}
# /oreon:deps
%package -n       python3-google-api-core+async_rest
Summary:        Metapackage for python3-google-api-core async_rest extras
Requires:       python3-google-api-core = %{version}-%{release}
Requires:       python3dist(google-auth[aiohttp]) >= 2.14.1
Requires:       python3dist(google-auth[aiohttp]) < 3.0.0
Requires:       python3dist(aiohttp) >= 3.13.4
Provides:       python3dist(google-api-core[async_rest]) = %{version}-%{release}

%description -n python3-google-api-core+async_rest
Metapackage for python3-google-api-core async_rest extras.

%package -n       python3-google-api-core+grpc
Summary:        Metapackage for python3-google-api-core grpc extras
Requires:       python3-google-api-core = %{version}-%{release}
Requires:       python3dist(grpcio) >= 1.59.0
Requires:       python3dist(grpcio) < 2.0.0
Requires:       python3dist(grpcio) >= 1.75.1
Requires:       python3dist(grpcio-status) >= 1.59.0
Requires:       python3dist(grpcio-status) < 2.0.0
Requires:       python3dist(grpcio-status) >= 1.75.1
Provides:       python3dist(google-api-core[grpc]) = %{version}-%{release}

%description -n python3-google-api-core+grpc
Metapackage for python3-google-api-core grpc extras.

%package -n       python3-google-api-core+tracing
Summary:        Metapackage for python3-google-api-core tracing extras
Requires:       python3-google-api-core = %{version}-%{release}
Requires:       python3dist(opentelemetry-instrumentation-grpc) >= 0.65b0
Requires:       python3dist(opentelemetry-instrumentation-grpc) < 1.0.0
Provides:       python3dist(google-api-core[tracing]) = %{version}-%{release}

%description -n python3-google-api-core+tracing
Metapackage for python3-google-api-core tracing extras.

%package -n       python3-google-api-core+testing
Summary:        Metapackage for python3-google-api-core testing extras
Requires:       python3-google-api-core = %{version}-%{release}
Requires:       python3dist(opentelemetry-sdk) >= 1.44.0
Requires:       python3dist(opentelemetry-sdk) < 2.0.0
Provides:       python3dist(google-api-core[testing]) = %{version}-%{release}

%description -n python3-google-api-core+testing
Metapackage for python3-google-api-core testing extras.

%description

%package -n     python3-google-api-core
Summary:        Google API client core library
# oreon:reqs
Requires:       python3dist(google-auth) < 3.0.0
Requires:       python3dist(google-auth) >= 2.14.1
Requires:       python3dist(googleapis-common-protos) < 2.0.0
Requires:       python3dist(googleapis-common-protos) >= 1.69.2
Requires:       python3dist(opentelemetry-api) < 2.0.0
Requires:       python3dist(opentelemetry-api) >= 1.44.0
Requires:       python3dist(proto-plus) < 2.0.0
Requires:       python3dist(proto-plus) >= 1.26.1
Requires:       python3dist(protobuf) < 8.0.0
Requires:       python3dist(protobuf) >= 6.33.5
Requires:       python3dist(requests) < 3.0.0
Requires:       python3dist(requests) >= 2.33.0
# /oreon:reqs
%description -n python3-google-api-core

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir google_api_core-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-google-api-core usr/lib/python3*/site-packages/google_api_core* usr/lib64/python3*/site-packages/google_api_core* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/google_api_core* usr/lib64/python3*/site-packages/google_api_core* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-google-api-core -f %{oreon_filedir}/python3-google-api-core.list

%changelog

%autochangelog
