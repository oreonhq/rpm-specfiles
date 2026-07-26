%global source0_hash bad368c471d7f4c371fbe8f5da24872f9e3ad609ddb7dad0e015c960c88b3aa9

# ***********************************************************************
# *                                                                     *
# *            Star Traders: A Game of Interstellar Trading             *
# *               Copyright (C) 1990-2024, John Zaitseff                *
# *                                                                     *
# ***********************************************************************

# Author: John Zaitseff <J.Zaitseff@zap.org.au>
# $Id: 60b7467370a91b8d874bd0a0bff37b4ac2a267b1 $

# This file is distributed under the same licence as Star Traders itself:
# the GNU General Public License, version 3 or later.

Name:           trader
Version:        7.20
Release:        5%{?dist}
Summary:        Star Traders, a simple game of interstellar trading
License:        GPL-3.0-or-later
Url:            https://www.zap.org.au/projects/trader/
Source0:        https://ftp.zap.org.au/pub/trader/unix/trader-%{version}.tar.xz
Source1:        https://ftp.zap.org.au/pub/trader/unix/trader-%{version}.tar.xz.sig
Source2:        https://www.zap.org.au/~john/pubkey.gpg

BuildRequires:  gcc make gettext pkgconfig(ncurses) desktop-file-utils libappstream-glib gperf gnupg2
Provides:       bundled(gnulib)

%description
Star Traders is a simple game of interstellar trading, where the objective
is to create companies, buy and sell shares, borrow and repay money, in
order to become the wealthiest player (the winner).

%global _hardened_build 1

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%build
%configure
%make_build

%install
%make_install
%find_lang %{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files -f %{name}.lang
%doc README NEWS
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_metainfodir}/*.metainfo.xml

%changelog
%autochangelog
