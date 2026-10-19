%global source0_hash 5ec234651709d92cb13ef085cce01633b23407459f88ccd85c77d4a76c877d2f
Name:           python-pytest-xvfb
Version:        3.1.1
Release:        1%{?dist}
Summary:        A pytest plugin to run Xvfb for tests
License:        MIT
URL:            https://github.com/The-Compiler/pytest-xvfb
Source0:        https://github.com/The-Compiler/pytest-xvfb/archive/v%{version}/pytest-xvfb-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
Requires:       python3-pytest-xvfb = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-xvfb
Summary:        A pytest plugin to run Xvfb for tests
# oreon:reqs
Requires:       python3dist(pytest) >= 2.8.1
Requires:       python3dist(pyvirtualdisplay) >= 1.3
# /oreon:reqs
%description -n python3-pytest-xvfb

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pytest-xvfb-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-xvfb usr/lib/python3*/site-packages/pytest_xvfb* usr/lib64/python3*/site-packages/pytest_xvfb* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_xvfb* usr/lib64/python3*/site-packages/pytest_xvfb* usr/bin/*

%check

%pytest
%files
%files -n python3-pytest-xvfb -f %{oreon_filedir}/python3-pytest-xvfb.list

%changelog

%autochangelog
