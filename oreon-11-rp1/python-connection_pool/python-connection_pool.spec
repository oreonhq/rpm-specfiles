%global source0_hash 3acb9bbd6ef9a6ca9d5e056c0afd14dbc5ca8d610d788b162412f6235a6e3759
Name:           python-connection_pool
Version:        0.0.3
Release:        1%{?dist}
Summary:        Thread-safe connection pool for python
License:        MIT
URL:            https://github.com/zhouyl/ConnectionPool
Source0:        https://github.com/zhouyl/ConnectionPool/archive/%{version}/connection_pool-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
%{summary}.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-connection_pool = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-connection-pool
Summary:        Thread-safe connection pool for python
%py_provides python3-connection_pool
Obsoletes:      python3-connection_pool < 0.0.3-18
%description -n python3-connection-pool %{common_description}

# Upstream provides no tests.

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-connection-pool usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files
%files -n python3-connection-pool -f %{oreon_filedir}/python3-connection-pool.list

%changelog

%autochangelog
