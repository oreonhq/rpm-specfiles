
Name:		console-setup
Version:	1.245
Release:	3%{?dist}
Summary:	Tools for configuring the console using X Window System key maps

# For a breakdown of the licensing, see COPYRIGHT, copyright, copyright.fonts and copyright.xkb
License:	GPL-2.0-or-later AND MIT AND LicenseRef-Public-Domain
URL:		http://packages.debian.org/cs/sid/console-setup
Source0:	http://ftp.de.debian.org/debian/pool/main/c/%{name}/%{name}_%{version}.tar.xz

# Fixes installing paths to Fedora style
Patch0:		console-setup-1.76-paths.patch
# Fixes FSF address, sent to upstream
Patch1:		console-setup-1.76-fsf-address.patch
# Removes Caps_Lock to CtrlL_Lock substitution
Patch2:		console-setup-1.84-ctrll-lock.patch

Requires:	kbd
# require 'xkeyboard-config' to have X Window keyboard descriptions?

BuildRequires:	perl-generators
BuildRequires:	perl(encoding) perl(open)
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
%setup -q
%autopatch -p1

cp -a --remove-destination debian/copyright COPYRIGHT
cp -a --remove-destination debian/changelog CHANGES

%build
make build-linux


%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT install-linux
# we don't want another set of keyboard descriptions, we want to use descriptions from
# xkeyboard-config (require it?), so removing it
# or maybe have these from tarball it in optional subpackage?
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.245-3
- Import
