%global source1_hash 333dd7c003608d8d27b122464cc6798f99d3e7cf51c2b1133238c8c2079accb7
%global source0_hash c519d77f2214cddeb0b89e68391ebc2355220c797b34a6eb7ff60e15e54e4ddb
%global snapshot 20060225
Name:           duel3
Version:        0.1
Release:        1%{?dist}
Summary:        One on one spaceship duel in a 2D arena
License:        LicenseRef-Callaway-BSD
Source0:        http://downloads.sourceforge.net/%{name}/Duel3_%{snapshot}_src.zip
Source1:        http://downloads.sourceforge.net/%{name}/Duel3_%{snapshot}_bin.zip
Source2:        %{name}.desktop
Source3:        %{name}.png
Source4:        music-credits.txt
Patch0:         Duel3_20060225-fixes.patch
Patch1:         Duel3_20060225-windowed-mode.patch
Patch2:         Duel3_20060225-fix-buf-oflow.patch
Patch3:         Duel3_20060225-extra-fix-buf-oflow.patch
Requires:       hicolor-icon-theme opengl-games-utils
# oreon:deps
BuildRequires:  alleggl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  dumb-devel
BuildRequires:  gcc-c++
BuildRequires:  libGLU-devel
BuildRequires:  make
# /oreon:deps
%description
The sudden attack from the Martain Rim miners caught the Earth by surprise,
there was no way the meager Earth Space Fleet could defend themselves. The
miners attacked, and eliminated their enemies, and then returned to the
asteroid belt. However, Earth could not accept such an embarrassing defeat. The
military developed new space fighters, and trained several squadrons of elite
pilots. The task force was then deployed against the miners. These trained
pilots utterly defeated the miners in a matter of weeks, and the first space
war in human history was finished.

The military, however, now had a new problem on their hands. These new elite
pilots were becoming restless, and there was no way for them to test their
skills. The military dare not disband the force, or let their skills dull, so
the Duel Combat League was formed. The newly formed league quickly became the
premier entertainment form on the planet, and the military's largest source of
income.

Take control of a Duel fighter, and test your skills against your opponents and
the arena itself in fast-paced space combat.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 1 -n Duel3_%{snapshot}_src
mv Duel3_%{snapshot}_bin/* Source
cp %{SOURCE4} .
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
sed -i 's/\r//' Source/readme.txt license.txt music-credits.txt
iconv -f iso8859-1 -t utf-8 music-credits.txt > temp
mv temp music-credits.txt

%build

pushd Source
make %{?_smp_mflags} PREFIX=%{_prefix} \
  CFLAGS="-std=c++14 $RPM_OPT_FLAGS -fsigned-char -Wno-deprecated-declarations -Wno-non-virtual-dtor"
popd
%install
pushd Source
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}
popd
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
