%global source0_hash 942b588fb623ea58ce8cac8844e6ff2829ad4bc9b4c163bba58e3fa9ebc15608

Summary: FUSE filesystem to transcode FLAC to MP3 on the fly
Name: mp3fs
Version: 1.1.1
Release: 16%{dist}
# Automatically converted from old format: GPLv3+ and GFDL - review is highly recommended.
License: GPL-3.0-or-later AND LicenseRef-Callaway-GFDL
Source0: https://github.com/khenriks/mp3fs/releases/download/v%{version}/mp3fs-%{version}.tar.gz
URL: https://khenriks.github.io/mp3fs/
# While mp3fs does encode to MP3, it is a consumer, not a provider
#Provides: mp3encoder
# While mp3fs does not strictly require the fuse cli (which does not provide
# the fuse libraries), mp3fs is fairly useless without it.
Requires: fuse
BuildRequires: make
BuildRequires: fuse-devel lame-devel flac-devel libid3tag-devel gcc-c++
BuildRequires: libvorbis-devel
BuildRequires: zlib-devel

%description
MP3FS is A read-only FUSE file-system which trans-codes audio formats (currently
FLAC/OGG) to MP3 on the fly when opened and read. This was written to enable me
to use my FLAC collection with software and/or hardware which only understands
MP3. e.g. "GMediaServer" to a Netgear MP101 mp3 player.

It is also a novel alternative to traditional mp3 encoder applications. Just
use your favorite file browser to select the files you want encoded and copy
them somewhere!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 

%build
%configure
%{make_build} LDFLAGS="$RPM_LD_FLAGS -lm" V=1

%install
%make_install

%files
%{!?_licensedir:%global license %%doc}
%license COPYING COPYING.DOC
%doc README.md INSTALL.md NEWS.md
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
%autochangelog
