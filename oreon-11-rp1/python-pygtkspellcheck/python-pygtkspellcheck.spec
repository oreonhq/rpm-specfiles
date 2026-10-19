%global source0_hash a693defede048360b6b61e7de84f4fc9d6a0421b6d908922ad0513cfd6280ce3
Name:           python-pygtkspellcheck
Version:        5.0.4
Release:        1%{?dist}
Summary:        A simple but quite powerful spellchecking library for GTK written in pure Python.
License:        GPL-3.0-or-later
URL:            https://github.com/koehlma/pygtkspellcheck
Source0:        https://files.pythonhosted.org/packages/source/p/pygtkspellcheck/pygtkspellcheck-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-pygtkspellcheck = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pygtkspellcheck
Summary:        A simple but quite powerful spellchecking library for GTK written in pure Python.
%description -n python3-pygtkspellcheck

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pygtkspellcheck-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pygtkspellcheck usr/lib/python3*/site-packages/pygtkspellcheck* usr/lib64/python3*/site-packages/pygtkspellcheck* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pygtkspellcheck* usr/lib64/python3*/site-packages/pygtkspellcheck* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pygtkspellcheck -f %{oreon_filedir}/python3-pygtkspellcheck.list

%changelog

%autochangelog
