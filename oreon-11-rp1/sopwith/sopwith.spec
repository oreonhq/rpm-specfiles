%global source0_hash f46e3a4ad6a1cc9a8d1ced01bd29b6a0a46d64852bd97014194fc42ed049efa9
Name:           sopwith
Version:        2.9.0
Release:        2%{?dist}
Summary:        SDL port of the sopwith game
License:        GPL-2.0-or-later
URL:            https://github.com/fragglet/sdl-sopwith/
Source0:        https://github.com/fragglet/sdl-sopwith/archive/refs/tags/sdl-sopwith-%{version}.tar.gz
Source1:        sopwith.png
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  make
# /oreon:deps
%description
This is a port of the classic computer game "Sopwith" to run on modern
computers and operating systems.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n sdl-sopwith-sdl-sopwith-%{version}
./autogen.sh

%build

%configure
make %{?_smp_mflags}
%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_docdir}/sdl-sopwith
cat > %{name}.desktop <<EOF
[Desktop Entry]
Name=Sopwith
Type=Application
Comment=The classic sopwith game
Exec=sopwith
Terminal=false
Icon=sopwith
EOF
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications           \
  --add-category ArcadeGame                            \
  --add-category Game                                  \
  %{name}.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
