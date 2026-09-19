%global source0_hash 672eea03da5c2617c88ece349bd8d253d790be2e3d5429c0e5e2d682529518dd

Name:       qmltermwidget
Summary:    A port of QTermWidget to QML

# Most of the project's code is under the GPL.
#
# The few files subject to the LGPL are:
# - lib/TerminalCharacterDecoder.cpp
# - lib/TerminalCharacterDecoder.h
# - lib/kprocess.cpp
# - lib/kprocess.h
# - lib/kpty.cpp
# - lib/kpty.h
# - lib/kpty_p.h
# - lib/kptydevice.cpp
# - lib/kptydevice.h
# - lib/kptyprocess.cpp
# - lib/kptyprocess.h
# - lib/qtermwidget.cpp
# - lib/qtermwidget.h
# - lib/qtermwidget_version.h.in
#
# There are also some build scripts under BSD-3-Clause,
# but since these are not included in the resulting package,
# said license is omitted from the License tag.
License:    GPL-2.0-or-later AND LGPL-2.0-or-later

%global git_date   20220109
%global git_commit 63228027e1f97c24abb907550b22ee91836929c5
%global git_commit_short %(c="%{git_commit}"; echo "${c:0:7}")

Version:    0.2.0^%{git_date}git%{git_commit_short}
Release:    7%{?dist}

URL:        https://github.com/Swordfish90/%{name}
Source0:    %{URL}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz

BuildRequires: make
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Quick)

%description
This project is a QML port of QTermWidget. It is written
to be as close as possible to the upstream project in order
to make cooperation possible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{git_commit}

%build
%qmake_qt5
%make_build

%install
make install INSTALL_ROOT=%{buildroot}
%if 0%{?flatpak}
# qtbase is part of runtime in /usr, this is built in /app
mv %{buildroot}/usr %{buildroot}%{_prefix}
%endif

%files
%license LICENSE LICENSE.LGPL2+
%doc README.md AUTHORS
%{_qt5_qmldir}/QMLTermWidget/

%changelog
%autochangelog
