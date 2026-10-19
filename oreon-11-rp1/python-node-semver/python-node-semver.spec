%global source0_hash f052dbdcbc42dd5a0c04b22829a3af98c1f29e4675cc6d88db24250a3f7f8ec7
Name:           python-node-semver
Version:        0.9.1
Release:        1%{?dist}
Summary:        port of node-semver
License:        mit
URL:            https://github.com/podhmo/python-node-semver
Source0:        https://files.pythonhosted.org/packages/source/n/node_semver/node_semver-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-node-semver = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-node-semver
Summary:        port of node-semver
%description -n python3-node-semver

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir node_semver-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-node-semver usr/lib/python3*/site-packages/node_semver* usr/lib64/python3*/site-packages/node_semver* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/node_semver* usr/lib64/python3*/site-packages/node_semver* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-node-semver -f %{oreon_filedir}/python3-node-semver.list

%changelog

%autochangelog
