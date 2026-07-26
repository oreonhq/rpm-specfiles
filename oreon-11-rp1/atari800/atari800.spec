%global source0_hash 3874d02b89d83c8089f75391a4c91ecb4e94001da2020c2617be088eba1f461f

Name:          atari800
Version:       5.2.0
Release:       9%{?dist}
Summary:       An emulator of 8-bit Atari personal computers

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           https://atari800.github.io/
%global ver_ %(echo %{version} | tr . _)
Source0:       https://github.com/%{name}/%{name}/releases/download/ATARI800_%{ver_}/%{name}-%{version}-src.tgz
BuildRequires: gcc
BuildRequires: ncurses-devel, libX11-devel, SDL-devel
BuildRequires: libpng-devel, zlib-devel

%description
Atari800 is an emulator for the 800, 800XL, 130XE and 5200 models of
the Atari personal computer. It can be used on console, FrameBuffer or X11.
It features excellent compatibility, HIFI sound support, artifacting
emulation, precise cycle-exact ANTIC/GTIA emulation and more.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure --docdir=%{_pkgdocdir}
%make_build

%install
%make_install

%files
%{_bindir}/atari800
%{_bindir}/cart
%{_mandir}/man1/atari800.1*
%license %{_pkgdocdir}/COPYING
%doc %{_pkgdocdir}/README.TXT
%doc %{_pkgdocdir}/README
%doc %{_pkgdocdir}/USAGE
%doc %{_pkgdocdir}/NEWS
%exclude %{_pkgdocdir}/INSTALL
%doc DOC/BUGS DOC/CREDITS DOC/ChangeLog DOC/FAQ DOC/HOWTO-*
%doc DOC/LPTjoy.txt DOC/TODO DOC/cart.txt DOC/coverage.txt DOC/pokeysnd.txt
%doc DOC/r_device.txt DOC/rdevice_faq.txt

%changelog
%autochangelog
