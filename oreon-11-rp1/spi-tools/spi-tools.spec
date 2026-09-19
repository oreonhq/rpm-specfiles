%global source0_hash f6a93ae4f729d42e9200ba491cf9088202b63cb88e011cf6bcb0a7d12432cdc4

Name:		spi-tools
Version:	1.0.2
Release:	8%{?dist}
Summary:	Simple command line tools to help using Linux spidev devices

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		https://github.com/cpb-/spi-tools/
Source0:	https://github.com/cpb-/spi-tools/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		0001-Don-t-override-the-compiler-flags-with-nonsense-ones.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	help2man

%description
This package contains spi-config and spi-pipe, simple command line tools to
help using Linux spidev devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/spi-config
%{_bindir}/spi-pipe
%{_mandir}/man1/spi-config.1*
%{_mandir}/man1/spi-pipe.1*

%changelog
%autochangelog
