%global source0_hash 640b4823b6f24ada6d417311bfd6263ab13be2422573c3b4ad4352223b535d88

Name:           tintin 
Version:        2.02.61
Release:        1%{?dist}
Summary:        TinTin++, aka tt++, is a free MUD client
License:        GPL-3.0-only
URL:            http://%{name}.mudhalla.net/
Source0:        https://github.com/scandum/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
# Build
BuildRequires:  bash
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  hostname
BuildRequires:  make
BuildRequires:  sed
# Runtime
BuildRequires:  gnutls-devel
BuildRequires:  ncurses-devel
BuildRequires:  pcre2-devel
BuildRequires:  zlib-devel

%description
TinTin++, aka tt++, is a free MUD client for Mac OS X, Linux, and Windows. The
Windows port named WinTin++ (using the PuTTY terminal) is available for
those who do not use Cygwin (A Linux/Unix emulator for Windows) and runs on
Windows XP, Windows Vista, and Windows 7. Besides MUDs, TinTin++ also works
well with MUSH, Rogue, BBS, and Linux servers.

%package doc
Summary:        TinTin++ documentation and examples
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
BuildArch:      noarch

%description doc
TinTin++, aka tt++, MUD client documentation and examples.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n tt
find . -type f -exec chmod 644 {} +
chmod a+x src/configure

%build
cd src
%configure
%make_build

%install
cd src
%make_install

%files
%license COPYING
%doc CREDITS FAQ README TODO
%doc mods
%{_bindir}/tt++

%files doc
%license COPYING
%doc SCRIPTS
%doc docs/*

%changelog
%autochangelog
