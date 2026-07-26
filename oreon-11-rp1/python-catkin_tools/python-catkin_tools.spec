%global source0_hash 5b6e1867b0e82b7a69b847be170d808074f6b817c44766d261bca55856475647

%global srcname catkin_tools

Name:           python-%{srcname}
Version:        0.9.4
Release:        13%{?dist}
Summary:        Command line tools for working with catkin

License:        Apache-2.0
URL:            http://catkin-tools.readthedocs.org
Source0:        https://github.com/catkin/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
# From https://github.com/catkin/catkin_tools/commit/8ef11ff40514ea9cdb973e4f8486fcc26f5eadcf
Patch0:         %{srcname}-0.9.5-sphinx8.patch
# Maintainers, please upstream
Patch1:         %{name}-rm-python-mock-usage.patch

BuildArch:      noarch

%description
Provides command line tools for working with catkin

%package doc
Summary:        HTML documentation for %{srcname}
BuildRequires:  make
BuildRequires:  python3-rpm-macros
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme

%description doc
HTML documentation for %{srcname}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  cmake
BuildRequires:  python%{python3_pkgversion}-catkin_pkg >= 0.3.0
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-osrf-pycommon >= 0.1.1
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-PyYAML
BuildRequires:  python%{python3_pkgversion}-setuptools
Requires:       cmake
Requires:       make
Conflicts:      python2-%{srcname} < 0.4.4-7
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-catkin_pkg >= 0.3.0
Requires:       python%{python3_pkgversion}-osrf-pycommon >= 0.1.1
Requires:       python%{python3_pkgversion}-PyYAML
Requires:       python%{python3_pkgversion}-setuptools
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Suggests:       %{name}-doc = %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{srcname}
Provides command line tools for working with catkin

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%make_build -C docs html man SPHINXBUILD=sphinx-build-%{python3_version}
rm docs/_build/html/.buildinfo

%install
%py3_install

install -p -m0644 -D docs/_build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1

%check
# Many system tests require catkin itself, which isn't packaged in Fedora
%pytest tests/unit

%files doc
%license LICENSE
%doc docs/_build/html

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_bindir}/catkin
%{_mandir}/man1/%{srcname}.1.*
%{_datadir}/zsh/site-functions/_catkin
%{_datadir}/bash-completion/

%changelog
%autochangelog
