%global source0_hash cba1ca1689d4031faf37bb7a184559106b6d2f462ae8890a9fa16e3022ca1eb0

# -*-Mode: rpm-spec -*-

Name:     aml
Version:  0.3.0
Release:  1%{?dist}
Summary:  Another Main Loop
License:  ISC AND LicenseRef-Callaway-BSD
URL:      https://github.com/any1/aml
Source0:  https://github.com/any1/aml/archive/v%{version}/aml-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: meson

%description

Event loop handler developed for wayvnc (Wayland VNC server) and
wlvncc (Wayland VNC client) - see https://github.com/any1

Goals:
 * Portability
 * Utility
 * Simplicity

Non-goals:
 * MS Windows (TM) support
 * Solving the C10K problem

Features:
 * File descriptor event handlers
 * Timers
 * Tickers
 * Signal handlers
 * Idle dispatch callbacks
 * Thread pool
 * Interoperability with other event loops

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains header files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%{_libdir}/lib%{name}.so.0*

%doc README.md

%license COPYING

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*

%changelog
%autochangelog
