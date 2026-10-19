%global source0_hash 7072b45e74b9d5e2d1316f49e13d200e05ccde52631a4d4b5469bbaba5e159b2
Name:          lnav
Version:       0.14.1
Release:        1%{?dist}
Summary:        Curses-based tool for viewing and analyzing log files
License:       LicenseRef-Callaway-BSD
URL:           http://lnav.org
Source0:        https://github.com/tstack/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  gcc-c++
BuildRequires:  libarchive-devel
BuildRequires:  libcurl-devel
BuildRequires:  libunistring-devel
BuildRequires:  make
BuildRequires:  notcurses-devel
BuildRequires:  openssh
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  re2c
BuildRequires:  sqlite-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
%{name} is an enhanced log file viewer that takes advantage of any semantic
information that can be gleaned from the files being viewed, such as
timestamps and log levels. Using this extra semantic information, it can
do things like interleaving messages from different files, generate
histograms of messages over time, and providing hotkeys for navigating
through the file. It is hoped that these features will allow the user to
quickly and efficiently zero in on problems.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --disable-static --disable-silent-rules
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
