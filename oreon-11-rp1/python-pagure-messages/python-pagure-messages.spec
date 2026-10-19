%global source0_hash 5fb04d7d93c7c4eedaf6086f2e1881e8f7d8b4ece66a274e89123fd5a90aa7e2
Name:           python-pagure-messages
Version:        1.3.3
Release:        1%{?dist}
Summary:        A schema package for messages sent by pagure
License:        GPL-2.0-or-later
URL:            https://pagure.io/pagure
Source0:        https://files.pythonhosted.org/packages/source/p/pagure_messages/pagure_messages-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pagure-messages = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pagure-messages
Summary:        A schema package for messages sent by pagure
%description -n python3-pagure-messages

%prep
%global oreon_srcdir pagure_messages-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pagure-messages usr/lib/python3*/site-packages/pagure_messages* usr/lib64/python3*/site-packages/pagure_messages* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pagure_messages* usr/lib64/python3*/site-packages/pagure_messages* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pagure-messages -f %{oreon_filedir}/python3-pagure-messages.list

%changelog

%autochangelog
