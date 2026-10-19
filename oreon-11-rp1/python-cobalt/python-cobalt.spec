%global source0_hash 3a1581f611d9dace7dee35f288e5f3891066a9dd1f5f0881532289fc37f89ea5
%bcond_with bootstrap
Name:           python-cobalt
Version:        9.0.1
Release:        1%{?dist}
Summary:        A lightweight library for working with Akoma Ntoso Act documents
License:        LGPL-3.0-or-later
URL:            https://github.com/laws-africa/cobalt
Source0:        https://files.pythonhosted.org/packages/source/c/cobalt/cobalt-%{version}.tar.gz
BuildArch:      noarch
%if %{without bootstrap}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-cobalt = %{version}-%{release}
# /oreon:deps
%package -n       python3-cobalt+test
Summary:        Metapackage for python3-cobalt test extras
Requires:       python3-cobalt = %{version}-%{release}
Provides:       python3dist(cobalt[test]) = %{version}-%{release}

%description -n python3-cobalt+test
Metapackage for python3-cobalt test extras.

%description

%package -n     python3-cobalt
Summary:        A lightweight library for working with Akoma Ntoso Act documents
# oreon:reqs
Requires:       python3dist(iso8601) >= 0.1
Requires:       python3dist(lxml) >= 3.4.1
# /oreon:reqs
%description -n python3-cobalt

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n cobalt-%{version}
%if %{without bootstrap}
sed -i '/with open("..\/VERSION") as f:/d' docs/conf.py
sed -i '/release = f.read/d' docs/conf.py
SHORTVERSION="$(echo %{version} | cut --delimiter '.'  --complement -f3)"
echo $SHORTVERSION
sed -i "s/version = '.'.join(release.split('.')\[:2\])/version = '${SHORTVERSION}'/g" docs/conf.py
cat docs/conf.py
%endif

%build

%pyproject_wheel
%if %{without bootstrap}
sphinx-build docs texinfo -b texinfo
pushd texinfo
makeinfo --docbook cobalt.texi
popd
%endif
%install
%pyproject_install
%if %{without bootstrap}
mkdir -p %{buildroot}%{_datadir}/help/en/python-cobalt/
install -m 644 texinfo/cobalt.xml %{buildroot}%{_datadir}/help/en/python-cobalt/
%oreon_autofiles python3-cobalt usr/lib/python3*/site-packages/cobalt* usr/lib64/python3*/site-packages/cobalt* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cobalt* usr/lib64/python3*/site-packages/cobalt* usr/bin/*
%endif
%check

%pyproject_check_import
%pytest
%files
%files -n python3-cobalt -f %{oreon_filedir}/python3-cobalt.list

%changelog

%autochangelog
