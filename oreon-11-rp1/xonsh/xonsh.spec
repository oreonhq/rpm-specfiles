%global source0_hash 461244cf1de8ed28d0c07cc548342b9e7969d46e17ef8d71b5d3064307930a25
Name:           xonsh
Version:        0.24.2
Release:        1%{?dist}
Summary:        A general purpose, Python-ish shell
License:        BSD-2-Clause AND MIT
URL:            https://xon.sh
Source0:        https://files.pythonhosted.org/packages/source/x/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       %{py3_dist prompt-toolkit}
Requires:       %{py3_dist pygments}
Requires:       %{py3_dist pyperclip}
Requires:       %{py3_dist setproctitle}
Requires:       %{py3_dist distro}
Requires:       %{py3_dist ujson}
Requires:       %{py3_dist ply}
Requires:       %{py3_dist virtualenv}
Recommends:     bash-completion
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-xonsh = %{version}-%{release}
# /oreon:deps
%package -n       python3-xonsh+ptk
Summary:        Metapackage for python3-xonsh ptk extras
Requires:       python3-xonsh = %{version}-%{release}
Requires:       python3dist(prompt-toolkit) >= 3.0.29
Provides:       python3dist(xonsh[ptk]) = %{version}-%{release}

%description -n python3-xonsh+ptk
Metapackage for python3-xonsh ptk extras.

%package -n       python3-xonsh+pygments
Summary:        Metapackage for python3-xonsh pygments extras
Requires:       python3-xonsh = %{version}-%{release}
Requires:       python3dist(pygments) >= 2.2
Provides:       python3dist(xonsh[pygments]) = %{version}-%{release}

%description -n python3-xonsh+pygments
Metapackage for python3-xonsh pygments extras.

%package -n       python3-xonsh+mac
Summary:        Metapackage for python3-xonsh mac extras
Requires:       python3-xonsh = %{version}-%{release}
Provides:       python3dist(xonsh[mac]) = %{version}-%{release}

%description -n python3-xonsh+mac
Metapackage for python3-xonsh mac extras.

%package -n       python3-xonsh+linux
Summary:        Metapackage for python3-xonsh linux extras
Requires:       python3-xonsh = %{version}-%{release}
Provides:       python3dist(xonsh[linux]) = %{version}-%{release}

%description -n python3-xonsh+linux
Metapackage for python3-xonsh linux extras.

%package -n       python3-xonsh+proctitle
Summary:        Metapackage for python3-xonsh proctitle extras
Requires:       python3-xonsh = %{version}-%{release}
Provides:       python3dist(xonsh[proctitle]) = %{version}-%{release}

%description -n python3-xonsh+proctitle
Metapackage for python3-xonsh proctitle extras.

%package -n       python3-xonsh+full
Summary:        Metapackage for python3-xonsh full extras
Requires:       python3-xonsh = %{version}-%{release}
Provides:       python3dist(xonsh[full]) = %{version}-%{release}

%description -n python3-xonsh+full
Metapackage for python3-xonsh full extras.

%package -n       python3-xonsh+bestshell
Summary:        Metapackage for python3-xonsh bestshell extras
Requires:       python3-xonsh = %{version}-%{release}
Requires:       python3dist(prompt-toolkit) >= 3.0.29
Requires:       python3dist(pygments) >= 2.2
Provides:       python3dist(xonsh[bestshell]) = %{version}-%{release}

%description -n python3-xonsh+bestshell
Metapackage for python3-xonsh bestshell extras.

%package -n       python3-xonsh+test
Summary:        Metapackage for python3-xonsh test extras
Requires:       python3-xonsh = %{version}-%{release}
Requires:       python3dist(pytest) >= 7
Requires:       python3dist(prompt-toolkit) >= 3.0.29
Requires:       python3dist(pygments) >= 2.2
Requires:       python3dist(coverage) >= 5.3.1
Requires:       python3dist(pyte) >= 0.8.0
Requires:       python3dist(virtualenv) >= 20.16.2
Provides:       python3dist(xonsh[test]) = %{version}-%{release}

%description -n python3-xonsh+test
Metapackage for python3-xonsh test extras.

%package -n       python3-xonsh+dev
Summary:        Metapackage for python3-xonsh dev extras
Requires:       python3-xonsh = %{version}-%{release}
Provides:       python3dist(xonsh[dev]) = %{version}-%{release}

%description -n python3-xonsh+dev
Metapackage for python3-xonsh dev extras.

%package -n       python3-xonsh+doc
Summary:        Metapackage for python3-xonsh doc extras
Requires:       python3-xonsh = %{version}-%{release}
Requires:       python3dist(sphinx) >= 3.1
Provides:       python3dist(xonsh[doc]) = %{version}-%{release}

%description -n python3-xonsh+doc
Metapackage for python3-xonsh doc extras.

%description
xonsh is a Python-powered, cross-platform, Unix-gazing shell language and
command prompt.

The language is a superset of Python 3.6+ with additional shell primitives.
xonsh (pronounced conch) is meant for the daily use of experts and novices
alike.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

# Unbundle ply
sed --in-place '/xonsh\.parsers\.ply/d' pyproject.toml
sed --in-place -e 's/xonsh\.parsers\.ply/ply/' \
               -e 's/from xonsh\.parsers import ply/import ply/' \
               $(grep -Erl --include='*.py' 'xonsh\.parsers( import |\.)ply')
rm -r xonsh/parsers/ply

# Remove shebang.
sed --in-place "s:#!\s*/usr.*::" xonsh/xoreutils/_which.py xonsh/webconfig/main.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%global __pytest PYTHONPATH="$PYTHONPATH:$(pwd)" %{python3} -m xonsh run-tests.xsh test --
%pytest -v || :
%post

if [ "$1" -ge 1 ]; then
  if [ ! -f %{_sysconfdir}/shells ] ; then
    touch %{_sysconfdir}/shells
  fi
  for binpath in %{_bindir} /bin; do
    if ! grep -q "^${binpath}/xonsh$" %{_sysconfdir}/shells; then
       (cat %{_sysconfdir}/shells; echo "$binpath/xonsh") > %{_sysconfdir}/shells.new
       mv %{_sysconfdir}/shells{.new,}
    fi
  done
fi
%postun

if [ "$1" = 0 ] && [ -f %{_sysconfdir}/shells ] ; then
  sed -e '\!^%{_bindir}/xonsh$!d' -e '\!^/bin/xonsh$!d' < %{_sysconfdir}/shells > %{_sysconfdir}/shells.new
  mv %{_sysconfdir}/shells{.new,}
fi
%files

%changelog

%autochangelog
