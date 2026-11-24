# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2042e268b085ad900f2f9863715d67fadb95b8994554f10d407fc14f224b73ae
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:		console-setup
Version:	1.249
Release:	1%{?dist}
Summary:	Tools for configuring the console using X Window System key maps

License:	GPL-2.0-or-later AND MIT AND LicenseRef-Oreon-Public-Domain
URL:		http://packages.debian.org/cs/sid/console-setup
Source0:	https://deb.debian.org/debian/pool/main/c/%{name}/%{name}_%{version}.tar.xz

Patch0:		console-setup-1.76-paths.patch
Patch1:		console-setup-1.76-fsf-address.patch
Patch2:		console-setup-1.84-ctrll-lock.patch

Requires:	kbd

BuildRequires: oreon-rpm-macros
BuildRequires:	perl-generators
BuildRequires:	perl(encoding)
BuildRequires:	perl(open)
BuildRequires:	make
BuildArch:	noarch

%description
This package provides the console with the same keyboard configuration
scheme that X Window System has. Besides the keyboard, the package configures
also the font on the console.  It includes a rich collection of fonts and
supports several languages that would be otherwise unsupported on the console
(such as Armenian, Georgian, Lao and Thai).

%package -n bdf2psf
Summary:	Generate console fonts from BDF source fonts

%description -n bdf2psf
This package provides a command-line converter that can be used in scripts
to build console fonts from BDF sources automatically. The converter comes
with a collection of font encodings that cover many of the world's
languages. The output font can use a different character encoding from the
input. When the source font does not define a glyph for a particular
symbol in the encoding table, that glyph position in the console font is
not wasted but used for another symbol.

%prep
%oreon_sha256
%setup -q -n %{name}
%autopatch -p1

cp -a --remove-destination debian/copyright COPYRIGHT
cp -a --remove-destination debian/changelog CHANGES

%build
make build-linux

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT install-linux
rm -rf $RPM_BUILD_ROOT/etc/console-setup

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -pm644 man/bdf2psf.1 $RPM_BUILD_ROOT%{_mandir}/man1/

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p Fonts/bdf2psf $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/bdf2psf
cp -a Fonts/fontsets Fonts/*.equivalents Fonts/*.set \
	$RPM_BUILD_ROOT%{_datadir}/bdf2psf/

%files
%doc README COPYRIGHT CHANGES copyright.fonts copyright.xkb Fonts/copyright
%{_bindir}/ckbcomp
%{_bindir}/setupcon
%config(noreplace) %{_sysconfdir}/default/console-setup
%config(noreplace) %{_sysconfdir}/default/keyboard
%{_datadir}/consolefonts
%{_datadir}/consoletrans
%{_mandir}/*/*

%files -n bdf2psf
%{_bindir}/bdf2psf
%{_mandir}/man1/bdf2psf.1*
%{_datadir}/bdf2psf
%license GPL-2

%changelog
%autochangelog
