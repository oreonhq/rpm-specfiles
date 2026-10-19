%global source0_hash dfdc0f339437345d9d5d8c2cb4bd43294c05821ebc8d5f0c9abfa4eec8f6c905
Name:           clifm
Version:        1.29
Release:        1%{?dist}
Summary:        Shell-like, command line terminal file manager
License:        GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only
URL:            https://github.com/leo-arch/clifm
Source0:        https://github.com/leo-arch/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  file-devel
BuildRequires:  gcc-c++
BuildRequires:  libacl-devel
BuildRequires:  libcap-devel
BuildRequires:  readline-devel
# /oreon:deps
%description
CliFM is a Command Line Interface File Manager: all input and interaction
is performed via commands. This is its main feature and strength.

Unlike most terminal file managers out there, indeed, CliFM replaces the
traditional TUI interface (also known as curses or text-menu based
interface) by a command-line interface (CLI), also known as REPL.

If working with the command-line, your workflow is not affected at all,
but just enriched with file management functionalities: automatic files
listing, files selection, bookmarks, tags, directory jumper, directory and
commands history, auto-cd and auto-open, bulk rename, TAB completion,
autosuggestions, and a trash system, among other features. In this sense,
CliFM is certainly a file manager, but also a shell extension.

Briefly put, with CliFM the command-line is always already there, never
hidden.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# just to be sure we use system lib
rm -f src/{printf*,qsort.h}

%build

%cmake
%cmake_build
%install
%cmake_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
