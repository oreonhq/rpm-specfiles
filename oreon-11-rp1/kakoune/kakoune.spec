%global source0_hash 7ef778bd199e05977841e6f69aad2bee6cd58fb23b0e4bc265d012d42de17580
%bcond_without tests
Name:           kakoune
Version:        2026.05.21
Release:        1%{?dist}
Summary:        mawww's experiment for a better code editor
License:        Unlicense
URL:            https://kakoune.org/
Source0:        https://github.com/mawww/kakoune/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc-c++
BuildRequires:  glibc-langpack-en
BuildRequires:  make
BuildRequires:  pkgconfig(ncurses)
# /oreon:deps
%description
Kakoune is a code editor that implements Vi’s "keystrokes as a text editing
language" model. As it is also a modal editor, it is somewhat similar to the Vim
editor (after which Kakoune was originally inspired).

Kakoune can operate in two modes: normal and insertion. In insertion mode, keys
are directly inserted into the current buffer. In normal mode, keys are used to
manipulate the current selection and to enter insertion mode.

Kakoune has a strong focus on interactivity. Most commands provide immediate and
incremental results, while being competitive with Vim in terms of keystroke
count.

Kakoune works on selections, which are oriented, inclusive ranges of characters.
Selections have an anchor and a cursor. Most commands move both of them except
when extending selections, where the anchor character stays fixed and the cursor
moves around.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Use default Fedora build flags
sed -i '/CXXFLAGS-debug-no = -O3 -g3/d' Makefile

%build

%set_build_flags
%make_build
%install
%make_install \
    PREFIX=%{_prefix} \
    version=%{version} \
    docdir=%{buildroot}%{_docdir}/%{name} \
    %{nil}
%oreon_autofiles main
%if %{with tests}
%check

%set_build_flags
LANG=en_US.utf8 %make_build test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
