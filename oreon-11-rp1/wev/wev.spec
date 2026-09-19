%global source0_hash 89b8d9bc756631795ee91c99a0d5b0877c9f5c3acfe81f77a2b69ecfc15daf16

# -*-Mode: rpm-spec -*-

Name:     wev
Version:  1.1.0
Release:  1%{?dist}
Summary:  A tool for debugging events on a sway Wayland window
License:  MIT
URL:      https://git.sr.ht/~sircmpwn/wev
Source0:  %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)

%description
A tool for debugging events on a sway Wayland window,
analogous to the X11 tool xev.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%license LICENSE
%doc README.md

%changelog
%autochangelog
