%global source0_hash 4f82fdff0dbe64ef8ab2279bd6aa3f6a99c3b28c05aa09cbfc07c9d7fbb5a463
Name:           python-click-didyoumean
Version:        0.3.1
Release:        1%{?dist}
Summary:        Enables git-like *did-you-mean* feature in click
License:        MIT
URL:            https://github.com/click-contrib/click-didyoumean
Source0:        https://files.pythonhosted.org/packages/source/c/click_didyoumean/click_didyoumean-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-click-didyoumean = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-click-didyoumean
Summary:        Enables git-like *did-you-mean* feature in click
%description -n python3-click-didyoumean

%prep
%global oreon_srcdir click_didyoumean-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-click-didyoumean usr/lib/python3*/site-packages/click_didyoumean* usr/lib64/python3*/site-packages/click_didyoumean* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/click_didyoumean* usr/lib64/python3*/site-packages/click_didyoumean* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-click-didyoumean -f %{oreon_filedir}/python3-click-didyoumean.list

%changelog

%autochangelog
