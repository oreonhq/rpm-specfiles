%global source0_hash d8ef0c7ef779771e2c8322231bdfa7246d495ba8f24c3c210c96f3b6bd3776a7

Name:		snownews
Version: 	1.9
Release: 	12%{?dist}
Summary: 	A text mode RSS/RDF newsreader
# Automatically converted from old format: GPLv3 - review is highly recommended.
License: 	GPL-3.0-only
Url:		https://github.com/msharov/snownews
Source0:	https://github.com/msharov/snownews/archive/v%{version}/snownews-%{version}.tar.gz
Patch0:		snownews-debugflags.patch
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRequires:	gettext
BuildRequires:	openssl-devel
BuildRequires:	libcurl-devel

%description
Snownews  is  a text mode RSS/RDF newsreader. It supports all versions
of RSS natively and supports other formats via plugins.

The program depends on ncurses for the user interface and uses libxml2 
for XML parsing. ncurses must be at least version 5.0. It should work
with any version of libxml2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build
%configure

%install
make DESTDIR="$RPM_BUILD_ROOT" PREFIX="$RPM_BUILD_ROOT%{_prefix}" install
%find_lang %name

%files -f %name.lang
%doc README.md LICENSE.md
%{_bindir}/snownews
%{_mandir}/man1/*
%{_mandir}/*/man1/*

%changelog
%autochangelog
