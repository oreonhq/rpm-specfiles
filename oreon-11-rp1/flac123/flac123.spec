%global source0_hash c09676dce51383ce4fe7a553e67f4369918cf40ee6d922e585e50c11bce9e227
%global OWNER flac123
%global PROJECT flac123
%global commit d969f2cc94a6b0ff623c2a64081a3d67b624a39d
%global commitdate 20230811
%global gittag v2.1.1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:		flac123
Version:	2.1.1%{?snapshot:^%{commitdate}git%{shortcommit}}
Release:        1%{?dist}
Summary:        Command-line program for playing FLAC audio files
License:	GPL-2.0-or-later
URL:		https://github.com/flac123/flac123
%if 0%{?snapshot}
Source0:        https://github.com/%{name}/%{name}/archive/%{gittag}/%{name}-2.1.1.tar.gz
%else
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  flac-devel
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  libao-devel
BuildRequires:  libogg-devel
BuildRequires:  make
BuildRequires:  popt-devel
# /oreon:deps
%description
flac123 is a command-line program for playing FLAC audio files.

FLAC (Free Lossless Audio Codec) is an open format for losslessly
compressing audio data.  Grossly oversimplified, FLAC is similar to
Ogg Vorbis, but lossless.

flac123 implements mpg123's 'Remote Control' interface via option -R.
This is useful if you're writing a frontend to flac123 which needs a
consistent, reliable interface to control playback.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?snapshot}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1
%endif

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
