%global source0_hash e5293d4fe2502662f19c793bef416e05ac020490218e71c75a5e92919c466071
Name:           hstr
Version:        3.2
Release:        1%{?dist}
Summary:        Suggest box like shell history completion
License:        Apache-2.0
URL:            https://github.com/dvorka/hstr
Source0:        https://github.com/dvorka/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  automake
BuildRequires:  bash-completion
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
# /oreon:deps
%description
A command line utility that brings improved shell command completion
from the history. It aims to make completion easier and faster than Ctrl-r.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
autoreconf -fiv

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
