%global source0_hash 6055a2abccc64296e1c38f9652f2056d3a3c096538e164b8b9526e10b486b3d8

Summary:  Adjust the volume of audio files to a standard level
Name:     normalize
Version:  0.7.7
Release:  35%{?dist}
URL:      http://normalize.nongnu.org/
License:  GPL-2.0-or-later AND LGPL-2.1-or-later
Source0:  http://download.savannah.gnu.org/releases/normalize/normalize-%{version}.tar.gz
Source1:  http://download.savannah.gnu.org/releases/normalize/normalize-%{version}.tar.gz.sig
# https://pgp.mit.edu/pks/lookup?op=get&search=0xAFC8519A83FE7486
# https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x659d42b60f3b86ea4d37777eafc8519a83fe7486
Source2:  0xAFC8519A83FE7486.gpg
# fix audiofile detection
Patch0:   normalize-0.7.7-audiofile.patch
# fix configure regeneration with autoreconf
Patch1:   normalize-0.7.7-autoreconf.patch
# fix building without XMMS
Patch2:   normalize-0.7.7-no-xmms.patch
# fix building with GCC 15
Patch3:   normalize-0.7.7-gcc15.patch

BuildRequires:  audiofile-devel
BuildRequires:  flac
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  lame
BuildRequires:  libtool
BuildRequires:  libmad-devel
BuildRequires:  mpg123
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  vorbis-tools
# Explicit, because won't be detected automatically.
Requires:       flac
Requires:       lame
Requires:       mpg123
Requires:       vorbis-tools

%description
normalize is a tool for adjusting the volume of audio files to a
standard level. This is useful for things like creating mixed CDs
and mp3 collections, where different recording levels on different
albums can cause the volume to vary greatly from song to song.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%autosetup -p1
touch AUTHORS ChangeLog
autoreconf -fi
for i in THANKS doc/normalize-mp3.1; do
    iconv -f ISO-8859-1 -t UTF8 "$i" > "$i.UTF8"
    touch -r "$i" "$i.UTF8"
    mv "$i.UTF8" "$i"
done

%build
%configure --disable-xmms --with-audiofile --disable-static
%make_build

%install
%make_install

%find_lang %{name}

%check
make check

%files -f %{name}.lang
%license COPYING
%doc README NEWS THANKS TODO
%{_bindir}/normalize
%{_bindir}/normalize-mp3
%{_bindir}/normalize-ogg
%{_mandir}/man1/normalize.1.*
%{_mandir}/man1/normalize-mp3.1.*

%changelog
%autochangelog
