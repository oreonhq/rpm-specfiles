%global source0_hash e5fb0f3965b86010976488589a45e48e9abb95101f2ddc2b3c31ca86d5261112

%global sum docutils-compatibility bridge to CommonMark
%global desc A docutils-compatibility bridge to CommonMark.\
\
This allows you to write CommonMark inside of Docutils & Sphinx projects.\
\
Documentation is available on Read the Docs: http://recommonmark.readthedocs.org

Name:           python-recommonmark
Version:        0.7.1
Release:        17.git%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/readthedocs/recommonmark
Source0:        https://github.com/readthedocs/recommonmark/archive/%{version}/recommonmark-%{version}.tar.gz
BuildArch:      noarch

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

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
#  install python3 first to have unversioned binaries for python 3
%pyproject_install
%pyproject_save_files recommonmark
pushd %{buildroot}%{_bindir}  # Enter buildroot bindir to ease symlink creation
for cm2bin in cm2*; do
    mv "${cm2bin}" "${cm2bin}-%{python3_version}"
    ln -s "${cm2bin}-%{python3_version}" "${cm2bin}-3"
done
popd  # Leave buildroot bindir

%check
%pyproject_check_import

# Skip some tests because of https://github.com/readthedocs/recommonmark/issues/164
%pytest --ignore tests/test_sphinx.py

%files -n python%{python3_pkgversion}-recommonmark -f %{pyproject_files}
%doc README.md
%license license.md
%{_bindir}/cm2*-3
%{_bindir}/cm2*-%{python3_version}

%changelog
%autochangelog
