%global source0_hash ffcb116c4bcce58c165f1b4644debf9cb973f9239a5fc1c3cf37328549f13c91
Summary:        SIP swiss army knife
Name:		sipsak
Version:	0.9.8.1
Release:        1%{?dist}
License:	GPL-2.0-or-later
URL:		https://github.com/nils-ohlmeier/sipsak
VCS:		git:%{url}.git
Source0:        https://github.com/nils-ohlmeier/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  c-ares-devel
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
%description
sipsak is a small command line tool for developers and
administrators of Session Initiation Protocol (SIP) applications.
It can be used for some simple tests on SIP applications and
devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -ivf
%configure --disable-gnutls
%make_build
%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
