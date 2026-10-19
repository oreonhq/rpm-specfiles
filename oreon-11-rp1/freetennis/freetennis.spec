%global source0_hash 0d4663d1c9ce5bbef4d87a9d9f85a4570016a2945c41d1d293fb1357e426bebf
Name:           freetennis
Version:        0.4.8
Release:        1%{?dist}
Summary:        Tennis simulation game
License:        GPL-2.0-or-later
URL:            http://freetennis.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        freetennis.desktop
Source2:        freetennis.png
Patch0:         freetennis-0.4.8-pathfixes.patch
Patch1:         freetennis-0.4.8-build.patch
Patch2:         freetennis-0.4.8-ocaml-4.12.patch
Patch3:         freetennis-0.4.8-ocaml-5.0.0.patch
ExcludeArch:    sparc64 s390 s390x %{ix86}
# oreon:deps
BuildRequires:  SDL_gfx-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk2-devel
BuildRequires:  libXmu-devel
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-SDL-devel
BuildRequires:  ocaml-camlimages-devel
BuildRequires:  ocaml-lablgl-devel
BuildRequires:  ocaml-lablgtk-devel
# /oreon:deps
%description
Free Tennis is a free software tennis simulation game.  The game can be 
played against an A.I. or human-vs-human via LAN or internet.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%ifarch %{ocaml_native_compiler}
%make_build
%else
%make_build byte
%endif
%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mv freetennis $RPM_BUILD_ROOT%{_bindir}
mv graphics $RPM_BUILD_ROOT%{_datadir}/%{name}/
mv sfx $RPM_BUILD_ROOT%{_datadir}/%{name}/
desktop-file-install                                      \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/
install -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
