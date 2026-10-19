%global source0_hash 475c12f9c376026ae5b4d4c52e50b45a61989146b66e2b021fa111919d00fa35
%bcond_with tests_py
%global srcurl  https://github.com/andreikop/%{name}
Name:           enki
Version:        22.08.0
Release:        1%{?dist}
Summary:        Text editor for programmers
License:        GPL-2.0-or-later
URL:            http://%{name}-editor.org/
Source0:        %{srcurl}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch: %{qt5_qtwebengine_arches} noarch
%if %{with tests_py}
%endif
Requires:       python3
Requires:       python3-qt5
Requires:       python3-pyparsing
Requires:       python3-qutepart >= 3.3.2
Requires:       python3-sphinx
Requires:       python3-markdown
Requires:       hicolor-icon-theme
Obsoletes:      %{name}-plugins < 19.10.0
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python3-markdown
BuildRequires:  python3-mock
BuildRequires:  python3-pyparsing
BuildRequires:  python3-qt5
BuildRequires:  python3-qutepart
BuildRequires:  python3-regex
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%if %{with tests_py}
pushd tests
sed -i "s:'TRAVIS_OS_NAME' in os.environ:True:" test_base.py
xvfb-run -s '-screen :0 1024x768x16' %{__python3} run_all.py
%endif
%files -f %{oreon_filedir}/main.list
%files -n enki-doc -f %{oreon_filedir}/enki-doc.list

%changelog

%autochangelog
