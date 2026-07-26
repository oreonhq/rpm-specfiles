%global source0_hash 84e9977770a131f3bbc699c2d6cae8b3471e44a4ae1e62024f697caa6bf19d96

Name:      schismtracker
Version:   20251014
Release:   2%{?dist}
Summary:   Sound module composer/player
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:   GPL-2.0-only
URL:       http://schismtracker.org/
Source0:   https://github.com/schismtracker/schismtracker/archive/%{version}.tar.gz

#Patch1:    desktop.patch

Excludearch:   s390x
Requires:      hicolor-icon-theme
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: perl-open
BuildRequires: SDL2-devel
BuildRequires: desktop-file-utils
BuildRequires: python3
%if 0%{!?_without_x:1}
BuildRequires: libXt-devel
BuildRequires: libXv-devel
%endif
BuildRequires: utf8proc-devel

%description
Schismtracker is a module tracker for the X Window System similar to
the DOS program `Impulse Tracker'. Schismtracker can play/modify various
sound formats such as MOD, S3M, XM, IT, 669 and others.  The user interface
is mostly text-based using SDL for graphical output.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
mkdir auto

%build
autoreconf -i
%configure --disable-dependency-tracking \
%if 0%{?_without_x:1}
--with-x=no \
%endif
;
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

pushd icons
for i in 16 22 24 32 36 48 64 72 96; do
        install -m644 -D schism-icon-${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done
install -m644 -D schism-icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
popd
desktop-file-validate %{buildroot}%{_datadir}/applications/schism.desktop

%files
%doc AUTHORS COPYING NEWS
%{_bindir}/schismtracker
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/schism.desktop
%{_datadir}/pixmaps/schism*.png

%changelog
%autochangelog
