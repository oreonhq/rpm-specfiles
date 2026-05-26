%global srcname jinja2

Name:           python-jinja2
Version:        3.1.6
Release:        7%{?dist}
Summary:        General purpose template engine
License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/jinja/
Source0:        https://files.pythonhosted.org/packages/source/j/jinja2/jinja2-3.1.6.tar.gz
# oreon url source checksums begin
%global source0_sha256 0137fb05990d35f1275a587e9aee6d56da821fc83491a0fb838183be43f66d6d
%global source0_file jinja2-3.1.6.tar.gz
# oreon url source checksums end

# Enable building without docs to avoid a circular dependency between this
# and python-sphinx:
%if 0%{?rhel} || 0%{?flatpak}
%bcond_with docs
%else
%bcond_without docs
%endif
# The dependency on trio is undesired on RHEL
%bcond asyncio_tests %{undefined rhel}

BuildArch:      noarch

%global _description %{expand:
Jinja2 is a template engine written in pure Python. It provides a
Django inspired non-XML syntax but supports inline expressions and an
optional sandboxed environment.

If you have any exposure to other text-based template languages, such
as Smarty or Django, you should feel right at home with Jinja2. It's
both designer and developer friendly by sticking to Python's
principles and adding functionality useful for templating
environments.}

%description %_description

%package -n python3-jinja2
Summary:        %{summary}
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

%description -n python3-jinja2 %_description

%pyproject_extras_subpkg -n python3-jinja2 i18n


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/jinja2-3.1.6.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0137fb05990d35f1275a587e9aee6d56da821fc83491a0fb838183be43f66d6d" || { echo "oreon: Source0 SHA256 mismatch for jinja2-3.1.6.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -x i18n


%build
%pyproject_wheel
%if %{with docs}
make -C docs html PYTHONPATH=$(pwd)/src SPHINXBUILD=sphinx-build-3
# remove hidden file
rm -rvf docs/_build/html/.buildinfo
%endif


%install
%pyproject_install
%pyproject_save_files jinja2


%check
# test_elif_deep is flaky for an unknown reason
# https://github.com/pallets/jinja/issues/2079
%pytest tests -k "not test_elif_deep" %{!?with_asyncio_tests:--ignore tests/test_async.py --ignore tests/test_async_filters.py}


%files -n python3-jinja2 -f %{pyproject_files}
%doc README.md
%doc docs/examples
%license LICENSE.txt
%if %{with docs}
%doc docs/_build/html
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.6-7
- Prepare for Oreon 11 (RP1)
