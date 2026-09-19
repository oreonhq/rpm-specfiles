%global source0_hash 2b6622a7b2ea6bb38c70bda4af76f93633916fb568217beca91559340b914e4d

Name:		alsamixergui
Summary:	GUI mixer for ALSA sound devices
Version:	0.9.0
Release:	0.48.rc2%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
# This is where the source used to live, but this upstream is dead.
# Source0:	ftp://www.iua.upf.es/pub/mdeboer/projects/alsamixergui/%%{name}-%%{version}rc1-2.tar.gz
# This tarball was taken from Debian, and is the most recent version as far as I know.
Source0:	http://ftp.de.debian.org/debian/pool/main/a/alsamixergui/alsamixergui_0.9.0rc2-1.orig.tar.gz
Source1:	alsamixergui.desktop
Source2:	alsamixergui.png
# This site is dead and gone.
URL:		ftp://www.iua.upf.es/pub/mdeboer/projects/alsamixergui
BuildRequires:  gcc-c++
BuildRequires:	fltk-devel, libstdc++-devel
BuildRequires:	alsa-lib-devel, desktop-file-utils
BuildRequires:	libtool
BuildRequires: make
# This is debian's patch, taken 2013-04-01
Patch0:		alsamixergui_0.9.0rc2-1-9.1.diff
Patch1:		alsamixergui-strsignal.patch
Patch2:		alsamixergui-autoconf-cxx.patch

%description
alsamixergui is a FLTK based frontend for alsamixer. It is written
directly on top of the alsamixer source, leaving the original source
intact, only adding a couple of ifdefs, and some calls to the gui
part, so it provides exactly the same functionality, but with a
graphical userinterface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}rc2-1.orig
%patch -P0 -p1 -b .debian
%patch -P1 -p1 -b .strsignal
%patch -P2 -p1
autoreconf -i
chmod +x configure

%build
%configure
make %{?_smp_mflags}

%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

%files
%doc README AUTHORS COPYING ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
