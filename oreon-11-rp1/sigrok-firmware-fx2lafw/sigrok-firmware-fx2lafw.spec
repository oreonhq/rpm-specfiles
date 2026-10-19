%global source0_hash 1a9a196a17997bbd33d7463d862bf55cbb945e72b926d9bee784ba1e606f2236
%global         gitrev 9fe40f8
%global         autohell autoconf automake
Name:           sigrok-firmware-fx2lafw
Version:        0.1.7.git%{gitrev}
Release:        1%{?dist}
Summary:        Firmware for logic analyzers based on the Cypress EZ-USB FX2(LP) chip
License:        GPL-2.0-or-later
URL:            http://www.sigrok.org
Source0:        %{name}-%{gitrev}.zip
BuildArch:      noarch
Requires:       sigrok-firmware-filesystem
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  sdcc
# /oreon:deps
%description
fx2lafw is a free/libre/open-source firmware for logic analyzers based on
the Cypress EZ-USB FX2(LP) chip.

This firmware package is needed to use libsigrok with Cypress EZ-USB FX2(LP)
based logic analyzers (the fx2lafw driver in libsigrok).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{gitrev}

%build

autoreconf --force --install
%configure
make %{?_smp_mflags}
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
