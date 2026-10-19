%global source0_hash b86885dcf294e15204919950f666e06ffc6c7c114ca900b060d6e16293528294
Name:           python-wsproto
Version:        1.3.2
Release:        1%{?dist}
Summary:        Pure-Python WebSocket protocol implementation
License:        MIT
URL:            https://github.com/python-hyper/wsproto/
Source0:        https://files.pythonhosted.org/packages/source/w/wsproto/wsproto-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-wsproto = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-wsproto
Summary:        Pure-Python WebSocket protocol implementation
# oreon:reqs
Requires:       python3dist(h11) < 1
Requires:       python3dist(h11) >= 0.16.0
# /oreon:reqs
%description -n python3-wsproto

%prep
%global oreon_srcdir wsproto-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-wsproto usr/lib/python3*/site-packages/wsproto* usr/lib64/python3*/site-packages/wsproto* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/wsproto* usr/lib64/python3*/site-packages/wsproto* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-wsproto -f %{oreon_filedir}/python3-wsproto.list

%changelog

%autochangelog
