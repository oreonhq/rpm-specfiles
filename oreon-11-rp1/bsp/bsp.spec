%global source0_hash 641c4350fd620d485e874dc9e504e6feeb6f44272be50f8622c97cbe396bc00e

Name:           bsp
Version:        5.2
Release:        41%{?dist}
Summary:        The most popular node builder for Doom

License:        GPL-2.0-or-later
URL:            http://games.moria.org.uk/doom/bsp/
Source0:        http://games.moria.org.uk/doom/bsp/download/%{name}-%{version}.tar.bz2
BuildRequires:  gcc
BuildRequires: make
Patch0:         bsp-configure-c99.patch

%description
Before you can play a level that you have created, you must use a node
builder to create the data that Doom will use to render the level.
Doom uses a rendering algorithm based on a binary space partition,
otherwise known as a BSP tree. This is stored in a data lump called
NODES in the WAD file. This data structure must be pre-calculated and
stored in the WAD file before the level can be played; the tool that
does this is called a node builder.

BSP is one of several node builders that can do this. There are
others: idbsp is the original node builder that id Software used on
the original Doom levels, for instance. BSP was the best known and
most widely used node builder throughout the height of the Doom
editing craze in the mid 1990s.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
iconv -f ISO_8859-2 -t UTF8 bsp.6 > bsp.6.tmp
mv bsp.6.tmp bsp.6
%patch -P0 -p1

%build
%configure
%make_build CFLAGS='%{optflags}' LIBS="-lm"

%install
install -D -p -m 755 bsp $RPM_BUILD_ROOT/%{_bindir}/bsp
install -D -p -m 644 bsp.6 $RPM_BUILD_ROOT/%{_mandir}/man6/bsp.6

%files
%doc AUTHORS ChangeLog INSTALL NEWS README visplane.txt test-wads/
%license COPYING
%{_bindir}/bsp
%{_mandir}/man6/bsp.6*

%changelog
%autochangelog
