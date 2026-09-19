%global source0_hash 475c12f9c376026ae5b4d4c52e50b45a61989146b66e2b021fa111919d00fa35

%bcond_with tests_py

%global srcurl  https://github.com/andreikop/%{name}

Name:           enki
Version:        22.08.0
Release:        15%{?dist}
Summary:        Text editor for programmers

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://%{name}-editor.org/

Source0:        %{srcurl}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch: %{qt5_qtwebengine_arches} noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  python3-qt5
BuildRequires:  python3-pyparsing
BuildRequires:  python3-qutepart

# documentation
BuildRequires:  python3-sphinx

# tests
BuildRequires:  desktop-file-utils
%if %{with tests_py}
#BuildRequires:  python3-sip
BuildRequires:  python3-qt5-webengine
BuildRequires:  xorg-x11-server-Xvfb
%endif

# FIXME add more optional dependencies to enable specific tests
BuildRequires:  python3-markdown
BuildRequires:  python3-mock
BuildRequires:  python3-regex

# runtime
Requires:       python3

Requires:       python3-qt5
Requires:       python3-pyparsing
# enforce fix for python 3.10
Requires:       python3-qutepart >= 3.3.2
# FIXME is sphinx optional?
Requires:       python3-sphinx

# FIXME issue#425, markdown is needed as dependency
Requires:       python3-markdown

%if 0%{?fedora}

# optional for special runtime
Recommends:     python3-flake8
Recommends:     python3-docutils
#Recommends:     python3-markdown
Recommends:     python3-regex
Recommends:     ctags
# FIXME do we need QtWebEngine for sure?
# upstream issues/446, rhbz#1642060
Recommends:     python3-qt5-webengine

# upstream issues/465
Suggests:       python3-qtconsole

%endif # fedora

# we place additional icons
Requires:       hicolor-icon-theme

# compatibility, accidently used subpackage, rhbz#1292724
Obsoletes:      %{name}-plugins < 19.10.0

%description
Enki is a text editor for programmers. It is:

    - User friendly. Intuitive interface. Works out of the box. You don’t have
      to read a lot of docs.
    - Hacker friendly. Work as quickly as possible. Navigate efficiently without
      your mouse.
    - Advanced. You invent software. An editor helps you focus on inventing,
      instead of fighting with your tools.
    - Extensible. Operating systems are designed for running applications. Enki
      is designed for running plugins.
    - Cross platform. Use your habitual editor on any OS. Tested on Linux and
      Windows. Users report that Enki works Mac OS X.
    - High quality. No long list of fancy features. But, what is done, is done
      well.
    - Open source. Created, tested, and designed for the community, by the
      community, and with the community.

%package doc
Summary:        Additional documentation for %{name}

%description doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n%{name}-%{version}
# distutils does not know options entry_points and install_requires: use setuptools instead
sed -i s:distutils\.core:setuptools: setup.py
# skip enforcement of optional dependencies
sed -i -r -e '/flake8/d' -e '/CodeChat/d' -e '/regex/d' setup.py
# ignore useless distribution folders
rm -rv debian rpm win
# skip tests of plugins, too hungry for poor Xvfb
rm -v tests/test_plugins/*.py

%build
%py3_build
sphinx-build-3 doc html
rm -rv html/.buildinfo html/.doctrees

%install
%py3_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# FIXME rhbz#1752766, python3-sip not available
%if %{with tests_py}
# we must be inside the tests folder to let the script find something
pushd tests
# FIXME ugly hackery to disable failing tests
# https://github.com/andreikop/enki/issues/456
sed -i "s:'TRAVIS_OS_NAME' in os.environ:True:" test_base.py
# run tests in a mocked X environment
xvfb-run -s '-screen :0 1024x768x16' %{__python3} run_all.py
%endif

%files
%license LICENSE.GPL2
%doc README.md ChangeLog
%{python3_sitelib}/%{name}*.egg-info
%{python3_sitelib}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}

%files doc
%license LICENSE.GPL2
%doc html/

%changelog
%autochangelog
