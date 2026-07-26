%global source0_hash 8f684737a52a75c0a0c465ec26e6a5d0fdc1d495392ea83015aed84563f93e0f

Name:           quake2
Version:        8.60
Release:        3%{?dist}
Summary:        Quake II (Yamagi version)

License:        GPL-2.0-or-later
URL:            http://www.yamagi.org/quake2 
Source0:        https://deponie.yamagi.org/quake2/quake2-%{version}.tar.xz
Source1:        %{name}.desktop

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libcurl-devel
BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  openal-soft-devel
BuildRequires:  SDL2-devel
BuildRequires:  zlib-devel

%description
This package contains the enhanced GPL YamagiQuake2 version of the Quake 2 
engine.
To run the game you will need the original data files from demo or 
full versions.

Full version setup:
Copy the baseq2 folder contents from the CD-ROM/Steam to ~/.yq2/baseq2/ 
(or to use the data files system-wide copy the data files to 
%{_libdir}/games/%{name}/baseq2/)
Enjoy the full version.

Demo version setup:
Get the demo from http://deponie.yamagi.org/quake2/idstuff/q2-314-demo-x86.exe 
and extract it. 
It's just an ordinary, self-extract ZIP file. 
An archiver or even the unzip command can be used. 
copy the extracted folder contents /Install/Data/baseq2/* to ~/.yq2/baseq2/ 
(or to use the data files system-wide copy the data files to 
%{_libdir}/games/%{name}/baseq2/)
Enjoy the demo version.

Not patched full version setup:
If your full version of quake 2 isn't patched you need to do some more steps
Please note that the patch is required for all full versions of the game, 
even the newer ones like Steam. Without it Yamagi Quake II will not work!

Download the patch: 
http://deponie.yamagi.org/quake2/idstuff/q2-3.20-x86-full-ctf.exe
Extract the patch into an empty directory. The patch is just an ordinary 
self-extracting ZIP file. On Windows it can be extracted by double clicking 
on it, on other systems an archiver or even the unzip command can be used.

Now it's time to remove the following files from the extracted patch. 
They're the original executables, documentation and so on. 
They aren't needed anymore:

3.20_Changes.txt
quake2.exe
ref_gl.dll
ref_soft.dll
baseq2/gamex86.dll
baseq2/maps.lst
ctf/ctf2.ico
ctf/gamex86.dll
ctf/readme.txt
ctf/server.cfg
xatrix/gamex86.dll
rogue/gamex86.dll

Copy the pak0.pak file and the video/ sub-directory from your Quake II 
distribution (CD, Steam download, etc) into the baseq2/ sub-directory 
of the extracted patch.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
# Use -std=gnu17 to work around build issues with C23 that gcc 15 defaults to
%global optflags %optflags -std=gnu17

%make_build \
    WITH_RPATH=no \
    WITH_SYSTEMWIDE=yes \
    WITH_SYSTEMDIR='%{_libdir}/games/%{name}'

%install
mkdir -p %{buildroot}%{_bindir}
ln -rs %{_libdir}/games/%{name}/quake2 %{buildroot}%{_bindir}/quake2
ln -rs %{_libdir}/games/%{name}/q2ded %{buildroot}%{_bindir}/q2ded

install -D -p -m 755 release/quake2 \
    %{buildroot}%{_libdir}/games/%{name}/quake2
install -D -p -m 755 release/q2ded \
    %{buildroot}%{_libdir}/games/%{name}/q2ded
install -D -p -m 755 release/ref_gl1.so \
    %{buildroot}%{_libdir}/games/%{name}/ref_gl1.so
install -D -p -m 755 release/ref_gl3.so \
    %{buildroot}%{_libdir}/games/%{name}/ref_gl3.so
install -D -p -m 755 release/ref_gles3.so \
    %{buildroot}%{_libdir}/games/%{name}/ref_gles3.so
install -D -p -m 755 release/ref_soft.so \
    %{buildroot}%{_libdir}/games/%{name}/ref_soft.so
install -D -p -m 755 release/baseq2/game.so \
    %{buildroot}%{_libdir}/games/%{name}/baseq2/game.so
install -D -p -m 644 stuff/yq2.cfg \
    %{buildroot}%{_libdir}/games/%{name}/baseq2/yq2.cfg
install -D -p -m 644 stuff/icon/Quake2.png \
    %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/quake2.png
install -D -p -m 644 stuff/icon/Quake2.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/quake2.svg
install -D -p -m 755 stuff/cdripper.sh \
    %{buildroot}%{_defaultdocdir}/%{name}/examples/cdripper.sh
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%license LICENSE
%doc CHANGELOG README.md
%doc doc/*
%{_bindir}/*
%{_libdir}/games/*
%{_datadir}/icons/hicolor/512x512/apps/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/applications/* 
%{_defaultdocdir}/%{name}/*

%changelog
%autochangelog
