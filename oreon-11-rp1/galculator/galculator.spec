%global source0_hash 01cfafe6606e7ec45facb708ef85efd6c1e8bb41001a999d28212a825ef778ae

Name:           galculator
Version:        2.1.4
Release:        25%{?dist}
Summary:        GTK 3 based scientific calculator

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://galculator.mnim.org/
Source0:        http://galculator.mnim.org/downloads/galculator-%{version}.tar.bz2
Patch1:         galculator-2.1.4-build.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  gtk3-devel
BuildRequires:  perl(XML::Parser)
BuildRequires:  autoconf, automake, libtool
BuildRequires: make

%description
A GTK 3 based scientific calculator with ordinary notation, reverse
polish notation, a formula entry mode, different number bases, and
different units of angular measure.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .build

%build
%set_build_flags
CFLAGS="$CFLAGS -std=gnu11"
%configure
make %{?_smp_mflags}

%install
make DESTDIR=${RPM_BUILD_ROOT} install
%find_lang %{name}

desktop-file-install --delete-original \
  %if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
    --vendor fedora \
  %endif
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
  --add-category "Calculator;GTK;" \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README COPYING THANKS
%attr(0755,root,root) %{_bindir}/galculator
%{_datadir}/applications/*galculator.desktop
%{_datadir}/galculator/
%{_datadir}/appdata/galculator.*
%{_datadir}/pixmaps/galculator.*
%{_datadir}/icons/hicolor/48x48/apps/galculator.*
%{_datadir}/icons/hicolor/scalable/apps/galculator.*
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
