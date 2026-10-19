%global source0_hash 3fa3d6d6209efdbdcf88840a2016efa53fa6c1a3e98847e60ded0d91d074216b
Name:           python-oslo-metrics
Version:        0.17.0
Release:        1%{?dist}
Summary:        Oslo Metrics library
License:        Apache-2.0
URL:            https://docs.openstack.org/oslo.metrics
Source0:        https://files.pythonhosted.org/packages/source/o/oslo_metrics/oslo_metrics-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-oslo-metrics = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-oslo-metrics
Summary:        Oslo Metrics library
%description -n python3-oslo-metrics

%prep
%global oreon_srcdir oslo_metrics-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-oslo-metrics usr/lib/python3*/site-packages/oslo_metrics* usr/lib64/python3*/site-packages/oslo_metrics* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/oslo_metrics* usr/lib64/python3*/site-packages/oslo_metrics* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-oslo-metrics -f %{oreon_filedir}/python3-oslo-metrics.list

%changelog

%autochangelog
