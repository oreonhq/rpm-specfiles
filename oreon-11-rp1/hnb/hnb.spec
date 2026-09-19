%global source0_hash 234f517ab08fdfc66f4f602c9e445c7f0cd60f001fc9819642394e8ef6194f77

Summary: Hierarchical Notebook
Name: hnb
Version: 1.9.19
Release: 29%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://github.com/liskin/lhnb
Source0: https://nomi.cz/download/releases/lhnb/lhnb-%{version}.tar.gz
Source1: hnbrc.vi
Patch0: %{name}-rpm.patch
# fix build with gcc10
Patch1: hnb-gcc10.patch
# fix -Werror=format-security errors
Patch3: hnb-format-security.patch
BuildRequires: gcc
BuildRequires: ncurses-devel
BuildRequires: make

%description
Hierarchical notebook(hnb) is a curses program to structure many kinds
of data in one place, for example addresses, to-do lists, ideas, book
reviews or to store snippets of brainstorming. Writing structured
documents and speech outlines.

The default format is XML but hnb can also export to ASCII and HTML.
External programs may be used for more advanced conversions of the XML
data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n lhnb-%{version}
%patch -P0 -p1 -b .r
%patch -P1 -p1 -b .gcc10
%patch -P3 -p1 -b .format-security
cp -p %{SOURCE1} doc/

%build
%{__make} OPTFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
install -D -p src/hnb $RPM_BUILD_ROOT%{_bindir}/hnb
install -D -pm644 doc/hnb.1 $RPM_BUILD_ROOT%{_mandir}/man1/hnb.1

%files
%license COPYING
%doc README doc/Documentation.html doc/hnbrc*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
