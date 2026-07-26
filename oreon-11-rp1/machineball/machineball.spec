%global source0_hash 6f48c7722df48a1d6f750a25a0a0a2f4c024a1a10717b0287226959a18e6a708

Name:           machineball
Version:        1.0
Release:        50%{?dist}
Summary:        A futuristic ball game with simple rules
License:        GPL-1.0-or-later
URL:            http://benny.kramekweb.com/machineball/
Source0:        http://benny.kramekweb.com/%{name}/%{name}-src-%{version}-1.tar.gz
Source1:        machineball.desktop
Patch0:         machineball-fixes.patch
Patch1:         machineball-config-only-once.patch
Patch2:         machineball-1.0-ode.patch
Patch3:         machineball-1.0-timer-fix.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  alleggl-devel libGLU-devel ode-devel dumb-devel allegro-tools
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme opengl-games-utils

%description
Machine Ball is a futuristic sport with amazing 3D graphics and realistic
physics with very simple rules: Get the ball into your opponents goal. You can
use your machine to push the ball in, or you can collect powerups such as
missiles and blast the ball into the goal. Be creative.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-src -p1

%build
# The deps in the Makefile are incomplete force mbdata.c / .h generation first
make mbdata.c
%make_build CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 755 %{name} $RPM_BUILD_ROOT/usr/bin
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

for i in "16x16" "24x24" "32x32" "48x48" "64x64"; do
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$i/apps
  install -p -m 644 %{name}-icon-$i.xpm \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$i/apps/%{name}.xpm
done

%files
%doc README
%license COPYING
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.xpm

%changelog
%autochangelog
