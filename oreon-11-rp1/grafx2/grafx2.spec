%global source3_hash bba50f327163d40b1014f5affc8042137f37b200dae50a4f0fe56b5769b3940f
%global source1_hash a10384a69de0ae4cbc6a21b2bf598e6191da9e8b2847f7aeda66ec18d66e27b9
%global source0_hash bba50f327163d40b1014f5affc8042137f37b200dae50a4f0fe56b5769b3940f
%global recoilver 6.1.0
%global sixfivezerotwover 0.1
Name:		grafx2
Version:	2.9
Release:        1%{?dist}
Summary:        A bitmap paint program specialized in 256 color drawing
URL:		http://grafx2.chez.com/
License:	GPL-2.0-only AND CECILL-2.0
Source0:        grafX2-v%{version}-clean.tar.bz2
Source1:	https://sourceforge.net/projects/recoil/files/recoil/%{recoilver}/recoil-%{recoilver}.tar.gz
Source2:	grafx2.appdata.xml
Source3:	https://github.com/redcode/6502/releases/download/v%{sixfivezerotwover}/6502-v%{sixfivezerotwover}.tar.xz
Source4:	6502-RELICENSE
Source5:	realpath-linux.c
Patch0:		grafX2-v2.8-recoil6.patch
Patch1:		grafX2-v2.8-fix-tiff-saving.patch
Patch2:		grafX2-v2.8-fix-ttf.patch
Patch3:		grafX2-v2.8-fix-coords.patch
Provides:	bundled(recoil) = %{recoilver}
Provides:	bundled(6502) = %{sixfivezerotwover}
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
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
mkdir -p %{buildroot}%{_metainfodir}
cp %{SOURCE2} %{buildroot}%{_metainfodir}
pushd %{buildroot}%{_bindir}
ln -s grafx2-sdl2 grafx2
popd
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/grafx2.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
