%global source0_hash 473c2f312391379960efe41caad37852c59312bc8f100f9b5f26609ab5704288
%global commit 1f13bf5c5e86cbc99a6f0492fcdcd38cf0da2105
%global gittag v1.8.6
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:		rdesktop
Version:	1.9.0
Release:        19%{?dist}
Summary:        X client for remote desktop into Windows Terminal Server
License:	GPL-3.0-or-later
URL:		http://www.rdesktop.org/
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/rdesktop-%{version}.tar.gz
Patch0:         https://patch-diff.githubusercontent.com/raw/rdesktop/rdesktop/pull/394.patch
Patch1:         rdesktop-crypto.patch
Patch2: rdesktop-configure-c99.patch
Patch3:         https://github.com/rdesktop/rdesktop/commit/53ba87dc174175e98332e22355ad8662c02880d6.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gnutls-devel
BuildRequires:  krb5-devel
BuildRequires:  libX11-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libtasn1-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  nettle-devel
BuildRequires:  pcsc-lite-devel
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
%description
rdesktop is an open source client for Windows NT Terminal Server and
Windows 2000 & 2003 Terminal Services, capable of natively speaking 
Remote Desktop Protocol (RDP) in order to present the user's NT
desktop. Unlike Citrix ICA, no server extensions are required.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vif
%configure --with-ipv6 --with-sound=pulse
%make_build
%install
%make_install STRIP=/bin/true
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
