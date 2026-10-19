%global source0_hash b18c07212bfead624345bb8e1d6141cdcf15a39736994ea0b94035ad2b1ba177
Name:      python-pathvalidate
Version:   3.3.1
Release:        1%{?dist}
Summary:        Library to sanitize/validate a string such as file-names/file-paths/etc
License:   MIT
URL:       https://github.com/thombashi/pathvalidate
Source0:        https://files.pythonhosted.org/packages/source/p/pathvalidate/pathvalidate-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-pathvalidate = %{version}-%{release}
# /oreon:deps
%description
%{summary}.

%package -n python3-pathvalidate
Summary:        Library to sanitize/validate a string such as file-names/file-paths/etc
%description -n python3-pathvalidate
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pathvalidate-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pathvalidate usr/lib/python3*/site-packages/pathvalidate* usr/lib64/python3*/site-packages/pathvalidate* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pathvalidate* usr/lib64/python3*/site-packages/pathvalidate* usr/bin/*

%check

%pytest -r fEs
%files
%files -n python3-pathvalidate -f %{oreon_filedir}/python3-pathvalidate.list

%changelog

%autochangelog
