%global source0_hash 35c5bf1899adbb5b52c2f66b741165f1369aba1c84045abc159929df12e61e1c
Name:		ibus-fep
Version:	1.4.4
Release:        1%{?dist}
Summary:        IBus client for text terminals (non frame buffer)
License:	GPL-3.0-or-later
URL:		https://github.com/ueno/ibus-fep
Source0:        https://github.com/downloads/ueno/ibus-fep/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  ibus-devel
BuildRequires:  intltool
BuildRequires:  libfep-devel
BuildRequires:  make
BuildRequires:  vala
# /oreon:deps
%description
ibus-fep is an IBus client that runs on text terminals such as xterm.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
touch src/*.vala

%build

%configure
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
