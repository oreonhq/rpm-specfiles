%global source0_hash 6c3ccc5578f93a1bd0051fcba25e92d259620d3d9c9031738570e7d78603e7a3
Name:           python-texext
Version:        0.6.8
Release:        1%{?dist}
Summary:        Sphinx extensions for working with LaTeX math
License:        BSD-2-Clause AND Unlicense
URL:            https://github.com/matthew-brett/texext
VCS:            git:%{url}.git
Source0:        https://files.pythonhosted.org/packages/source/t/texext/texext-%{version}.tar.gz
Patch:          %{name}-remove-six.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-texext = %{version}-%{release}
# /oreon:deps
%description
This package contains Sphinx extensions for working with LaTeX math.

%package -n     python3-texext
Summary:        Sphinx extensions for working with LaTeX math
%description -n python3-texext
This package contains Sphinx extensions for working with LaTeX math.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir texext-%{version}
%oreon_prep
%build

%pyproject_wheel
rst2html --no-datestamp README.rst README.html
%install
%pyproject_install
%oreon_autofiles python3-texext usr/lib/python3*/site-packages/texext* usr/lib64/python3*/site-packages/texext* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/texext* usr/lib64/python3*/site-packages/texext* usr/bin/*

%check

%pytest -v
%files
%files -n python3-texext -f %{oreon_filedir}/python3-texext.list

%changelog

%autochangelog
