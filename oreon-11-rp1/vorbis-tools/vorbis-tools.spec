%global source0_hash a1fe3ddc6777bdcebf6b797e7edfe0437954b24756ffcc8c6b816b63e0460dde

Summary:	The Vorbis General Audio Compression Codec tools
Name:		vorbis-tools
Version:	1.4.3
Release:	4%{?dist}
Epoch:		1
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		https://www.xiph.org/
Source:        https://ftp.osuosl.org/pub/xiph/releases/vorbis/%{name}-%{version}.tar.gz

# http://lists.xiph.org/pipermail/vorbis-dev/2021-January/020538.html
# http://lists.xiph.org/pipermail/vorbis-dev/2013-May/020336.html
Patch1:		vorbis-tools-1.4.2-man-page.patch

BuildRequires:	flac-devel
BuildRequires:	gettext
BuildRequires:	gcc
BuildRequires:	libao-devel
BuildRequires:	libcurl-devel
BuildRequires:	libvorbis-devel
BuildRequires:	make
BuildRequires:	speex-devel
Obsoletes:	vorbis < %{epoch}:%{version}-%{release}
Provides:	vorbis = %{epoch}:%{version}-%{release}

# source code of vorbis-tools contains a copy of vasnprintf.c from gnulib
Provides: bundled(gnulib)

%description
Ogg Vorbis is a fully open, non-proprietary, patent- and royalty-free,
general-purpose compressed audio format for audio and music at fixed
and variable bitrates from 16 to 128 kbps/channel.

The vorbis package contains an encoder, a decoder, a playback tool, and a
comment editor.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1


%build
# fix FTBFS if "-Werror=format-security" flag is used (#1025257)
export CFLAGS="$RPM_OPT_FLAGS -Wno-error=format-security"

# uncomment this when debugging
#CFLAGS="$CFLAGS -O0"

%configure
%make_build


%install
%make_install
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}*
%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING README ogg123/ogg123rc-example
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.3-4
- Prepare for Oreon 11 (RP1)
