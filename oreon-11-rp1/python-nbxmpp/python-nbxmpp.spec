%global source0_hash f498e874e32d5be2ae59b3d18cd9eed85f50ef5443326d2756ec7bb6a647f7a4
Name:           python-nbxmpp
Version:        7.4.0
Release:        1%{?dist}
Summary:        XMPP Library
License:        GPL-3.0-or-later
URL:            https://dev.gajim.org/gajim/python-nbxmpp
Source0:        https://files.pythonhosted.org/packages/source/n/nbxmpp/nbxmpp-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 65.0.0
Requires:       python3-nbxmpp = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-nbxmpp
Summary:        XMPP Library
# oreon:reqs
Requires:       python3dist(precis-i18n) >= 1.0.0
Requires:       python3dist(pygobject) >= 3.42.0
# /oreon:reqs
%description -n python3-nbxmpp

%prep
%global oreon_srcdir nbxmpp-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-nbxmpp usr/lib/python3*/site-packages/nbxmpp* usr/lib64/python3*/site-packages/nbxmpp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/nbxmpp* usr/lib64/python3*/site-packages/nbxmpp* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-nbxmpp -f %{oreon_filedir}/python3-nbxmpp.list

%changelog

%autochangelog
