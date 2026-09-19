%global source0_hash b378bd469ee1e50f5246236d2b1432f393d244e1e4b0662cc5147b427354a47c

%define         gituser         jessek
%define         gitname         hashdeep
%global         commit          cd2ed7416685a5e83eb10bb659d6e9bec01244ae
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           md5deep
Version:        4.4
Release:        27%{?dist}
Summary:        A set of cross-platform tools to compute hashes
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://md5deep.sf.net/
#Source0:       http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Patch0:		md5deep-gcc11.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake

%description
This is md5deep, a set of cross-platform tools to compute hashes, or
message digests, for any number of files while optionally recursively
digging through the directory structure.  It can also take a list of known
hashes and display the filenames of input files whose hashes either do or
do not match any of the known hashes. This version supports MD5, SHA-1,
SHA-256, Tiger, and Whirlpool hashes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gitname}-%{commit}
%patch -P0 -p1
autoreconf -vif

%build
export CFLAGS="-fPIE -pie ${RPM_OPT_FLAGS}"
export CXXFLAGS="-fPIE -pie ${RPM_OPT_FLAGS}"
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc README NEWS COPYING ChangeLog AUTHORS TODO
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
