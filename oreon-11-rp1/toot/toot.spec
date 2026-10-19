%global source0_hash 05dd422ec0689183b7ff80c9610594156777a0f8e7d1205dce09fbbfe338f86f
%global modname toot
Name:           %{modname}
Version:        0.52.1
Release:        1%{?dist}
Summary:        A CLI and TUI tool for interacting with Mastodon
License:        GPL-3.0-only
URL:            https://github.com/ihabunek/%{modname}
Source0:        https://github.com/ihabunek/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-toot = %{version}-%{release}
# /oreon:deps
%package -n       python3-toot+images
Summary:        Metapackage for python3-toot images extras
Requires:       python3-toot = %{version}-%{release}
Requires:       python3dist(pillow) >= 9.5.0
Requires:       python3dist(term-image) >= 0.7.2
Provides:       python3dist(toot[images]) = %{version}-%{release}

%description -n python3-toot+images
Metapackage for python3-toot images extras.

%description
Toot is a CLI and TUI tool for interacting with Mastodon instances
from the command line.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version}
rm -rf %{modname}.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build

export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel
%install
%pyproject_install
%{python3} -m pytest -k 'not test_console' --ignore=tests/tui/test_rich_text.py
%oreon_autofiles main

%files

%changelog

%autochangelog
