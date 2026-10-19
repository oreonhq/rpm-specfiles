%global source0_hash 814da89a9a7603b7e4d85c487c7381656fa83632f20065e5ed782ab1dbbb5083
Name:           python-sphinxemoji
Version:        0.3.2
Release:        1%{?dist}
Summary:        Use emoji codes in your Sphinx documentation
License:        BSD-3-Clause
URL:            https://pypi.org/pypi/sphinxemoji
Source0:        https://files.pythonhosted.org/packages/source/s/sphinxemoji/sphinxemoji-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sphinxemoji = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-sphinxemoji
Summary:        Use emoji codes in your Sphinx documentation
BuildRequires:  python3-devel
# oreon:reqs
Requires:       python3dist(sphinx) >= 5.0
# /oreon:reqs
%description -n python3-sphinxemoji

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir sphinxemoji-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinxemoji usr/lib/python3*/site-packages/sphinxemoji* usr/lib64/python3*/site-packages/sphinxemoji* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinxemoji* usr/lib64/python3*/site-packages/sphinxemoji* usr/bin/*

%check

%files
%files -n python3-sphinxemoji -f %{oreon_filedir}/python3-sphinxemoji.list

%changelog

%autochangelog
