%global source0_hash 2042e268b085ad900f2f9863715d67fadb95b8994554f10d407fc14f224b73ae
Name:		console-setup
Version:	1.249
Release:        1%{?dist}
Summary:        Tools for configuring the console using X Window System key maps
License:	GPL-2.0-or-later AND MIT AND LicenseRef-Public-Domain
URL:		http://packages.debian.org/cs/sid/console-setup
Source0:        https://deb.debian.org/debian/pool/main/c/%{name}/%{name}_%{version}.tar.xz
Patch0:		console-setup-1.76-paths.patch
Patch1:		console-setup-1.76-fsf-address.patch
Patch2:		console-setup-1.84-ctrll-lock.patch
Requires:	kbd
BuildArch:	noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(encoding)
BuildRequires:  perl(open)
BuildRequires:  perl-generators
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n console-setup
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
%oreon_autofiles bdf2psf usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n bdf2psf -f %{oreon_filedir}/bdf2psf.list

%changelog

%autochangelog
