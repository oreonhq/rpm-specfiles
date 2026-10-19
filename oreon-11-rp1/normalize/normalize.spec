%global source1_hash 7f894cf15dc2e18d28f8c72dbd0024107cecdee961db47c38071c6266bbd8b37
%global source0_hash 6055a2abccc64296e1c38f9652f2056d3a3c096538e164b8b9526e10b486b3d8
Summary:        Adjust the volume of audio files to a standard level
Name:     normalize
Version:  0.7.7
Release:        1%{?dist}
URL:      http://normalize.nongnu.org/
License:  GPL-2.0-or-later AND LGPL-2.1-or-later
Source0:        http://download.savannah.gnu.org/releases/normalize/normalize-%{version}.tar.gz
Source1:  http://download.savannah.gnu.org/releases/normalize/normalize-%{version}.tar.gz.sig
Source2:  0xAFC8519A83FE7486.gpg
Patch0:   normalize-0.7.7-audiofile.patch
Patch1:   normalize-0.7.7-autoreconf.patch
Patch2:   normalize-0.7.7-no-xmms.patch
Patch3:   normalize-0.7.7-gcc15.patch
Requires:       flac
Requires:       lame
Requires:       mpg123
Requires:       vorbis-tools
# oreon:deps
BuildRequires:  audiofile-devel
BuildRequires:  flac
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  lame
BuildRequires:  libmad-devel
BuildRequires:  libtool
BuildRequires:  mpg123
BuildRequires:  perl(Carp)
BuildRequires:  perl-generators
BuildRequires:  vorbis-tools
# /oreon:deps
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
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
