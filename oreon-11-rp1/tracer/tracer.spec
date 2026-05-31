%global source0_hash 32e8c70f497a14cfa0eb4a0e1a59fe5cb17193d84790d8ca728260423689d76d

%if 0%{?rhel} || (0%{?oreon} >= 11)

%if 0%{?rhel} <= 7 || (0%{?oreon} >= 11)
%bcond_without python2
%bcond_with python3
%bcond_with suggest
%else
%bcond_with python2
%bcond_without python3
%bcond_without suggest
%endif

%else
%bcond_with python2
%bcond_without python3
%bcond_without suggest
%endif

Name:       tracer
Version:    1.4
Release:    2%{?dist}
Summary:    Finds outdated running applications in your system

BuildArch:  noarch
License:    GPL-2.0-or-later
URL:        http://tracer-package.com/
# Sources can be obtained by
# git clone git@github.com:FrostyX/tracer.git
# cd tracer
# tito build --tgz
Source0:    %{name}-%{version}.tar.gz

BuildRequires:  asciidoc
BuildRequires:  gettext
BuildRequires:  make

%global _description \
Tracer determines which applications use outdated files and prints them. For\
special kind of applications such as services or daemons, it suggests a standard\
command to restart it. Detecting whether file is outdated or not is based on a\
simple idea. If application has loaded in memory any version of a file\
which is provided by any package updated since system was booted up, tracer\
consider this application as outdated.

%description %{_description}

%package common
Summary:        Common files for %{name}

%description common
%{summary}.

%if %{with python2}
%package -n python2-%{name}
Summary:        %{summary}
%if ! %{with python3}
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} <= 0.6.11
%endif
BuildRequires:  python2-devel
BuildRequires:  python2-sphinx
%if 0%{?rhel} && 0%{?rhel} <= 7 || (0%{?oreon} >= 11)
BuildRequires:  rpm-python
BuildRequires:  python2-mock
Requires:       rpm-python
%else
BuildRequires:  python2-rpm
Requires:       python2-rpm
%endif
BuildRequires:  python2-pytest
BuildRequires:  python2-psutil
BuildRequires:  python2-six
BuildRequires:  dbus-python
BuildRequires:  python2-distro
BuildRequires:  python2-backports-functools_lru_cache
Requires:       dbus-python
Requires:       python2-psutil
Requires:       python2-future
Requires:       python2-six
Requires:       python2-distro
Requires:       python2-backports-functools_lru_cache
Requires:       %{name}-common = %{version}-%{release}
%if %{with suggest}
Suggests:       python-argcomplete
%else
Requires:       python-argcomplete
%endif
%{?python_provide:%python_provide python2-%{name}}

%description -n python2-%{name} %{_description}

Python 2 version.
%endif

%if %{with python3}
%package -n python3-%{name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-pytest
BuildRequires:  python3-psutil
BuildRequires:  python3-six
BuildRequires:  python3-dbus
BuildRequires:  python3-rpm
BuildRequires:  python3-distro
BuildRequires:  python3-setuptools
%if 0%{?fedora} || (0%{?oreon} >= 11)
BuildRequires:  python3-libdnf5
%endif
Requires:       python3-rpm
Requires:       python3-psutil
Requires:       python3-dbus
Requires:       python3-six
Requires:       python3-distro
Requires:       %{name}-common = %{version}-%{release}
%if 0%{?fedora} || (0%{?oreon} >= 11)
Requires:       python3-libdnf5
%endif
%if %{with suggest}
Suggests:       python3-argcomplete
%else
Requires:       python3-argcomplete
%endif
%{?python_provide:%python_provide python3-%{name}}
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} <= 0.6.11

%description -n python3-%{name} %{_description}

Python 3 version.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%if %{with python2}
sed -i -e '1s|^#!.*$|#!%{__python2}|' bin/%{name}.py
%endif

%if %{with python3}
sed -i -e '1s|^#!.*$|#!%{__python3}|' bin/%{name}.py
%endif

%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%py3_build
%endif
make %{?_smp_mflags} man

%check
%if %{with python3}
python3 -m pytest -v tests
%else
python2 -m pytest -v tests
%endif

%install
# @TODO use following macros
# %%py2_install
# %%py3_install

mkdir -p %{buildroot}%{_datadir}/%{name}/
cp -a data/* %{buildroot}%{_datadir}/%{name}/

%if %{with python2}
mkdir -p %{buildroot}%{python2_sitelib}/%{name}/
cp -ar %{name}/* tests %{buildroot}%{python2_sitelib}/%{name}/
%endif

%if %{with python3}
mkdir -p %{buildroot}%{python3_sitelib}/%{name}/
cp -ar %{name}/* tests %{buildroot}%{python3_sitelib}/%{name}/
%endif

install -Dpm0755 bin/%{name}.py %{buildroot}%{_bindir}/%{name}
install -Dpm0644 doc/build/man/%{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
install -pm 644 scripts/tracer.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/tracer

make DESTDIR=%{buildroot}%{_datadir} mo
%find_lang %{name}

%files common -f %{name}.lang
%license LICENSE
%doc README.md
%{_datadir}/%{name}/
%{_sysconfdir}/bash_completion.d/tracer

%if %{with python2}
%files -n python2-%{name}
%{python2_sitelib}/%{name}/
%endif

%if %{with python3}
%files -n python3-%{name}
%{python3_sitelib}/%{name}/
%endif

%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4-2
- Import
