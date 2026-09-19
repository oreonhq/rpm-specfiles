%global source0_hash 9455aeb8f826fa8385c850dc22bf0f22cf9069b3c3423fba4bf2c6f6226d9903

Summary: more, less, most
Name: most
Version: 5.2.0
Release: 10%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.jedsoft.org/releases/most/
Source: http://www.jedsoft.org/releases/most/most-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires: slang-devel
# https://bugzilla.redhat.com/show_bug.cgi?id=1230278
Patch0: bz1230278.patch
Patch1: most-no-strip.patch

%description
most is a paging program that displays, one window-full at a time, the
contents of a file on a terminal. It pauses after each window-full and
prints on the window status line the screen the file name, current line
number, and the percentage of the file so far displayed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0
%patch -P1 -p0

%build
%configure
# Parallel builds sometimes miss to create this directory before starting
# the compiler. In theory the Makefile would create this before running gcc.
mkdir -p src/objs
%make_build

%install
%make_install

%files
%license COPYRIGHT
%doc README changes.txt most.txt most-fun.txt lesskeys.rc most.rc
%{_bindir}/most
%{_mandir}/man1/most.1*

%changelog
%autochangelog
