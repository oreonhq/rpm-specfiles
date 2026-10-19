%global source0_hash 5b9a9dcf7aa82465e31bd667f5cb7000604811dce83554f1c8a43693a32cb303
Name:           python-mimeparse
Version:        2.0.0
Release:        1%{?dist}
Summary:        Python module for parsing mime-type names
License:        MIT
URL:            https://github.com/falconry/python-mimeparse
Source0:        https://files.pythonhosted.org/packages/source/p/python_mimeparse/python_mimeparse-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
This module provides basic functions for handling mime-types.  It can handle
matching mime-types against a list of media-ranges.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 47
BuildRequires:  python3dist(wheel) >= 0.34
Requires:       python3-mimeparse = %{version}-%{release}
# /oreon:deps
%package -n       python3-mimeparse+test
Summary:        Metapackage for python3-mimeparse test extras
Requires:       python3-mimeparse = %{version}-%{release}
Provides:       python3dist(mimeparse[test]) = %{version}-%{release}

%description -n python3-mimeparse+test
Metapackage for python3-mimeparse test extras.

%description %{common_description}

%package -n python3-mimeparse
Summary:        Python module for parsing mime-type names
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%description -n python3-mimeparse %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir python_mimeparse-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mimeparse usr/lib/python3*/site-packages/mimeparse* usr/lib64/python3*/site-packages/mimeparse* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mimeparse* usr/lib64/python3*/site-packages/mimeparse* usr/bin/*

%check

%pytest
%files
%files -n python3-mimeparse -f %{oreon_filedir}/python3-mimeparse.list

%changelog

%autochangelog
