%global source0_hash df09ddb9e8fac4c433ae31a11974339df26e77f528cb704376eba444979a84bf
Name:           python-mailman-web
Version:        0.0.9
Release:        1%{?dist}
Summary:        Mailman 3 Web interface.
License:        GPL-3.0-or-later
URL:            https://gitlab.com/mailman/mailman-web
Source0:        https://files.pythonhosted.org/packages/source/m/mailman_web/mailman_web-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mailman-web = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mailman-web
Summary:        Mailman 3 Web interface.
# oreon:reqs
Requires:       python3dist(django) < 4.3
Requires:       python3dist(django) >= 4.0
# /oreon:reqs
%description -n python3-mailman-web

%prep
%global oreon_srcdir mailman_web-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mailman-web usr/lib/python3*/site-packages/mailman_web* usr/lib64/python3*/site-packages/mailman_web* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mailman_web* usr/lib64/python3*/site-packages/mailman_web* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mailman-web -f %{oreon_filedir}/python3-mailman-web.list

%changelog

%autochangelog
