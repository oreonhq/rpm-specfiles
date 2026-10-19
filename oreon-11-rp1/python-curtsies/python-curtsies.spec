%global source0_hash 102a0ffbf952124f1be222fd6989da4ec7cce04e49f613009e5f54ad37618825
Summary:        Curses-like terminal wrapper, with colored strings
Name:          python-curtsies
Version:       0.4.3
Release:        1%{?dist}
License:       MIT
URL:           https://github.com/bpython/curtsies
Source0:        https://files.pythonhosted.org/packages/source/c/curtsies/curtsies-%{version}.tar.gz
BuildArch:     noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 46.4.0
Requires:       python3-curtsies = %{version}-%{release}
# /oreon:deps
%description

%package     -n python3-curtsies
Summary:        %summary
Requires:       python3-blessings >= 1.5
Requires:       python3-cwcwidth
%description -n python3-curtsies

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir curtsies-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-curtsies usr/lib/python3*/site-packages/curtsies* usr/lib64/python3*/site-packages/curtsies* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/curtsies* usr/lib64/python3*/site-packages/curtsies* usr/bin/*

%check

%pytest
%files
%files -n python3-curtsies -f %{oreon_filedir}/python3-curtsies.list

%changelog

%autochangelog
