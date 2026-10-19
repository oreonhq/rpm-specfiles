%global source2_hash fe33190be319f4369b57b30da6d305f9c5037a8c858d574bd7b6797ad2f9ee79
%global source1_hash a57969ae6dfff34256e21f0606967260c4abeafdd4f8d1154aad50e2183c578e
%global source0_hash 541d1180dde04173c071d5c59eaf72a6572f8dfc8065e184eaf7d14bccd0257d
Name:           trader
Version:        7.21
Release:        1%{?dist}
Summary:        Star Traders, a simple game of interstellar trading
License:        GPL-3.0-or-later
Url:            https://www.zap.org.au/projects/trader/
Source0:        https://ftp.zap.org.au/pub/trader/unix/trader-%{version}.tar.xz
Source1:        https://ftp.zap.org.au/pub/trader/unix/trader-%{version}.tar.xz.sig
Source2:        https://www.zap.org.au/~john/pubkey.gpg
Provides:       bundled(gnulib)
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  gperf
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(ncurses)
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
