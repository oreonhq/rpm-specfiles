%global source0_hash bba50f327163d40b1014f5affc8042137f37b200dae50a4f0fe56b5769b3940f

%global recoilver 6.1.0
%global sixfivezerotwover 0.1

Name:		grafx2
Version:	2.8
Release:	13%{?dist}
Summary:	A bitmap paint program specialized in 256 color drawing
URL:		http://grafx2.chez.com/
# recoil is GPLv2+, grafX2 is GPLv2 only
# two files are CeCILL v2
# 6502 has license permission to be used as GPLv2 in this program, see 6502-RELICENSE
# src/libraw2crtc.*
License:	GPL-2.0-only AND CECILL-2.0
# Source0:	https://gitlab.com/GrafX2/grafX2/-/archive/v%%{version}/grafX2-v%%{version}.tar.bz2
# We need to remove src/realpath.c as there is no license for it.
Source0:	grafX2-v%{version}-clean.tar.bz2
Source1:	https://sourceforge.net/projects/recoil/files/recoil/%{recoilver}/recoil-%{recoilver}.tar.gz
Source2:	grafx2.appdata.xml
Source3:	https://github.com/redcode/6502/releases/download/v%{sixfivezerotwover}/6502-v%{sixfivezerotwover}.tar.xz
# http://pulkomandy.tk/projects/GrafX2/ticket/162
Source4:	6502-RELICENSE
# Replacement file for unlicensed realpath.c
Source5:	realpath-linux.c
Patch0:		grafX2-v2.8-recoil6.patch
# https://gitlab.com/GrafX2/grafX2/-/commit/103fc6bd49ac5e4c34013f056f441686a6c0c019
# https://gitlab.com/GrafX2/grafX2/-/commit/77f24ad3a435a59e5e8a44716cc766f81ab46b23
Patch1:		grafX2-v2.8-fix-tiff-saving.patch
# https://gitlab.com/GrafX2/grafX2/-/commit/7e5daa65a8699f6640bf51272c925f4307164f9f
Patch2:		grafX2-v2.8-fix-ttf.patch
# https://gitlab.com/GrafX2/grafX2/-/commit/a851e49f861c7b9bdf1b89c0dd55b8fc12676009
Patch3:		grafX2-v2.8-fix-coords.patch
BuildRequires:	SDL2-devel, SDL2_image-devel, SDL2_ttf-devel, zlib-devel, libtiff-devel
BuildRequires:	libpng-devel, freetype-devel, libX11-devel, lua-devel, gcc, make
BuildRequires:	fontconfig-devel, desktop-file-utils
Provides:	bundled(recoil) = %{recoilver}
Provides:	bundled(6502) = %{sixfivezerotwover}

%description
GrafX2 is a bitmap paint program inspired by the Amiga programs ​Deluxe Paint
and Brilliance. Specialized in 256-color drawing, it includes a very large
number of tools and effects that make it particularly suitable for pixel
art, game graphics, and generally any detailed graphics painted with a
mouse.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n grafX2-v%{version}
%patch -P0 -p1 -b .r6
%patch -P1 -p1 -b .fix-tiff-saving
%patch -P2 -p1 -b .ttf-fix
%patch -P3 -p1 -b .fix-coords

cp %{SOURCE5} src/realpath.c

sed -i 's|-O$(OPTIM)|%{optflags}|g' src/Makefile
sed -i 's|$(LUALOPT)|$(LUALOPT) %{build_ldflags}|g' src/Makefile

# Use the newer recoil
sed -i 's|RECOILVER = 5.1.1|RECOILVER = %{recoilver}|g' src/Makefile
sed -i 's|RECOILVER=5.1.1|RECOILVER=%{recoilver}|g' 3rdparty/Makefile

cp %{SOURCE4} .

mkdir -p 3rdparty/archives/
cp -a %{SOURCE1} %{SOURCE3} 3rdparty/archives/

%build
cd src
make %{?_smp_mflags} API=sdl2

%install
cd src
make API=sdl2 DESTDIR=%{buildroot} PREFIX=%{_prefix} CP="cp -a" install

# install appdata file
mkdir -p %{buildroot}%{_metainfodir}
cp %{SOURCE2} %{buildroot}%{_metainfodir}

pushd %{buildroot}%{_bindir}
ln -s grafx2-sdl2 grafx2
popd

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/grafx2.desktop

%files
%license LICENSE 6502-RELICENSE
%doc doc/README.txt doc/quickstart.rtf
%{_bindir}/grafx2*
%{_metainfodir}/grafx2.appdata.xml
%{_datadir}/applications/grafx2.desktop
%{_datadir}/grafx2/
%{_datadir}/icons/hicolor/scalable/apps/*

%changelog
%autochangelog
