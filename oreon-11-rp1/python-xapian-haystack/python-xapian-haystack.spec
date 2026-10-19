%global source0_hash db4917cace93ecf3f321b96f974e4f0798936e1f883a2ab17f14112d3bfede0c
Name:           python-xapian-haystack
Version:        4.0.0
Release:        1%{?dist}
Summary:        A Xapian backend for Haystack
License:        GPL-2.0-or-later
URL:            https://github.com/notanumber/xapian-haystack
Source0:        https://files.pythonhosted.org/packages/source/x/xapian_haystack/xapian_haystack-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-xapian-haystack = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-xapian-haystack
Summary:        A Xapian backend for Haystack
# oreon:reqs
Requires:       python3dist(django) >= 4.2
Requires:       python3dist(django-haystack) >= 3.0
Requires:       python3dist(filelock) >= 3.4
# /oreon:reqs
%description -n python3-xapian-haystack

%prep
%global oreon_srcdir xapian_haystack-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xapian-haystack usr/lib/python3*/site-packages/xapian_haystack* usr/lib64/python3*/site-packages/xapian_haystack* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xapian_haystack* usr/lib64/python3*/site-packages/xapian_haystack* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xapian-haystack -f %{oreon_filedir}/python3-xapian-haystack.list

%changelog

%autochangelog
