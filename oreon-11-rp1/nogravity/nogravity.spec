%global source0_hash 7af4412e5da8ccec62f4df9288f2f9d30884388285e6e645aef9c033d7f0694a

Name:           nogravity
Version:        2.00
Release:        51%{?dist}
Summary:        Space shooter in 3D
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.realtech-vr.com/nogravity/
Source0:        http://downloads.sourceforge.net/%{name}/rt-%{name}-src.zip
Source2:        %{name}.desktop
Source3:        %{name}.png
Source4:        nogravity--Makefile.am
Source5:        nogravity--bootstrap
Source6:        nogravity--configure.in
Source7:        nogravity.sh
Source8:        %{name}.appdata.xml
Patch0:         nogravity--snd_sdlmixer_c-powerpc-fix.diff
Patch1:         nogravity--fullscreen_as_option.patch
Patch2:         nogravity--fixed_path_to_game_data.diff
Patch3:         nogravity--64-bit.patch
Patch4:         nogravity--cvs.patch
Patch5:         nogravity--openal.patch
# See: https://www.redhat.com/archives/fedora-games-list/2007-June/msg00000.html
Patch6:         nogravity--README.patch
Patch7:         nogravity--bufer-overflows.patch
Patch8:         nogravity--strcpy-abuse.patch
Patch9:         nogravity-2.00-rhbz699274.patch
Patch10:        nogravity-2.00-libpng15.patch
Patch11:        0001-v3xscene-Remove-some-unused-code.patch
Patch12:        0002-rlx32-Stop-using-MaxExtentableObjet.patch
Patch13:        nogravity-2.00-stdint_h.patch
Patch14:        nogravity--gcc6.patch
Patch15:        nogravity-2.00-build-fixes.patch
Patch16:        nogravity-2.00-c23.patch
Requires:       %{name}-data = %{version}
BuildRequires:  make gcc-c++
BuildRequires:  SDL_mixer-devel openal-soft-devel libpng-devel libvorbis-devel
BuildRequires:  automake desktop-file-utils libappstream-glib
Requires:       hicolor-icon-theme glx-utils

%description
No Gravity is a fantastic and futuristic universe made of five
intergalactic worlds. An arcade type game with great play-ability,
where it is easy to plunge into space battles against space-fighters,
space stations and more!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -c
cp %{SOURCE4} ./src/Linux/Makefile.am
cp %{SOURCE5} ./src/Linux/bootstrap
cp %{SOURCE6} ./src/Linux/configure.in
sed -i 's/\r//g' GNU.TXT README.TXT
pushd src/Linux
sh bootstrap
popd

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
pushd src/Linux

%configure --enable-sound=sdl_mixer --disable-opengl
make %{?_smp_mflags} LDADD=-lz
mv %{name} %{name}-software

make distclean

%configure --enable-sound=openal --enable-opengl
make %{?_smp_mflags} LDADD=-lz
mv %{name} %{name}-opengl

popd

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -m 755 src/Linux/%{name}-software $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/Linux/%{name}-opengl   $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 %{SOURCE7} $RPM_BUILD_ROOT%{_bindir}/%{name}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -p -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc README.TXT
%license GNU.TXT
%{_bindir}/%{name}*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%changelog
%autochangelog
