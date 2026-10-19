%global source0_hash 72cb2be14048c0cbc89ccf1b57863013a9977fd51248c300ccc72001e7c43dbb
Name:           python-pywlroots
Version:        0.17.0
Release:        1%{?dist}
Summary:        Python binding to the wlroots library using cffi
License:        NCSA
URL:            https://github.com/flacjacket/pywlroots
Source0:        https://files.pythonhosted.org/packages/source/p/pywlroots/pywlroots-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi) >= 1.12.0
BuildRequires:  python3dist(setuptools) >= 62.4.0
Requires:       python3-pywlroots = %{version}-%{release}
# /oreon:deps
%package -n       python3-pywlroots+test
Summary:        Metapackage for python3-pywlroots test extras
Requires:       python3-pywlroots = %{version}-%{release}
Provides:       python3dist(pywlroots[test]) = %{version}-%{release}

%description -n python3-pywlroots+test
Metapackage for python3-pywlroots test extras.

%package -n       python3-pywlroots+typecheck
Summary:        Metapackage for python3-pywlroots typecheck extras
Requires:       python3-pywlroots = %{version}-%{release}
Provides:       python3dist(pywlroots[typecheck]) = %{version}-%{release}

%description -n python3-pywlroots+typecheck
Metapackage for python3-pywlroots typecheck extras.

%description

%package -n     python3-pywlroots
Summary:        Python binding to the wlroots library using cffi
# oreon:reqs
Requires:       python3dist(cffi) >= 1.12.0
Requires:       python3dist(pywayland) >= 0.4.14
Requires:       python3dist(xkbcommon) >= 0.2
# /oreon:reqs
%description -n python3-pywlroots

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pywlroots-%{version}
%oreon_prep
%build

%pyproject_wheel
python3 wlroots/ffi_build.py
%install
%pyproject_install
%oreon_autofiles python3-pywlroots usr/lib/python3*/site-packages/pywlroots* usr/lib64/python3*/site-packages/pywlroots* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pywlroots* usr/lib64/python3*/site-packages/pywlroots* usr/bin/*

%check

%pyproject_check_import -t
%pytest
%files
%files -n python3-pywlroots -f %{oreon_filedir}/python3-pywlroots.list

%changelog

%autochangelog
