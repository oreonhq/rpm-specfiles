%global source0_hash 0d38b524d377257b106bad6d856d8ae3304140e1ee24085343e6ddf1b65811f1

Name:           cgdb
Version:        0.8.0
Release:        %autorelease
Summary:        CGDB is a curses-based interface to the GNU Debugger (GDB)

License:        GPL-2.0-only
URL:            https://cgdb.github.io/
Source0:        https://cgdb.me/files/%{name}-%{version}.tar.gz
Source1:        https://cgdb.github.io/images/screenshot_debugging.png

Patch:          cgdb-configure-c99.patch

BuildRequires:  gcc-c++
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  texinfo
BuildRequires:  flex
BuildRequires:  make

Requires:       gdb

%description
CGDB is a curses-based interface to the GNU Debugger (GDB).
The goal of CGDB is to be lightweight and responsive; not encumbered with
unnecessary features.
The interface is designed to deliver the familiar GDB text interface,
with a split screen showing the source as it executes.
The UI is modeled on the classic Unix text editor, vi.
Those familiar with vi should feel right at home using CGDB.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Avoid re-running configure.
touch -r aclocal.m4 config/*.m4 configure

%build
autoconf
%configure
%make_build

%install
%make_install
rm -rf %{buildroot}%{_infodir}/dir

%files
%doc AUTHORS NEWS ChangeLog
%license COPYING
%{_bindir}/cgdb
%{_datadir}/cgdb
%{_infodir}/cgdb.info.*

%changelog
%autochangelog
