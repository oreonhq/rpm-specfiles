%global source0_hash dd6db051cad972bcac25d47b4a9e40e217bb548a1f16328eddbb4e66613530ec

Name:           vorbisgain
Version:        0.37
Release:        %autorelease
Summary:        Adds tags to Ogg Vorbis files to adjust the volume

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://sjeng.org/vorbisgain.html
Source0:        https://sjeng.org/ftp/vorbis/%{name}-%{version}.tar.gz
Patch0:         vorbisgain-spelling.patch
Patch1:         001-fprintf_fix.patch
Patch2:         vorbisgain-c99.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libvorbis-devel
BuildRequires:  libogg-devel

%description
VorbisGain is a utility that uses a psychoacoustic method to correct the
volume of an Ogg Vorbis file to a predefined standardized loudness.

It needs player support to work. Non-supporting players will play back
the files without problems, but you'll miss out on the benefits.
Nowadays most good players such as ogg123, xmms and mplayer are already
compatible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure --enable-recursive
%make_build

%install
%make_install

%files
%doc NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
%autochangelog
