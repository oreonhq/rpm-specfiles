%global source0_hash 22021caf5867a46fae5ab927bbdcb430599d7e5ee3898449cbbe430ff07b7d08
Name:           python-levenshtein
Version:        0.27.5
Release:        1%{?dist}
Summary:        Python extension for computing string edit distances and similarities.
License:        GPL-2.0-or-later
URL:            https://github.com/rapidfuzz/Levenshtein
Source0:        https://files.pythonhosted.org/packages/source/l/levenshtein/levenshtein-%{version}.tar.gz
Patch0:       levenshtein-0.27.1-cython-cpp.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(scikit-build-core) >= 0.11
Requires:       python3-levenshtein = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-levenshtein
Summary:        Python extension for computing string edit distances and similarities.
# oreon:reqs
Requires:       python3dist(rapidfuzz) < 4.0.0
Requires:       python3dist(rapidfuzz) >= 3.9.0
# /oreon:reqs
%description -n python3-levenshtein

%prep
%global oreon_srcdir levenshtein-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-levenshtein usr/lib/python3*/site-packages/levenshtein* usr/lib64/python3*/site-packages/levenshtein* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/levenshtein* usr/lib64/python3*/site-packages/levenshtein* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-levenshtein -f %{oreon_filedir}/python3-levenshtein.list

%changelog

%autochangelog
