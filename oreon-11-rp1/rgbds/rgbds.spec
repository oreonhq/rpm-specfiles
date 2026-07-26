%global source0_hash 2be649a6b3c3b4a462e222b3082fa2e1c83142f317ba862b17899f5a25717380

Name:		rgbds
Version:	0.9.0
Release:	4%{?dist}
Summary:	A development package for the Game Boy, including an assembler

License:	MIT
URL:		https://github.com/gbdev/%{name}
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	g++
BuildRequires:	byacc
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	git-core
BuildRequires:	pkgconfig(libpng)

%description
RGBDS (Rednex Game Boy Development System) is a free assembler/linker package
for the Game Boy and Game Boy Color.

It consists of:

* rgbasm (assembler)
* rgblink (linker)
* rgbfix (checksum/header fixer)
* rgbgfx (PNG‐to‐2bpp graphics converter)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git

%build
%make_build Q="" CFLAGS="%{optflags}" VERSION_STRING=""

%install
%make_install PREFIX=%{_prefix} bindir=%{_bindir} mandir=%{_mandir} STRIP="-p" MANMODE="644 -p" Q=""

%files
%{_bindir}/rgbasm
%{_bindir}/rgblink
%{_bindir}/rgbfix
%{_bindir}/rgbgfx
%{_mandir}/man1/rgbasm.1.*
%{_mandir}/man1/rgblink.1.*
%{_mandir}/man1/rgbfix.1.*
%{_mandir}/man1/rgbgfx.1.*
%{_mandir}/man5/rgbds.5.*
%{_mandir}/man5/rgbasm-old.5.*
%{_mandir}/man5/rgbasm.5.*
%{_mandir}/man5/rgblink.5.*
%{_mandir}/man7/rgbds.7.*
%{_mandir}/man7/gbz80.7.*
%license LICENSE
%doc README.md

%changelog
%autochangelog
