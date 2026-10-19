%global source0_hash b1d756fd04d17c291303bf9777da11c052cac795a4d3e82569e250a76c72d28c
Name:           python-repoze-who
Version:        3.2.0
Release:        1%{?dist}
Summary:        Identification and authentication framework for WSGI.
License:        ...
URL:            https://github.com/repoze/repoze.who
Source0:        https://files.pythonhosted.org/packages/source/r/repoze_who/repoze_who-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-repoze-who = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-repoze-who
Summary:        Identification and authentication framework for WSGI.
%description -n python3-repoze-who

%prep
%global oreon_srcdir repoze_who-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-repoze-who usr/lib/python3*/site-packages/repoze_who* usr/lib64/python3*/site-packages/repoze_who* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/repoze_who* usr/lib64/python3*/site-packages/repoze_who* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-repoze-who -f %{oreon_filedir}/python3-repoze-who.list

%changelog

%autochangelog
