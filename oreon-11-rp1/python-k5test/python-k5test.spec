%global source0_hash e152491e6602f6a93b3d533d387bd4590f2476093b6842170ff0b93de64bef30
Name:           python-k5test
Version:        0.10.4
Release:        1%{?dist}
Summary:        Library for testing Python apps in self-contained Kerberos 5 environments
License:        ISC AND HPND-export-US-modify
URL:            https://github.com/pythongssapi/k5test
Source0:        https://files.pythonhosted.org/packages/source/k/k5test/k5test-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
k5test is a library for setting up self-contained Kerberos 5 environments, and
running Python unit tests inside those environments.  It is based on the file
of the same name found alongside the MIT Kerberos 5 unit tests.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 40.6.0
Requires:       python3-k5test = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-k5test
Summary:        Library for testing Python apps in self-contained Kerberos 5 environments
%description -n python3-k5test %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir k5test-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-k5test usr/lib/python3*/site-packages/k5test* usr/lib64/python3*/site-packages/k5test* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/k5test* usr/lib64/python3*/site-packages/k5test* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-k5test -f %{oreon_filedir}/python3-k5test.list

%changelog

%autochangelog
