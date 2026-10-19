%global source0_hash 7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3
%bcond tests 1
Name:           python-pluggy
Version:        1.6.0
Release:        1%{?dist}
Summary:        The plugin manager stripped of pytest specific details
License:        MIT
URL:            https://github.com/pytest-dev/pluggy
Source0:        https://files.pythonhosted.org/packages/source/p/pluggy/pluggy-1.6.0.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 65.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 8.0
Requires:       python3-pluggy = %{version}-%{release}
# /oreon:deps
%package -n       python3-pluggy+dev
Summary:        Metapackage for python3-pluggy dev extras
Requires:       python3-pluggy = %{version}-%{release}
Provides:       python3dist(pluggy[dev]) = %{version}-%{release}

%description -n python3-pluggy+dev
Metapackage for python3-pluggy dev extras.

%package -n       python3-pluggy+testing
Summary:        Metapackage for python3-pluggy testing extras
Requires:       python3-pluggy = %{version}-%{release}
Provides:       python3dist(pluggy[testing]) = %{version}-%{release}

%description -n python3-pluggy+testing
Metapackage for python3-pluggy testing extras.

%description

%package -n python3-pluggy
Summary:  %summary
%description -n python3-pluggy

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pluggy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pluggy usr/lib/python3*/site-packages/pluggy* usr/lib64/python3*/site-packages/pluggy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pluggy* usr/lib64/python3*/site-packages/pluggy* usr/bin/*
%if %{with tests}
%check

%pytest
%endif
%files
%files -n python3-pluggy -f %{oreon_filedir}/python3-pluggy.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.0-5
- Prepare for Oreon 11 (RP1)
