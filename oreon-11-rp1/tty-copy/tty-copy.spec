%global source0_hash 5dad7c9eeb1f13747f989e38c4165edd367e7c6c348545b28ac8c1fb50cf4716
Name:           tty-copy
Version:        0.2.2
Release:        1%{?dist}
Summary:        Copy content to system clipboard via TTY and terminal using ANSI OSC52 sequence
License:        MIT
URL:            https://github.com/jirutka/tty-copy
Source0:        https://github.com/jirutka/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  asciidoctor
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
tty-copy is a utility for copying content to the system clipboard from
anywhere via a TTY and terminal using the ANSI OSC52 sequence. It works in any
terminal session, whether local, remote (e.g. SSH), or even nested therein.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
%make_build
%install
%make_install PREFIX=%{_prefix}
%oreon_autofiles main

%check

%{buildroot}%{_bindir}/tty-copy -V
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
