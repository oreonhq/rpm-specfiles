%global source0_hash 2b3b79c2e04f27f689f7b145838b4aa1a4bef43fd968358e28e2bf95fd9b6376

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		arpage
Version:	0.3.3
Release:	43%{?dist}
Summary:	A JACK MIDI arpeggiator

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		http://arpage.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-gcc46.patch
Patch1:		%{name}-gcc47.patch

BuildRequires:  gcc-c++
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	gtkmm24-devel
BuildRequires:	intltool libxml++-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libtool
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires: make

%description

A GTK application that runs up to 4 arpeggiators on incoming MIDI
data, synchronized to JACK.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

#fix compilation with gcc 4.6
%patch -P0 -p1 -b .%{name}-gcc46.patch
#fix compilation with gcc 4.7
%patch -P1 -p1 -b .%{name}.gcc47.patch

# fix bad permissions in debuginfo
chmod 644 %{_builddir}/%{name}-%{version}/src/main.cc

%build

# Fix for aarch64 build
#automake --add-missing
autoreconf -i

%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} arpagedocdir=%{_pkgdocdir}

desktop-file-install --dir=%{buildroot}/%{_datadir}/applications %{SOURCE1}

mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps
install -m 644 %{_builddir}/%{name}-%{version}/src/arpage.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/

%files
%doc COPYING ChangeLog AUTHORS README INSTALL NEWS
%{_bindir}/%{name}
%{_bindir}/zonage
%{_datadir}/%{name}/ui/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%changelog
%autochangelog
