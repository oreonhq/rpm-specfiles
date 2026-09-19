%global source0_hash 123d71f40051e6afc59dc8f8fb6efef0524a99b377856d99d5e64d0b867ab2be

Name:           purple-mm-sms
Version:        0.1.7
Release:        %autorelease
Summary:        A libpurple plugin for sending and receiving SMS via ModemManager

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://source.puri.sm/Librem5/purple-mm-sms
Source0:        https://source.puri.sm/Librem5/purple-mm-sms/-/archive/v%{version}/%{name}-v%{version}.tar.gz

# Until the next release which contains this in the source
Source1:        COPYING

BuildRequires:  gcc
BuildRequires:  pkgconfig(purple)
BuildRequires:  pkgconfig(mm-glib)

# By default, the library file is installed with 0644, which breaks debuginfo.
# https://source.puri.sm/Librem5/purple-mm-sms/-/merge_requests/24
Patch0: install-library-with-correct-permissions.patch

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

%files
%{_libdir}/purple-2/mm-sms.so
%{_datadir}/pixmaps/*
%doc README.md
%license COPYING

%changelog
%autochangelog
