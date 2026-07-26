%global source0_hash 2cdd67f8746e048f00df47a2880f4d6acbcdb399031b604e34ba8f71d5787680

%global pypi_name blessed
%global summary A thin, practical wrapper around terminal capabilities in Python
%global _description \
Blessed is a thin, practical wrapper around terminal styling, screen \
positioning, and keyboard input. \
\
It provides: \
- Styles, color, and maybe a little positioning without necessarily clearing \
  the whole screen first. \
- Works great with standard Python string formatting. \
- Provides up-to-the-moment terminal height and width, so you can respond \
  to terminal size changes. \
- Avoids making a mess if the output gets piped to a non-terminal: outputs \
  to any file-like object such as StringIO, files, or pipes. \
- Uses the terminfo(5) database so it works with any terminal type and \
  supports any terminal capability: No more C-like calls to tigetstr and \
  tparm. \
- Keeps a minimum of internal state, so you can feel free to mix and match \
  with calls to curses or whatever other terminal libraries you like. \
- Provides plenty of context managers to safely express terminal modes, \
  automatically restoring the terminal to a safe state on exit. \
- Act intelligently when somebody redirects your output to a file, omitting \
  all of the terminal sequences such as styling, colors, or positioning. \
- Dead-simple keyboard handling: safely decoding unicode input in your \
  system’s preferred locale and supports application/arrow keys. \
- Allows the printable length of strings containing sequences to be \
  determined.

%bcond_without python3

# Disable dependency generator until it has test code
%{?python_disable_dependency_generator}

# Drop Python 2 with Fedora 30 and EL8
%if (0%{?fedora} && 0%{?fedora} < 30) || (0%{?rhel} && 0%{?rhel} < 8)
  %bcond_without python2
%else
  %bcond_with python2
%endif

Name:       python-%{pypi_name}
Version:    1.20.0
Release:    8%{?dist}
Summary:    %{summary}

License:    MIT
URL:        https://github.com/jquast/blessed
Source0:    %{pypi_source}
BuildArch:      noarch

%if 0%{?el7}
Patch0:     el7_req_fixes.patch
Patch1:     el7_pytest_fixes.patch
%endif

%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-six
BuildRequires:  python2-wcwidth
BuildRequires:  python2-mock
BuildRequires:  python2-pytest
BuildRequires:  python2-backports-functools_lru_cache
%endif

%if %{with python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-wcwidth
BuildRequires:  python%{python3_pkgversion}-pytest
%endif

%if 0%{?with_python3_other}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
BuildRequires:  python%{python3_other_pkgversion}-six
BuildRequires:  python%{python3_other_pkgversion}-wcwidth
BuildRequires:  python%{python3_other_pkgversion}-pytest
%endif

%description %{_description}

# Python 2 package
%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2-six
Requires:       python2-wcwidth
Requires:       python2-backports-functools_lru_cache

%description -n python2-%{pypi_name} %{_description}
%endif

# Python 3 package
%if %{with python3}
%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}-wcwidth

%description -n python%{python3_pkgversion}-%{pypi_name} %{_description}
%endif

# Python 3 other package
%if 0%{?with_python3_other}
%package -n     python%{python3_other_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{pypi_name}}

Requires:       python%{python3_other_pkgversion}-six
Requires:       python%{python3_other_pkgversion}-wcwidth

%description -n python%{python3_other_pkgversion}-%{pypi_name} %{_description}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%py3_build
%endif

%if 0%{?with_python3_other}
%py3_other_build
%endif

%install
%if 0%{?with_python3_other}
%py3_other_install
%endif

%if %{with python3}
%py3_install
%endif

%if %{with python2}
%py2_install
%endif

%check
export PYTHONIOENCODING=UTF8
export TERM=xterm-256color
%if %{with python2}
# Skip test that uses pytest.warn, since it's not supported in older versions
%{__python2} -m pytest --strict --verbose --verbose --exitfirst -c /dev/null \
-k 'not test_unknown_preferredencoding_warned_and_fallback_ascii'
%endif

%if %{with python3}
%{__python3} -m pytest --strict --verbose --verbose --exitfirst -c /dev/null
%endif

%if 0%{?with_python3_other}
%{__python3_other} -m pytest --strict --verbose --verbose --exitfirst -c /dev/null
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst docs/*.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-*.egg-info
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst docs/*.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*.egg-info
%endif

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst docs/*.rst
%{python3_other_sitelib}/%{pypi_name}
%{python3_other_sitelib}/%{pypi_name}-*.egg-info
%endif

%changelog
%autochangelog
