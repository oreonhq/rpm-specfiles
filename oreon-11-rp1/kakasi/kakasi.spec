%global source0_hash 2ee57b1b03c74fd5766e741c3812028efc73bc0e0bf93a6e7ff20eb4701f3ee3

Name:		kakasi
Version:	2.3.6
Release:	35%{?dist}
URL:		http://kakasi.namazu.org/
License:	GPL-2.0-or-later
BuildRequires:	autoconf automake libtool gettext-devel
BuildRequires: make

Source:	http://kakasi.namazu.org/stable/%{name}-%{version}.tar.xz
Patch4:		kakasi-multilib.patch
Patch5: kakasi-configure-c99.patch
Patch6:	%{name}-ftbfs.patch

Summary:	A Japanese character set conversion filter

%description
KAKASI is a filter for converting Kanji characters to Hiragana or
Katakana characters, or into Romaji (phonetic transcription of
Japanese pronunciation).

%package libs
Summary:	Libraries for KAKASI

%description libs
The kakasi-libs package contains the library file for KAKASI

%package devel
Summary:	Files for development of applications which will use KAKASI
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Conflicts:	%{name} < 2.3.6

%description devel
The kakasi-devel package contains the header file and library for
developing applications which will use the KAKASI Japanese character
set filter.

%package dict
Summary:	The base dictionary for KAKASI
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description dict
The kakasi-dict package contains the base dictionary for the KAKASI
Japanese character set filter.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf -f -i -I%{_datadir}/gettext/m4

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# correct timestamp
touch -r kakasi-config.in $RPM_BUILD_ROOT%{_bindir}/kakasi-config

# remove the unnecesary files
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la

mkdir -p $RPM_BUILD_ROOT%{_mandir}/ja/man1
iconv -f euc-jp -t utf-8 man/kakasi.1.ja > man/kakasi.1.ja.utf8 && touch -r man/kakasi.1.ja man/kakasi.1.ja.utf8 && install -m 0644 man/kakasi.1.ja.utf8 $RPM_BUILD_ROOT/%{_mandir}/ja/man1/kakasi.1

%ldconfig_scriptlets	libs

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%lang(ja) %doc README-ja
%dir %{_datadir}/kakasi
%{_bindir}/*
%exclude %{_bindir}/kakasi-config
%{_mandir}/man1/kakasi.1*
%{_mandir}/ja/man1/kakasi.1*
%{_datadir}/kakasi/itaijidict

%files libs
%license COPYING
%{_libdir}/libkakasi.so.*

%files devel
%license COPYING
%{_bindir}/kakasi-config
%{_libdir}/libkakasi.so
%{_mandir}/man1/kakasi-config.1*
%{_includedir}/libkakasi.h

%files dict
%license COPYING
%{_datadir}/kakasi/kanwadict

%changelog
%autochangelog
