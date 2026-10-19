%global source0_hash c6bd67695734fd430ce8e8d744710531ed4dae1bc78d5cd0529af930144e7903
Name:           stormbaancoureur
Version:        2.1.6
Release:        1%{?dist}
Summary:        Simulated obstacle course for automobiles
License:        GPL-2.0-or-later
URL:            http://www.stolk.org/stormbaancoureur/
Source0:        http://www.stolk.org/stormbaancoureur/download/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        sturmbahnfahrer.png
Patch0:         stormbaancoureur-1.5.3-no-static-ode.patch
Patch1:         stormbaancoureur-2.0.2-snd-debug.patch
Patch2:         stormbaancoureur-2.1.6-ode.patch
Patch3:         stormbaancoureur-freeglut.patch
Requires:       hicolor-icon-theme opengl-games-utils
Provides:       sturmbahnfahrer = %{version}-%{release}
Obsoletes:      sturmbahnfahrer < %{version}-%{release}
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ode-devel
BuildRequires:  plib-devel
# /oreon:deps
%description
Stormbaancoureur is Dutch for "assault course driver"... for expert drivers
only. If you want to master the obstacle course, try to have the laws of
physics work with you, not against you.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p0
%patch -P3 -p0

sed -i 's|/usr/share/games/%{name}|%{_datadir}/%{name}|' src-%{name}/main.cxx

%build

pushd src-%{name}
make %{?_smp_mflags} \
  CXXFLAGS="$RPM_OPT_FLAGS -I../src-common -DGAMEVERSION=%{version}-Fedora"
popd
%install
pushd src-%{name}
make install DESTDIR=$RPM_BUILD_ROOT GAMEDIR=$RPM_BUILD_ROOT%{_datadir}/%{name}
popd
install -p -m 644 models-%{name}/*.3ds \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/models
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT%{_prefix}/games/%{name} $RPM_BUILD_ROOT%{_bindir}
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
