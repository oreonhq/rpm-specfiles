%global source0_hash d4a690cb4ca6d52885ebfdc6230bfb550eecf4b8edb9b54453829a77f63ea7b9

Name: ttyplot
Summary: Real-time plotting utility for the terminal
License: Apache-2.0

Version: 1.7.4
Release: 2%{?dist}

URL: https://github.com/tenox7/ttyplot/
Source0: %{URL}archive/refs/tags/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconfig(ncursesw)

%description
%{name} is a realtime plotting utility for text mode consoles and terminals
with data input from stdin / pipe.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%make_build

%install
%make_install PREFIX=%{_prefix} MANPREFIX=%{_mandir}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
