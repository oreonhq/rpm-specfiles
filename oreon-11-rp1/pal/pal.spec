%global source0_hash ce470cb7be76522ff58cd0325ad7817b6cc2132a5e0cea55de8c9eb63b54551c
Summary:        Command line calendar that displays holidays and events
Name:       pal
Version:    0.4.3
Release:        1%{?dist}
License:    GPL-2.0-or-later
Url:        http://palcal.sourceforge.net
Source0:        http://downloads.sourceforge.net/palcal/pal-%{version}.tgz
Patch0: pal-0.4.3-bz1037238.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
# /oreon:deps
%description
Pal is command-line calendar program for Unix/Linux that can keep track of
events.  It has similarities with the Unix cal command, the more complex GNU
gcal program, and the calendar program distributed with the BSDs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i 's/-o\ root//g' src/Makefile
sed -i 's/-o\ root//g' src/convert/Makefile
sed -i 's/G_CONST_RETURN/const/' src/*.c
%patch -P0 -p1

%build

make DEBUG=1 -C src OPT="$RPM_OPT_FLAGS"
%install
make -C src DESTDIR="$RPM_BUILD_ROOT" install-no-rm
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}*
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
