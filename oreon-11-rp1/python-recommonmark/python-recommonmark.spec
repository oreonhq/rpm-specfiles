%global source0_hash e5fb0f3965b86010976488589a45e48e9abb95101f2ddc2b3c31ca86d5261112
%global sum docutils-compatibility bridge to CommonMark
%global desc A docutils-compatibility bridge to CommonMark.\
\
This allows you to write CommonMark inside of Docutils & Sphinx projects.\
\
Documentation is available on Read the Docs: http://recommonmark.readthedocs.org
Name:           python-recommonmark
Version:        0.7.1
Release:        1%{?dist}
Summary:        docutils-compatibility bridge to CommonMark
License:        MIT
URL:            https://github.com/readthedocs/recommonmark
Source0:        https://github.com/readthedocs/recommonmark/archive/%{version}/recommonmark-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-recommonmark = %{version}-%{release}
# /oreon:deps
%description
%{desc}

%package -n     python%{python3_pkgversion}-recommonmark
Summary:        %{sum}
BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-docutils
BuildRequires:  python%{python3_pkgversion}-CommonMark
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-sphinx
%description -n python%{python3_pkgversion}-recommonmark
%{desc}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn recommonmark-%{version}
# Remove upstream's egg-info

sed -i '1{\@^#!/usr/bin/env python@d}' recommonmark/scripts.py

%build

%pyproject_wheel
%install
%pyproject_install
pushd %{buildroot}%{_bindir}  # Enter buildroot bindir to ease symlink creation
for cm2bin in cm2*; do
    mv "${cm2bin}" "${cm2bin}-%{python3_version}"
    ln -s "${cm2bin}-%{python3_version}" "${cm2bin}-3"
done
popd  # Leave buildroot bindir
%oreon_autofiles main usr/lib/python3*/site-packages/recommonmark* usr/lib64/python3*/site-packages/recommonmark* usr/bin/*

%check

%pyproject_check_import
%pytest --ignore tests/test_sphinx.py
%files
%files -n python3-recommonmark -f %{oreon_filedir}/python3-recommonmark.list

%changelog

%autochangelog
