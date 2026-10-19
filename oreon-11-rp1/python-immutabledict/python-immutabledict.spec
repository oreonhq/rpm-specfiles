%global source0_hash f844a669106cfdc73f47b1a9da003782fb17dc955a54c80972e0d93d1c63c514
Name:           python-immutabledict
Version:        4.3.1
Release:        1%{?dist}
Summary:        Immutable wrapper around dictionaries _a fork of frozendict_
License:        MIT
URL:            https://github.com/corenting/immutabledict
Source0:        https://files.pythonhosted.org/packages/source/i/immutabledict/immutabledict-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 2.0.0
Requires:       python3-immutabledict = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-immutabledict
Summary:        Immutable wrapper around dictionaries _a fork of frozendict_
%description -n python3-immutabledict

%prep
%global oreon_srcdir immutabledict-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-immutabledict usr/lib/python3*/site-packages/immutabledict* usr/lib64/python3*/site-packages/immutabledict* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/immutabledict* usr/lib64/python3*/site-packages/immutabledict* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-immutabledict -f %{oreon_filedir}/python3-immutabledict.list

%changelog

%autochangelog
