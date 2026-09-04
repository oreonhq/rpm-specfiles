%global source0_hash 5005696304065f9d44c301e035078e87d8d848e0f86ba9f6a5c54fc0cc827e2e

%global modname toot

Name:           %{modname}
Version:        0.51.1
Release:        %autorelease
Summary:        A CLI and TUI tool for interacting with Mastodon

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/ihabunek/%{modname}
Source0:        https://github.com/ihabunek/%{modname}/archive/refs/tags/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
# https://github.com/ihabunek/toot/issues/540
# but tui is broken
# Patch0:         urwid.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(setuptools-scm) >= 8
BuildRequires:  python3dist(wheel) python3dist(pytest) python3dist(pillow)
BuildRequires:  python3dist(urwid)

%description
Toot is a CLI and TUI tool for interacting with Mastodon instances
from the command line.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version}
rm -rf %{modname}.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel

%install
%pyproject_install

#%check
%{python3} -m pytest -k 'not test_console' --ignore=tests/tui/test_rich_text.py

%files -n %{modname}
%{_bindir}/toot
%{python3_sitelib}/%{modname}
%{python3_sitelib}/%{modname}-%{version}.dist-info/
%license LICENSE

%changelog
%autochangelog
