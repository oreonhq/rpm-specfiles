%global source0_hash 123d71f40051e6afc59dc8f8fb6efef0524a99b377856d99d5e64d0b867ab2be
Name:           purple-mm-sms
Version:        0.1.7
Release:        1%{?dist}
Summary:        A libpurple plugin for sending and receiving SMS via ModemManager
License:        GPL-3.0-or-later
URL:            https://source.puri.sm/Librem5/purple-mm-sms
Source0:        https://source.puri.sm/Librem5/purple-mm-sms/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:        COPYING
Patch0: install-library-with-correct-permissions.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(purple)
# /oreon:deps
%description
A libpurple plugin for sending and receiving SMS via ModemManager

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version}

# Temporary until the next release which contains this license
cp %{SOURCE1} .

%build

%set_build_flags
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
