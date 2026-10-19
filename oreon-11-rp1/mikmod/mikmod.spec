%global source0_hash 465e99d89d762608b7d0c0a103a58eec68c8c28ae6bbd196354c13433e40d20a
Name:           mikmod
Version:        3.2.10
Release:        1%{?dist}
Summary:        Console music module player
License:        GPL-2.0-only AND LicenseRef-Callaway-LGPLv2+
URL:            http://mikmod.sourceforge.net/
Source0:        http://downloads.sourceforge.net/mikmod/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  libmikmod-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
