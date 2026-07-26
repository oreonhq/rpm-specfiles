%global source0_hash 214c10aa3019807a1eb26b2c709592f63dbcc00b72985aa86a4fb7ac3cd8b901

Name:           mikmod
Version:        3.2.9
Release:        4%{?dist}
Summary:        Console music module player

# Automatically converted from old format: GPLv2 and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-LGPLv2+
URL:            http://mikmod.sourceforge.net/
Source0:        http://downloads.sourceforge.net/mikmod/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  libmikmod-devel
BuildRequires:  git-core

%description
MikMod is one of the best and most well known MOD music file players
for UNIX-like systems.  This particular distribution is intended to
compile fairly painlessly in a Linux environment. MikMod uses the OSS
/dev/dsp driver including all recent kernels for output, and will also
write .wav files. Supported file formats include MOD, STM, S3M, MTM,
XM, ULT, and IT.  The player uses ncurses for console output and
supports transparent loading from gzip/pkzip/zoo archives and the
loading/saving of playlists.

Install the mikmod package if you need a MOD music file player.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p2 -Sgit

%build
%configure
%make_build

%install
%make_install INSTALL="install -p"

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
