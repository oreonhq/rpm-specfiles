%global source0_hash 478a5cbae4375c42f2e114ea0aafda105b8753b9b8bd1acc09d154a254048002
Name:           python-oslo-log
Version:        8.3.2
Release:        1%{?dist}
Summary:        oslo.log library
License:        Apache-2.0
URL:            https://docs.openstack.org/oslo.log
Source0:        https://files.pythonhosted.org/packages/source/o/oslo_log/oslo_log-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 6.1.1
Requires:       python3-oslo-log = %{version}-%{release}
# /oreon:deps
%package -n       python3-oslo-log+fixtures
Summary:        Metapackage for python3-oslo-log fixtures extras
Requires:       python3-oslo-log = %{version}-%{release}
Requires:       python3dist(fixtures) >= 3.0.0
Provides:       python3dist(oslo-log[fixtures]) = %{version}-%{release}

%description -n python3-oslo-log+fixtures
Metapackage for python3-oslo-log fixtures extras.

%package -n       python3-oslo-log+systemd
Summary:        Metapackage for python3-oslo-log systemd extras
Requires:       python3-oslo-log = %{version}-%{release}
Requires:       python3dist(systemd-python) >= 234
Provides:       python3dist(oslo-log[systemd]) = %{version}-%{release}

%description -n python3-oslo-log+systemd
Metapackage for python3-oslo-log systemd extras.

%description

%package -n     python3-oslo-log
Summary:        oslo.log library
%description -n python3-oslo-log

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir oslo_log-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-oslo-log usr/lib/python3*/site-packages/oslo_log* usr/lib64/python3*/site-packages/oslo_log* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/oslo_log* usr/lib64/python3*/site-packages/oslo_log* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-oslo-log -f %{oreon_filedir}/python3-oslo-log.list

%changelog

%autochangelog
