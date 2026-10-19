%global source0_hash 0137fb05990d35f1275a587e9aee6d56da821fc83491a0fb838183be43f66d6d
%global srcname jinja2
Name:           python-jinja2
Version:        3.1.6
Release:        1%{?dist}
Summary:        General purpose template engine
License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/jinja/
Source0:        https://files.pythonhosted.org/packages/source/j/jinja2/jinja2-3.1.6.tar.gz
%bcond_without docs
%bcond asyncio_tests %{undefined rhel}
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
Requires:       python3-jinja2 = %{version}-%{release}
# /oreon:deps
%package -n       python3-jinja2+i18n
Summary:        Metapackage for python3-jinja2 i18n extras
Requires:       python3-jinja2 = %{version}-%{release}
Requires:       python3dist(babel) >= 2.7
Provides:       python3dist(jinja2[i18n]) = %{version}-%{release}

%description -n python3-jinja2+i18n
Metapackage for python3-jinja2 i18n extras.

%description

%package -n python3-jinja2
Summary:        General purpose template engine
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%if %{with asyncio_tests}
BuildRequires:  python3-trio
%endif
%if %{with docs}
BuildRequires:  %{_bindir}/sphinx-build-3
BuildRequires:  make
BuildRequires:  python3-Pallets-Sphinx-Themes >= 2
BuildRequires:  python3-sphinxcontrib-log-cabinet
BuildRequires:  python3-sphinx-issues
%endif
# oreon:reqs
Requires:       python3dist(markupsafe) >= 2.0
# /oreon:reqs
%description -n python3-jinja2

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{srcname}-%{version}

%build

%pyproject_wheel
%if %{with docs}
make -C docs html PYTHONPATH=$(pwd)/src SPHINXBUILD=sphinx-build-3
rm -rvf docs/_build/html/.buildinfo
%endif
%install
%pyproject_install
%oreon_autofiles python3-jinja2 usr/lib/python3*/site-packages/jinja2* usr/lib64/python3*/site-packages/jinja2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jinja2* usr/lib64/python3*/site-packages/jinja2* usr/bin/*

%check

%pytest tests -k "not test_elif_deep" %{!?with_asyncio_tests:--ignore tests/test_async.py --ignore tests/test_async_filters.py}
%files
%files -n python3-jinja2 -f %{oreon_filedir}/python3-jinja2.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.6-7
- Prepare for Oreon 11 (RP1)
