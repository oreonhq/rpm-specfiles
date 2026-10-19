%global source0_hash 14126ed1706a9c6638c81c3f3d915357f7ab0c0245c464a611eb5903811ee45b
Name:           python-roundrobin
Version:        0.1.0
Release:        1%{?dist}
Summary:        Collection of roundrobin utilities
License:        MIT
URL:            https://github.com/linnik/roundrobin
Source0:        https://files.pythonhosted.org/packages/source/r/roundrobin/roundrobin-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-roundrobin = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-roundrobin
Summary:        Collection of roundrobin utilities
%description -n python3-roundrobin

%prep
%global oreon_srcdir roundrobin-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-roundrobin usr/lib/python3*/site-packages/roundrobin* usr/lib64/python3*/site-packages/roundrobin* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/roundrobin* usr/lib64/python3*/site-packages/roundrobin* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-roundrobin -f %{oreon_filedir}/python3-roundrobin.list

%changelog

%autochangelog
