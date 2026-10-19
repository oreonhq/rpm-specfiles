%global source0_hash 1e567e7ce5d9c68aac7b348e03b4cdb652d23fc4652b0089b83238e62d8925de
Name:      schismtracker
Version:   20260524
Release:        1%{?dist}
Summary:        Sound module composer/player
License:   GPL-2.0-only
URL:       http://schismtracker.org/
Source0:        https://github.com/schismtracker/schismtracker/archive/%{version}.tar.gz
Excludearch:   s390x
Requires:      hicolor-icon-theme
%if 0%{!?_without_x:1}
%endif
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libXt-devel
BuildRequires:  libXv-devel
BuildRequires:  make
BuildRequires:  perl-open
BuildRequires:  python3
BuildRequires:  utf8proc-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
