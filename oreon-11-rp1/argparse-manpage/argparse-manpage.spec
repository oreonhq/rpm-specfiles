%global source0_hash 1deab76b212ac8753cbb67b9d2d2bc0949bbc338bb1cc3547f0890cb34108b32
%global pip_module_name argparse_manpage
  %bcond_with      pyproject
    %bcond_without python2
    %bcond_with    python3
%bcond_without check
%global sum()   Build manual page from %* ArgumentParser object
%global desc \
Generate manual page an automatic way from ArgumentParser object, so the \
manpage 1:1 corresponds to the automatically generated --help output.  The \
manpage generator needs to known the location of the object, user can \
specify that by (a) the module name or corresponding python filename and \
(b) the object name or the function name which returns the object. \
There is a limited support for (deprecated) optparse objects, too.
Name:           argparse-manpage
Version:        4.7
Release:        1%{?dist}
Summary:        Build manual page from Python ArgumentParser object
BuildArch:      noarch
License:        Apache-2.0
URL:            https://github.com/praiskup/%{name}
Source0:        https://files.pythonhosted.org/packages/source/a/argparse_manpage/argparse_manpage-4.7.tar.gz
%if %{with python2}
%if %{with check}
%endif
%endif
%if %{with python3}
%if %{with check}
%endif
%endif
%if %{with pyproject}
%if %{with check}
%endif
%endif
%if %{with python3} || %{with pyproject}
Requires: python3-%name = %version-%release
%else
Requires: python2-%name = %version-%release
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-argparse-manpage = %{version}-%{release}
# /oreon:deps
%description
%desc

%package -n     python2-%name
Summary:        %{sum Python 2}
Requires:       python2-setuptools
Requires:       python2-toml
%description -n python2-%name
%{desc}

%package -n     python3-%name
Summary:        %{sum Python 3}
%if %{without pyproject}
Requires:       python3-setuptools
%endif
%description -n python3-%name
%{desc}

%if %{with pyproject}
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{pip_module_name}-%{version}

%if %{with pyproject}
%build

%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif
%if %{with pyproject}
%pyproject_wheel
%endif
%install
%if %{with python2}
%py2_install
%endif
%if %{with python3}
%py3_install
%endif
%if %{with pyproject}
%pyproject_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/lib/python3*/site-packages/argparse_manpage* usr/lib64/python3*/site-packages/argparse_manpage* usr/bin/*
%endif
%if %{with check}
%check

export PIP_NO_BUILD_ISOLATION=0
%if %{with python2}
PYTHONPATH=%buildroot%python2_sitearch %__python2 -m pytest -vv
%endif
%if %{with python3}
PYTHONPATH=%buildroot%python3_sitearch %__python3 -m pytest -vv
%endif
%if %{with pyproject}
%pytest -vv
%endif
%endif
%files

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.7-6
- Prepare for Oreon 11 (RP1)
%endif
