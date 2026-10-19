%global source0_hash 351d6b27b5e4524ae1b752d309e84092f765c6bc254d893de96150c4ea14c056
%bcond_without docs
%bcond_without tests
Name:           pychess
Version:        1.1.0
Release:        1%{?dist}
Summary:        Chess game for GNOME
License:        GPL-3.0-only
URL:            http://pychess.github.io
Source0:        https://github.com/pychess/pychess/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          0001-TimeSeal.py-make-IAC_WONT_ECHO-a-literal-as-telnetli.patch
Patch:          0001-Adjust-test-usage-of-get_event_loop-for-Python-3.14-.patch
Patch:          2359.patch
Patch:          2362.patch
Patch:          2364.patch
Patch:          65f609da762eded553d618d711f944fbfe39d2f5.patch
BuildArch:      noarch
%if %{with docs} || %{with tests}
%endif
%if %{with docs}
Suggests:       %{name}-doc
%endif
%if %{with tests}
%endif
Requires:       python3dist(psutil)
Requires:       python3dist(sqlalchemy) >= 2
Requires:       python3dist(websockets)
Requires:       python3-gobject
Requires:       librsvg2
Requires:       hicolor-icon-theme
Requires:       python3-gstreamer1
Requires:       gtksourceview3
Recommends:     stockfish
# oreon:deps
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gstreamer1
BuildRequires:  gtk3
BuildRequires:  gtksourceview3
BuildRequires:  libappstream-glib
BuildRequires:  librsvg2
BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  python3-gobject
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pexpect)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sqlalchemy)
BuildRequires:  python3dist(websockets)
BuildRequires:  sed
BuildRequires:  stockfish
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

pushd testing
PYCHESS_UNITTEST=true PYTHONPATH=../lib xvfb-run -a %{python3} ./run_tests.py
%endif
%files -f %{oreon_filedir}/main.list
%files -n pychess-doc -f %{oreon_filedir}/pychess-doc.list

%changelog

%autochangelog
