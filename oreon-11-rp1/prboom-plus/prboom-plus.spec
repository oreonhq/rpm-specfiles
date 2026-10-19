%global source0_hash 4b647b4b14c3fac00711e6bf19f996bbfe37754a3b9bb5be6791f0c3fd993438
Name:    prboom-plus
Version: 2.6.66
Release:        1%{?dist}
Summary:        Free enhanced DOOM engine
URL:     https://github.com/coelckers/prboom-plus/tags
License: BSD-3-Clause AND MIT AND LGPL-2.0-or-later
Source0:        https://github.com/coelckers/prboom-plus/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:  pointer-types.patch
Requires:      freedoom
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dumb-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libpcre2-32)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  portmidi-devel
# /oreon:deps
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
desktop-file-install --dir=%{buildroot}%{_datadir}/applications ICONS/%{name}.desktop
install -Dpm 644 ICONS/%{name}.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg
install -Dpm 644 ICONS/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}.bash
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n prboom-plus-bash-completion -f %{oreon_filedir}/prboom-plus-bash-completion.list

%changelog

%autochangelog
