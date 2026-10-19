%global source0_hash bfc16531d1246dd2558eb9b3a63aa37a9978672b956860dc5426da2343ebf366
Summary:        Python bindings for wc(s)width
Name:           python-cwcwidth
Version:        0.1.12
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/sebastinas/cwcwidth
Source0:        https://files.pythonhosted.org/packages/source/c/cwcwidth/cwcwidth-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.1
BuildRequires:  python3dist(setuptools) >= 43
Requires:       python3-cwcwidth = %{version}-%{release}
# /oreon:deps
%description

%package     -n python3-cwcwidth
Summary:        Python bindings for wc(s)width
%description -n python3-cwcwidth

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir cwcwidth-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cwcwidth usr/lib/python3*/site-packages/cwcwidth* usr/lib64/python3*/site-packages/cwcwidth* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cwcwidth* usr/lib64/python3*/site-packages/cwcwidth* usr/bin/*

%check

%pyproject_check_import
(cd tests ; PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -m unittest -v)
%files
%files -n python3-cwcwidth -f %{oreon_filedir}/python3-cwcwidth.list

%changelog

%autochangelog
