%global source0_hash 4b647b4b14c3fac00711e6bf19f996bbfe37754a3b9bb5be6791f0c3fd993438

Name:    prboom-plus
Version: 2.6.66
Release: 11%{?dist}
Summary: Free enhanced DOOM engine
URL:     https://github.com/coelckers/prboom-plus/tags
License: BSD-3-Clause AND MIT AND LGPL-2.0-or-later

Source0: https://github.com/coelckers/prboom-plus/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:  pointer-types.patch

Requires:      freedoom

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: dumb-devel pkgconfig(fluidsynth) pkgconfig(libpcre2-32) pkgconfig(libpng)
BuildRequires: pkgconfig(SDL2_image) pkgconfig(SDL2_mixer) pkgconfig(SDL2_net) pkgconfig(glu)
BuildRequires: pkgconfig(alsa) portmidi-devel pkgconfig(mad) pkgconfig(vorbis)
BuildRequires: desktop-file-utils

%description
Doom is a classic 3D shoot-em-up game.
PrBoom+ is a Doom source port developed from the original PrBoom project
by Andrey Budko.
The target of the project is to extend the original port with features
that are necessary or useful.

%package        bash-completion
Summary:        Bash completion for %{name}
Group:          System/Shells
Requires:       bash-completion
Supplements:    packageand(%{name}:bash)
BuildArch:      noarch

%description    bash-completion
Bash command line completion support for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{version}

%patch -P 0 -p0

%build
pushd prboom2
%cmake -DDiOOMWADDIR=%{_datadir}/doom -DCMAKE_C_FLAGS="$CMAKE_C_FLAGS -std=gnu17 -fPIE" -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
pushd prboom2
%cmake_install

# desktop + icons
desktop-file-install --dir=%{buildroot}%{_datadir}/applications ICONS/%{name}.desktop
install -Dpm 644 ICONS/%{name}.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg

# Completions
install -Dpm 644 ICONS/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}.bash

%files
%license prboom2/COPYING
%{_docdir}/*
%{_bindir}/*
%{_datadir}/prboom-plus/*
%{_mandir}/man5/*
%{_mandir}/man6/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}.bash

%changelog
%autochangelog
