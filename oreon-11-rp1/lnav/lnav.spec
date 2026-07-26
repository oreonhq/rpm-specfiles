%global source0_hash 4541581d34981aff3be8aee1ddf2b79172bfc18f16223007a880b8053abb0cc4

Name:          lnav
Version:       0.13.2
Release:       2%{?dist}
Summary:       Curses-based tool for viewing and analyzing log files
# Automatically converted from old format: BSD - review is highly recommended.
License:       LicenseRef-Callaway-BSD

URL:           http://lnav.org
Source0:       https://github.com/tstack/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2

BuildRequires: bzip2-devel
BuildRequires: gcc-c++
BuildRequires: libarchive-devel
BuildRequires: libcurl-devel
BuildRequires: libunistring-devel
BuildRequires: make
BuildRequires: notcurses-devel
BuildRequires: openssh
BuildRequires: openssl-devel
BuildRequires: pcre2-devel
BuildRequires: re2c
BuildRequires: sqlite-devel
BuildRequires: zlib-devel

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

%files
%doc AUTHORS NEWS.md README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
