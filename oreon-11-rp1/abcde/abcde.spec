%global source1_hash d9a8bc46943d7f9b7ca5f4a32dde188a457572094df0316612b0dad9b987f9e9
%global source0_hash 046cd0bba78dd4bbdcbcf82fe625865c60df35a005482de13a6699c5a3b83124
Name:           abcde
Version:        2.9.3
Release:        20%{?dist}
Summary:        A Better CD Encoder
License:        GPL-2.0-or-later
URL:            https://abcde.einval.com/
Source0:        https://abcde.einval.com/download/%{name}-%{version}.tar.gz
Source1:        https://abcde.einval.com/download/%{name}-%{version}.tar.gz.sign
Source2:        587979573442684E.gpg
Patch0:         %{name}-normalize.patch
Patch1:         https://bugzilla.redhat.com/attachment.cgi?id=1748056#/abcde-gnudb.patch
BuildArch:      noarch
Requires:       cd-discid
Requires:       %{_bindir}/hostname
Requires:       wget
Requires:       which
Requires:       cdparanoia
Requires:       vorbis-tools
Recommends:     icedax
Recommends:     flac
Suggests:       cd-discid
Suggests:       cdrdao
Suggests:       ImageMagick
Suggests:       lame
Suggests:       libcdio-paranoia
Suggests:       normalize
Suggests:       opus-tools
Suggests:       speex-tools
Suggests:       twolame
Suggests:       wavpack
Suggests:       vorbisgain
Suggests:       %{_bindir}/eyeD3
Conflicts:      python-eyed3 < 0.7.0
# oreon:deps
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
%description
abcde is a front end command line utility (actually, a shell script)
that grabs audio tracks off a CD, encodes them to various formats, and
tags them, all in one go.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%autosetup
mv examples/cue2discid .
sed -i -e 's|bin/python\b|bin/python3|' cue2discid
chmod -c -x examples/musicbrainz-get-tracks

%build

%install
%make_install prefix=%{_prefix} sysconfdir=%{_sysconfdir}
rm -r $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version} # handled separately
install -pm 755 cue2discid $RPM_BUILD_ROOT%{_bindir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
