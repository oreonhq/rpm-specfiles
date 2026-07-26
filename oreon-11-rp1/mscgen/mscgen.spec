%global source0_hash 3c3481ae0599e1c2d30b7ed54ab45249127533ab2f20e768a0ae58d8551ddc23

Name:           mscgen
Version:        0.20
Release:        43%{?dist}
Summary:        Message Sequence Chart rendering program
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.mcternan.me.uk/mscgen/
Source0:        http://www.mcternan.me.uk/mscgen/software/%{name}-src-%{version}.tar.gz

# Removes unknown escape sequence '\-'
# Patch sent upstream.
# http://code.google.com/p/mscgen/issues/detail?id=72
Patch0:         %{name}-0.20-escape.patch

# Fixes 'ymax' variable initialization
# http://code.google.com/p/mscgen/issues/detail?id=73
Patch1:         %{name}-0.20-uninitialized-ymax.patch

# Fixes language.c:464:5: error: conflicting types for 'yyparse'
# https://code.google.com/p/mscgen/issues/detail?id=83
Patch2:         %{name}-0.20-language.patch
# Fixes crash in tests
Patch3:         https://salsa.debian.org/debian/mscgen/-/raw/638a985eed63f6849c77c03216780a671757165d/debian/patches/width-never-less-than-zero.patch#/%{name}-0.20-width-never-less-than-zero.patch

%global test_with_valgrind %{?_with_valgrind:1}%{!?_with_valgrind:0}

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  pkgconfig
BuildRequires:  gd-devel
BuildRequires:  freetype-devel
BuildRequires:  urw-base35-fonts

%if %{test_with_valgrind}
BuildRequires:  valgrind
%endif

# Freetype based font rendering requires some fonts to be installed.
Requires:       urw-base35-fonts

%description
Mscgen is a small program that parses Message Sequence Chart descriptions
and produces PNG, SVG, EPS or server side image maps (ismaps) as the output.
Message Sequence Charts (MSCs) are a way of representing entities and
interactions over some time period and are often used in combination with SDL.
MSCs are popular in Telecoms to specify how protocols operate although MSCs
need not be complicated to create or use. Mscgen aims to provide a simple text
language that is clear to create, edit and understand, which can also be
transformed into common image formats for display or printing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .escape
%patch -P1 -p1 -b .initialization
%patch -P2 -p1 -b .language
%patch -P3 -p1 -b .zero
#this ensures that they get regenerated
rm -f src/language.{c,h} src/lexer.c

%build
# Correct EOL.
sed 's/\r//' TODO >TODO.tmp && touch -r TODO TODO.tmp && mv TODO.tmp TODO
%configure \
    --with-freetype \
    --docdir=%{_defaultdocdir}/%{name}
make %{?_smp_mflags}

%check
%if %{test_with_valgrind}
export VALGRIND="valgrind -v --track-origins=yes --tool=memcheck"
%endif
make check

%install
make install INSTALL="install -p" DESTDIR=%{buildroot}
cp -p TODO %{buildroot}%{_defaultdocdir}/%{name}/

%files
# due to this entry, doc must not be used to add any other files
%{_defaultdocdir}/%{name}/
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*

%changelog
%autochangelog
