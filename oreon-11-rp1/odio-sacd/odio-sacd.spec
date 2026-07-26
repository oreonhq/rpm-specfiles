%global source0_hash 4ed0fc92cc9e3472a9ed6888249cbdbb35b21e21a83eea6d00d9b6f2e9e3d085

# disable LTO to workaround ICE in gcc happening randomly on all arches
# https://bugzilla.redhat.com/show_bug.cgi?id=2240371
%global _lto_cflags %nil

%global forgeurl https://github.com/tari01/odio-sacd

Name:           odio-sacd
Version:        23.1.31
Release:        %autorelease
Summary:        Command-line SACD decoder

License:        GPL-3.0-or-later
URL:            https://tari.in/www/software/odio-sacd/
Source:         %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

BuildRequires:  libodiosacd-devel

%description
Odio SACD is a command-line application which takes a Super Audio CD source and
extracts a 24-bit high resolution wave file. It handles both DST and DSD
streams.

The application reads the following input:
- SACD image files (*.iso)
- Sony DSF files (*.dsf)
- Philips DSDIFF files (*.dff)

Supported output sample rates:
- 88.2kHz
- 176.4kHz

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
chmod -x COPYING
sed -i Makefile \
  -e 's/CC =/CC ?=/' \
  -e 's/CFLAGS = -g -O$O/CFLAGS +=/'

%build
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
