Name:           gnome-common
Version:        3.18.0
Release:        23%{?dist}
Summary:        Useful things common to building GNOME packages from scratch
BuildArch:      noarch
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Projects/GnomeCommon
Source0:        https://download.gnome.org/sources/%{name}/3.18/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 22569e370ae755e04527b76328befc4c73b62bfd4a572499fde116b8318af8cf
%global source0_file gnome-common-3.18.0.tar.xz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/gnome-common-3.18.0.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "22569e370ae755e04527b76328befc4c73b62bfd4a572499fde116b8318af8cf" || { echo "oreon: Source0 SHA256 mismatch for gnome-common-3.18.0.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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
