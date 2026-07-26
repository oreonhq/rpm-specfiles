%global source0_hash 046cd0bba78dd4bbdcbcf82fe625865c60df35a005482de13a6699c5a3b83124

Name:           abcde
Version:        2.9.3
Release:        20%{?dist}
Summary:        A Better CD Encoder

# previously license field included Public Domain, but FOSSology scan of v2.9.3 did not 
# turn up any public domain dedications other than a reference in an old changelog entry
# to a public domain mention that has since been removed upstream.
License:        GPL-2.0-or-later
URL:            https://abcde.einval.com/
Source0:        https://abcde.einval.com/download/%{name}-%{version}.tar.gz
Source1:        https://abcde.einval.com/download/%{name}-%{version}.tar.gz.sign
# gpg2 --recv-key 0x587979573442684E
# gpg2 --export --export-options export-minimal 0x587979573442684E > 587979573442684E.gpg
Source2:        587979573442684E.gpg
Patch0:         %{name}-normalize.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1916974
Patch1:         https://bugzilla.redhat.com/attachment.cgi?id=1748056#/abcde-gnudb.patch

BuildArch:      noarch
BuildRequires:  %{_bindir}/gpgv2
BuildRequires:  make
BuildRequires:  perl-generators
Requires:       cd-discid
Requires:       %{_bindir}/hostname
Requires:       wget
Requires:       which
# cdparanoia, vorbis-tools for defaults
Requires:       cdparanoia
Requires:       vorbis-tools
# icedax for cd-text
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
# eyeD3 is smaller than id3v2
Suggests:       %{_bindir}/eyeD3
Conflicts:      python-eyed3 < 0.7.0

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

%files
%license COPYING
%doc FAQ README changelog examples/
%config(noreplace) %{_sysconfdir}/abcde.conf
%{_bindir}/abcde
%{_bindir}/abcde-musicbrainz-tool
%{_bindir}/cddb-tool
%{_bindir}/cue2discid
%{_mandir}/man1/abcde.1*
%{_mandir}/man1/cddb-tool.1*

%changelog
%autochangelog
