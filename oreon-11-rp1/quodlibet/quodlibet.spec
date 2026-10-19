%global source2_hash dc3278286afa2c11f66fc0f741e1a69550f43edf85b0bf57ed803b61ba5a2819
%global source1_hash 6b1d558c8ccda6f5392b17567cfe1ee13be6cbbb277d4d43678919c3b5b03f01
%global source0_hash b77ce02a3144133acc37489dc8cea2afc71a22ce0ed1e780fe92072012f03dd1
Name:		quodlibet
Version:	4.7.1
Release:        1%{?dist}
Summary:        A music management program
License:	GPL-2.0-or-later
URL:		https://quodlibet.readthedocs.org/en/latest/
Source0:        https://github.com/quodlibet/quodlibet/releases/download/release-%{version}/quodlibet-%{version}.tar.gz
Source1:	https://github.com/quodlibet/quodlibet/releases/download/release-%{version}/quodlibet-%{version}.tar.gz.sig
Source2:	https://keys.openpgp.org/vks/v1/by-fingerprint/E0AA0F031DBD80FFBA57B06D5A62D0CAB6264964
Source3:	README.fedora
Patch:		https://github.com/quodlibet/quodlibet/commit/93d2de93663245bd3b2aadc2ea6085991cd7da35.patch
BuildArch:	noarch
Requires:	exfalso = %{version}-%{release}
Requires:	gstreamer1
Requires:	gstreamer1-plugins-base
Requires:	gstreamer1-plugins-good
Requires:	python3-dbus
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-quodlibet = %{version}-%{release}
# /oreon:deps
%package -n       python3-quodlibet+plugins
Summary:        Metapackage for python3-quodlibet plugins extras
Requires:       python3-quodlibet = %{version}-%{release}
Requires:       python3dist(musicbrainzngs) >= 0.0.0
Requires:       python3dist(musicbrainzngs) < 1.0.0
Requires:       python3dist(soco) >= 0.27
Requires:       python3dist(soco) < 0.28
Requires:       python3dist(pypresence) >= 4.2.1
Requires:       python3dist(pypresence) < 5.0.0
Requires:       python3dist(paho-mqtt) >= 1.6.1
Requires:       python3dist(paho-mqtt) < 2.0.0
Provides:       python3dist(quodlibet[plugins]) = %{version}-%{release}

%description -n python3-quodlibet+plugins
Metapackage for python3-quodlibet plugins extras.

%description
Quod Libet is a music management program. It provides several different ways
to view your audio library, as well as support for Internet radio and
audio feeds. It has extremely flexible metadata tag editing and searching
capabilities.
Supported file formats include Ogg Vorbis, MP3, FLAC, MOD/XM/IT, Musepack,
Wavpack, and MPEG-4 AAC.

%package -n exfalso
Summary: Tag editor for various music files
Requires:	adwaita-icon-theme
Requires:	gtk3 >= 3.18
Requires:	hicolor-icon-theme
Requires:	libsoup >= 2.44
Requires:	pkgconfig
Requires:	python3-gobject >= 3.18
Requires:	python3 >= 3.5
Requires:	python3-mutagen >= 1.14
Requires:	python3-feedparser
Requires:	python3-musicbrainzngs >= 0.6
%description -n exfalso
Ex Falso is a tag editor with the same tag editing interface as Quod Libet,
but it does not play files.
Supported file formats include Ogg Vorbis, MP3, FLAC, MOD/XM/IT, Musepack,
Wavpack, and MPEG-4 AAC.

%package zsh-completion
Summary: zsh completion files for %{name}
Requires: quodlibet = %{version}-%{release}
Requires: zsh
%description zsh-completion
This package installs %{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p 1

install -pm 0644 %{S:3} .

%build

%pyproject_wheel
%install
%pyproject_install
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications		\
	--delete-original					\
	%{buildroot}%{_datadir}/applications/io.github.quodlibet.QuodLibet.desktop
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications		\
	--delete-original					\
	%{buildroot}%{_datadir}/applications/io.github.quodlibet.ExFalso.desktop
%find_lang quodlibet
%oreon_autofiles exfalso usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -m "not network"
%files
%files -n exfalso -f %{oreon_filedir}/exfalso.list
%files -n quodlibet-zsh-completion -f %{oreon_filedir}/quodlibet-zsh-completion.list

%changelog

%autochangelog
