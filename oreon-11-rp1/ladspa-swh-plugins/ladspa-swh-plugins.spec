%global source0_hash d1b090feec4c5e8f9605334b47faaad72db7cc18fe91d792b9161a9e3b821ce7

%global pkgname swh-plugins

Summary:        A set of audio plugins for LADSPA
Name:           ladspa-%{pkgname}
Version:        0.4.17
Release:        20%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://plugin.org.uk/
Source0:        https://github.com/swh/ladspa/archive/v%{version}/%{name}-%{version}.tar.gz
# Unbundle libgsm
Patch0:         %{name}-libgsm.patch
# Do not add -march directives to CFLAGS
Patch1:         %{name}-0.4.17-riceitdown.patch
# Fix an undefined symbol due to a misplaced inline
Patch2:         %{name}-noinline.patch
# Add Language headers to the po files
Patch3:         %{name}-language.patch

BuildRequires:  gcc
BuildRequires:  fftw3-devel
BuildRequires:  gettext-devel
BuildRequires:  gsm-devel
BuildRequires:  ladspa-devel
# Github does not ship configure and Makefile.in
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig
BuildRequires: make

Requires:       ladspa

%description
A set of audio plugins for LADSPA (see http://plugin.org.uk/ for more
details).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n ladspa-%{version}
# Unbundle libgsm
rm -rf %{_builddir}/gsm

%build
autoreconf -f -i -I m4
%configure \
  %ifarch %{ix86} x86_64
    --enable-sse \
  %endif
    --disable-static

%make_build

%install
%make_install
%find_lang %{pkgname}

%files -f %{pkgname}.lang
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/ladspa/*.so
%{_datadir}/ladspa/rdf/*

%changelog
%autochangelog
