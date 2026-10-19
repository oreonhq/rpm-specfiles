%global source0_hash 67647e5e9566edcf421166fdf022b3537f818635daa852b289e34604dc6fb33a
Name:           python-opentelemetry-api
Version:        1.44.0
Release:        1%{?dist}
Summary:        OpenTelemetry Python API
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-api
Source0:        https://files.pythonhosted.org/packages/source/o/opentelemetry_api/opentelemetry_api-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-opentelemetry-api = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-opentelemetry-api
Summary:        OpenTelemetry Python API
# oreon:reqs
Requires:       python3dist(typing-extensions) >= 4.5.0
# /oreon:reqs
%description -n python3-opentelemetry-api

%prep
%global oreon_srcdir opentelemetry_api-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-opentelemetry-api usr/lib/python3*/site-packages/opentelemetry_api* usr/lib64/python3*/site-packages/opentelemetry_api* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/opentelemetry_api* usr/lib64/python3*/site-packages/opentelemetry_api* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-opentelemetry-api -f %{oreon_filedir}/python3-opentelemetry-api.list

%changelog

%autochangelog
