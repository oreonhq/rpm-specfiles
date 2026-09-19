%global source0_hash 17d6ddeb817b0f8fdde63b0f8a026b6a4ef4d7a7872591ed7c5b33f7fe83734b

%define _legacy_common_support 1

%global commit d583dfc9603e004b1c6a870f5475a21475b581f7
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           wmacpi
Version:        2.3
Release:        14.20200618git%{shortcommit}%{?dist}
Summary:        Dockapp for laptop acpi/apm information

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.dockapps.net/wmacpi
Source0:	https://repo.or.cz/dockapps.git/snapshot/%{commit}.tar.gz
#Source0:        https://www.dockapps.net/download/wmacpi-2.3.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  libdockapp-devel

%description
Dockapp which displays acpi/apm information.
his is a typical laptop ACPI dockapp. One interesting feature is the "timer" 
mode, where you can keep track of how long the laptop has been "on battery". 
This is opposite of the information usually provided by the BIOS, which is 
"time remaining", and in many cases wrong. This option can be toggled at 
run-time. System messages scroll on the bottom of the window, AC plug flashes 
when battery is charging, and green LED inside the big button flashes red if 
battery level is critical low.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n dockapps-%{shortcommit}/wmacpi

%build
# -lXpm -lXext are not directly needed, only through libdockapp
CFLAGS="%{build_cflags} -ansi" LDFLAGS="%{build_ldflags} -lX11 -ldockapp" \
      %make_build

%install
%make_install PREFIX="%{_prefix}"

%files
%doc AUTHORS COPYING README ChangeLog
%{_bindir}/wmacpi
%{_mandir}/man1/wmacpi.1*
%{_bindir}/wmacpi-cli
%{_mandir}/man1/wmacpi-cli.1*

%changelog
%autochangelog
