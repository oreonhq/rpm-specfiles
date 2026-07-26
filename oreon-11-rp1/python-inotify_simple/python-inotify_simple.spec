%global source0_hash 8440ffe49c4ae81a8df57c1ae1eb4b6bfa7acb830099bfb3e305b383005cc128

%global sum()   A simple %* wrapper around inotify
%global desc \
inotify_simple is a simple Python wrapper around inotify. No fancy bells and \
whistles, just a literal wrapper with ctypes. Only 122 lines of code!

%if 0%{?fedora}
  %bcond_without python3
  %if 0%{?fedora} > 29
    %bcond_with python2
  %else
    %bcond_without python2
  %endif
%else
  %if 0%{?rhel} > 7
    %bcond_with    python2
    %bcond_without python3
  %else
    %bcond_without python2
    %bcond_with    python3
  %endif
%endif

%global sname inotify_simple

Name:           python-%sname
Version:        1.3.5
Release:        17%{?dist}
Summary:        %{sum Python}
BuildArch:      noarch

License:        BSD-2-Clause
URL:            https://github.com/chrisjbillington/%sname
Source0:        https://pypi.org/packages/source/i/%sname/%sname-%version.tar.gz

%if %{with python2}
BuildRequires: python2-devel
BuildRequires: python2-enum34
BuildRequires: python2-setuptools
%endif
%if %{with python3}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%endif

%description
%desc

%if %{with python2}
%package -n     python2-%sname
Summary:        %{sum Python 2}
Requires:       python2-enum34

%description -n python2-%sname
%{desc}
%endif

%if %{with python3}
%package -n     python3-%sname
Summary:        %{sum Python 3}

%description -n python3-%sname
%{desc}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %sname-%version -p1

%build
%{?with_python2:%py2_build}
%{?with_python3:%py3_build}

%install
%{?with_python2:%py2_install}
%{?with_python3:%py3_install}

%if %{with python2}
%files -n python2-%sname
%license LICENSE
%python2_sitelib/%sname.py*
%python2_sitelib/%sname-%{version}*.egg-info
%endif

%if %{with python3}
%files -n python3-%sname
%license LICENSE
%python3_sitelib/%sname.py
%python3_sitelib/%sname-%{version}*.egg-info
%python3_sitelib/__pycache__/inotify_simple*
%endif

%changelog
%autochangelog
