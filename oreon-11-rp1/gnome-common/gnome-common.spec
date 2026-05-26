# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 22569e370ae755e04527b76328befc4c73b62bfd4a572499fde116b8318af8cf
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           gnome-common
Version:        3.18.0
Release:        23%{?dist}
Summary:        Useful things common to building GNOME packages from scratch
BuildArch:      noarch
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Projects/GnomeCommon
Source0:        https://download.gnome.org/sources/%{name}/3.18/%{name}-%{version}.tar.xz

BuildRequires: make

# This will pull in the latest version; if your package requires something older,
# well, BuildRequire it in that spec.  At least until such time as we have a
# build system that is intelligent enough to inspect your source code
# and auto-inject those requirements.
Requires:       automake
Requires:       autoconf
Requires:       autoconf-archive
Requires:       gettext
Requires:       libtool
Requires:       pkgconfig
Requires:       yelp-tools

%description
This package contains sample files that should be used to develop pretty much
every GNOME application.  The programs included here are not needed for running
GNOME apps or building ones from distributed tarballs.  They are only useful
for compiling from git sources or when developing the build infrastructure for
a GNOME application.

%prep
%oreon_verify_sources
%setup -q

%build
%configure --with-autoconf-archive
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} INSTALL="install -p" install

%files
%doc ChangeLog README
%license COPYING
%{_bindir}/gnome-autogen.sh
%{_datadir}/aclocal/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.18.0-23
- Prepare for Oreon 11 (RP1)
