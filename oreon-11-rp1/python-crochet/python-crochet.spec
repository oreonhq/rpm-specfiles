%global source0_hash 22d12da1080080ef3494b38a994a43ac5711ef6492e8fe3a08b0e6d148ab9caa
Name:           python-crochet
Version:        2.1.1
Release:        1%{?dist}
Summary:        A library that makes it easier to use Twisted from blocking code
Patch1:         https://github.com/itamarst/crochet/pull/150.patch
License:        MIT
URL:            https://github.com/itamarst/crochet
Source0:        https://github.com/itamarst/crochet/archive/%{version}/crochet-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-crochet = %{version}-%{release}
# /oreon:deps
%description

%package doc
Summary: Documentation for python-crochet
BuildRequires:  make
BuildRequires:  python3-sphinx
%description doc
Documentation for python-crochet.

%package -n python3-crochet
Summary:        Documentation for python-crochet
BuildRequires:  python3-devel
%description -n python3-crochet

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir crochet-%{version}
%oreon_prep
%build

%pyproject_wheel
%make_build -C docs html
rm docs/_build/html/.buildinfo
%install
%pyproject_install
%oreon_autofiles python3-crochet usr/lib/python3*/site-packages/crochet* usr/lib64/python3*/site-packages/crochet* usr/bin/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/lib/python3*/site-packages/crochet* usr/lib64/python3*/site-packages/crochet* usr/bin/*

%check

%{py3_test_envvars} %{python3} -m unittest discover -v crochet.tests
%files
%files -n python-crochet-doc -f %{oreon_filedir}/python-crochet-doc.list
%files -n python3-crochet -f %{oreon_filedir}/python3-crochet.list

%changelog

%autochangelog
