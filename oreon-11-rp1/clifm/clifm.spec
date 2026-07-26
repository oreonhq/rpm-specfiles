%global source0_hash 902badc747aee1eb1a3a5556ff3fd9d83d2aa987d24e058024064df8a4b6b71f

Name:           clifm
Version:        1.26.3
Release:        3%{?dist}
Summary:        Shell-like, command line terminal file manager

# source is pretty evently split between these
License:        GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only
# misc/colors/ and plugins/ are GPL-3.0-only
# src/ are GPL-2.0-or-later

URL:            https://github.com/leo-arch/clifm
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  readline-devel
BuildRequires:  libcap-devel
BuildRequires:  libacl-devel
BuildRequires:  file-devel
BuildRequires:  desktop-file-utils

Requires:       hicolor-icon-theme

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

%files
%license LICENSE
%doc README.md CHANGELOG
%{_bindir}/%{name}
%{_datadir}/applications/clifm.desktop
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%changelog
%autochangelog
