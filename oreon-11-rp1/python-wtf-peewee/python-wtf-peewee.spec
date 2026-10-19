%global source0_hash 830f94a326a5790c1a17b29bc9944b30de97b6cc66e6f9d06895e3ff3a60b211
Name:           python-wtf-peewee
Version:        3.2.1
Release:        1%{?dist}
Summary:        wtforms integration for peewee
License:        ...
URL:            https://github.com/coleifer/wtf-peewee
Source0:        https://files.pythonhosted.org/packages/source/w/wtf_peewee/wtf_peewee-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-wtf-peewee = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-wtf-peewee
Summary:        wtforms integration for peewee
# oreon:reqs
Requires:       python3dist(peewee) >= 3.0.0
Requires:       python3dist(wtforms) >= 3.0
# /oreon:reqs
%description -n python3-wtf-peewee

%prep
%global oreon_srcdir wtf_peewee-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-wtf-peewee usr/lib/python3*/site-packages/wtf_peewee* usr/lib64/python3*/site-packages/wtf_peewee* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/wtf_peewee* usr/lib64/python3*/site-packages/wtf_peewee* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-wtf-peewee -f %{oreon_filedir}/python3-wtf-peewee.list

%changelog

%autochangelog
