%global source0_hash 4e38e32392e4a4780fe15d644bfc7c8514057cfc3861e060b11814ce829c25e4
Name:           python-bracex
Version:        3.0.1
Release:        1%{?dist}
Summary:        Bash style brace expander.
License:        MIT
URL:            https://github.com/facelessuser/bracex
Source0:        https://files.pythonhosted.org/packages/source/b/bracex/bracex-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 0.21.1
Requires:       python3-bracex = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-bracex
Summary:        Bash style brace expander.
%description -n python3-bracex

%prep
%global oreon_srcdir bracex-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-bracex usr/lib/python3*/site-packages/bracex* usr/lib64/python3*/site-packages/bracex* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/bracex* usr/lib64/python3*/site-packages/bracex* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-bracex -f %{oreon_filedir}/python3-bracex.list

%changelog

%autochangelog
