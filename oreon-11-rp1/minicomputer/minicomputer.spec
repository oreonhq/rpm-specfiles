%global source0_hash b4d5f0be2b9af7ffcd2015d00c8e582959ce8e6d3b039f90f5551477b12d67e2

Name:		minicomputer
Version:	1.41
Release:	43%{?dist}
Summary:	Software Synthesizer
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://minicomputer.sourceforge.net/
Source0:	http://downloads.sourceforge.net/minicomputer/MinicomputerV%{version}.tar.gz
Source1:	%{name}.desktop
# DSO linking fix. Sent upstream by email.
Patch0:		%{name}-linking.patch
# GCC 4.7 fix
Patch1:		%{name}-gcc47.patch
# Build with Python 3
Patch2:		%{name}-build-python3.patch

BuildRequires:	gcc-c++
BuildRequires:	alsa-lib-devel
BuildRequires:	desktop-file-utils
BuildRequires:	fltk1.3-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	liblo-devel
BuildRequires:	/usr/bin/scons

Requires:	hicolor-icon-theme

%description
Minicomputer is a standalone Linux software synthesizer for creating 
experimental electronic sounds as its often used in but not limited to
Industrial music, IDM, EBM, Glitch, sound design and minimal electronic. It is
monophonic but can produce up to 8 different sounds at the same time. It uses
Jack as realtime audio infrastructure and can be controlled via Midi.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n MinicomputerV%{version}
%patch -P0 -p1 -b .linking
%patch -P1 -p1 -b .%{name}-gcc47.patch
%patch -P2 -p1 -b .%{name}-build-python3.patch

# Fix optflags
# SSE instruction set, which provides improved functionality, is only available in these archs:
%ifnarch %{ix86} x86_64 ia64
sed -i "s|\(^env.Append(CCFLAGS =\).*|\1 ['%{optflags} -Wno-incompatible-pointer-types'.split() ])|" SConstruct
%else
sed -i "s|\(^env.Append(CCFLAGS =\).*|\1 ['%{optflags} -Wno-incompatible-pointer-types'.split(),'-msse','-mfpmath=sse' ])|" SConstruct
%endif
sed -i "s|\(^guienv.Append(CPPFLAGS =\).*|\1 ['%{optflags} -Wno-incompatible-pointer-types'.split() ])|" SConstruct

%build
scons %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -pm 755 %{name}{,CPU} %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install				\
--dir=%{buildroot}%{_datadir}/applications	\
%{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -pm 644 %{name}.xpm \
	%{buildroot}%{_datadir}/icons/hicolor/32x32/apps

%files
%doc CHANGES README minicomputerManual.pdf factoryPresets
%license COPYING
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm

%changelog
%autochangelog
