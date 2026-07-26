%global source0_hash 7d1f0bbd0d7d303fc77c6b9549b61708d7a83b4dc007818011b1f55d1fa922ba

Name:       bristol
Version:    0.60.11
Release:    33%{dist}
Summary:    Synthesizer emulator

License:    GPL-2.0-or-later
URL:        http://bristol.sourceforge.net
Source0:    http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:    %{name}.desktop
Patch0:     bristol-0.60.9-CVE-2010-3351.patch
Patch1:     bristol-0.60.11-fix-build-with-alsa.patch
Patch2:     bristol-0.60.11-fix-common.patch
Patch3: bristol-c99.patch

BuildRequires: gcc autoconf automake libtool
BuildRequires: libX11-devel alsa-lib-devel jack-audio-connection-kit-devel desktop-file-utils
BuildRequires: make

%description
Bristol is an emulation package for a number of different 'classic'
synthesizers including additive and subtractive and a few organs.
The application consists of the engine, which is called bristol,
and its own GUI library called brighton that represents all the emulations.

%package devel
Summary:    %{summary}
Requires:   %{name} = %{version}

%description devel
This package contains the development libraries for Bristol.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

find ./bitmaps/ -name '*.gz' | xargs chmod -x
chmod -x ./memory/profiles/*
find . -name '*.c' | xargs chmod -x
find . -name '*.h' | xargs chmod -x
find . -name '*.xbm' | xargs chmod -x
find . -name '*.svg' | xargs chmod -x
chmod -x NEWS COPYING* README AUTHORS ChangeLog
chmod -x memory/mixer/default/memory memory/mini/readme.txt

# Only x86_64 is optimised for SSE, non x86 platforms don't have SSE
%ifnarch x86_64
sed -i.sse 's/-msse -mfpmath=sse //g' bristol/Makefile.am
sed -i.sse 's/-msse -mfpmath=sse //g' bristol/Makefile.in
%endif

%build
export CFLAGS="$CFLAGS -std=gnu17"
autoreconf -if
./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-static=no --disable-version-check
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm INSTALL
mkdir -p -m 0755 $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p -m 0755 $RPM_BUILD_ROOT%{_datadir}/applications
install -p -m 0644 bitmaps/bicon.svg $RPM_BUILD_ROOT%{_datadir}/pixmaps/bristol.svg
desktop-file-install \
    --mode 0644 \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications/ \
    %{SOURCE1}

%ldconfig_scriptlets

%files
%license COPYING*
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/bristol
%{_datadir}/pixmaps/*
%{_datadir}/applications/bristol.desktop
%{_libdir}/lib*.so.*
%{_mandir}/man1/*

%files devel
%{_libdir}/lib*.so

%changelog
%autochangelog
