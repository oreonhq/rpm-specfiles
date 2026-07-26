%global source0_hash 3dda31117e5a18b0e0357aaafea6d498f64e717ad8beab82adcde00711be5638

%bcond_without docs
%bcond_without tests

Name:           pychess
Version:        1.0.5
Release:        3%{?dist}
Summary:        Chess game for GNOME

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://pychess.github.io
Source0:        https://github.com/pychess/pychess/archive/%{version}/%{name}-%{version}.tar.gz
# PR#2235 Python 3.13: Drop use of telnetlib
# https://github.com/pychess/pychess/pull/2235
Patch:          0001-TimeSeal.py-make-IAC_WONT_ECHO-a-literal-as-telnetli.patch
# PR #2361 Adjust test usage of get_event_loop() for Python 3.14 changes
# Backported to 1.0.3
# https://github.com/pychess/pychess/pull/2361
Patch:          0001-Adjust-test-usage-of-get_event_loop-for-Python-3.14-.patch
# Fix run_tests.py so it exits 1 on failure
# https://github.com/pychess/pychess/pull/2359
Patch:          2359.patch
# Fix some async test failures
# https://github.com/pychess/pychess/pull/2362
Patch:          2362.patch
# Initial incorrect fix for FICS issues with Python 3.13+
# https://github.com/pychess/pychess/pull/2364
Patch:          2364.patch
# Corrected fix for FICS issues with Python 3.13+
# https://github.com/pychess/pychess/commit/65f609da762eded553d618d711f944fbfe39d2f5
Patch:          65f609da762eded553d618d711f944fbfe39d2f5.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pexpect)
BuildRequires:  python3dist(sqlalchemy) >= 2
BuildRequires:  gtk3
BuildRequires:  librsvg2
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  sed
%if %{with docs} || %{with tests}
BuildRequires:  gstreamer1
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(websockets)
%endif
%if %{with docs}
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-docs
Suggests:       %{name}-doc
%endif
%if %{with tests}
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  python3dist(coverage)
BuildRequires:  gtksourceview3
BuildRequires:  stockfish
%endif

Requires:       python3dist(psutil)
Requires:       python3dist(sqlalchemy) >= 2
Requires:       python3dist(websockets)
# gnome-settings-daemon
Requires:       python3-gobject
Requires:       librsvg2
Requires:       hicolor-icon-theme
Requires:       python3-gstreamer1
# for editing .pgn files
Requires:       gtksourceview3

Recommends:     stockfish

%description
PyChess is a GTK+ chess game for Linux. It is designed to at the same time
be easy to use, beautiful to look at, and provide advanced functions for
advanced players.

%if %{with docs}
%package        doc
Summary:        Documentation for PyChess
Requires:       python3-docs

%description    doc
This package contains additional documentation for PyChess.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

# disable update check
cat > lib/pychess/Utils/checkversion.py <<EOF
def isgit():
    return False

async def checkversion():
    return
EOF

%if %{with docs}
# Use local intersphinx inventory
# TODO: do the same for pgi-docs once that's packaged
sed -r \
    -e 's|https://docs.python.org/3\.4|%{_docdir}/python3-docs/html|' \
    -i docs/conf.py
%endif

%build
PYTHONPATH=${PWD}/lib %{python3} pgn2ecodb.py
PYTHONPATH=${PWD}/lib %{python3} create_theme_preview.py
%py3_build
%if %{with docs}
# generate html docs
PYTHONPATH=${PWD}/lib sphinx-build-3 docs html
%endif

%install
%py3_install

desktop-file-install --delete-original               \
        --dir=%{buildroot}%{_datadir}/applications   \
        --set-key=Exec --set-value=pychess           \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet                \
        %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%find_lang %{name}

%if %{with tests}
%check
# run tests
pushd testing
PYCHESS_UNITTEST=true PYTHONPATH=../lib xvfb-run -a %{python3} ./run_tests.py
%endif

%files -f %{name}.lang
%doc README.md AUTHORS ARTISTS DOCUMENTERS TRANSLATORS
%doc utilities
%license LICENSE
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/gtksourceview-3.0/language-specs/pgn.lang
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man?/*
%{_metainfodir}/*.metainfo.xml

%if %{with docs}
%files doc
%license LICENSE
%doc doc/*.dia
%doc html
%endif

%changelog
%autochangelog
