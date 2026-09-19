%global source0_hash cd6886f9aefe6a3f6c566fa61271a55710901a71849c630bf5376aa984bf77cc

Summary: test VT100-type terminal

%define AppPatched 20251205

Name: vttest
Version: 2.7.%{AppPatched}
Release: 9%{?dist}
License: MIT
URL: https://invisible-island.net/%{name}/
Source0: https://invisible-island.net/archives/%{name}/%{name}-%{AppPatched}.tgz
BuildRequires: gcc
BuildRequires: make

%description
Vttest is a program designed to test the functionality of a VT100
terminal (or emulator thereof).  It tests both display (escape sequence
handling) and keyboard.

The program is menu-driven and contains full on-line operating
instructions.  To run a given menu-item, you must enter its number.  You
can run all menu-items (for a given level) by entering an asterisk, i.e,
`*'.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{AppPatched}

%build

%configure

%make_build

%install
%make_install

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%doc CHANGES MANIFEST README
%license COPYING

%changelog
%autochangelog
