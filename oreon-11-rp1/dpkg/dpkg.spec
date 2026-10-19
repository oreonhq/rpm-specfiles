%global source0_hash 4baf0632157bfac430b7dc1fe8800ea0787dac91f8bb272404ae19d98e569dd3
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(at|extra|file\\)$
%global pkgconfdir %{_sysconfdir}/dpkg
%global pkgdatadir %{_datadir}/dpkg
Name:           dpkg
Version:        1.23.11
Release:        1%{?dist}
Summary:        Package maintenance system for Debian Linux
License:        GPL-2.0-only AND GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-Public-Domain AND LicenseRef-Callaway-BSD
URL:            https://tracker.debian.org/pkg/dpkg
Source0:        http://ftp.debian.org/debian/pool/main/d/dpkg/%{name}_%{version}.tar.xz
Requires:      tar
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  dotconf-devel
BuildRequires:  doxygen
BuildRequires:  fakeroot
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  gnupg2
BuildRequires:  libmd-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Tie::Handle)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-podlators
BuildRequires:  po4a
BuildRequires:  xz-devel
BuildRequires:  zlib-ng-devel
# /oreon:deps
%description
This package provides the low-level infrastructure for handling the
installation and removal of Debian software packages.

This package contains the tools (including dpkg-source) required to unpack,
build and upload Debian source packages.

This package also contains the programs dpkg which used to handle the
installation and removal of packages on a Debian system.

This package also contains dselect, an interface for managing the installation
and removal of packages on the system.

dpkg and dselect will certainly be non-functional on a rpm-based system because
packages dependencies will likely be unmet.

%package devel
Summary:    Debian package management static library
Provides:   dpkg-static = %{version}-%{release}
%description devel
This package provides the header files and static library necessary to develop
software using dpkg, the same library used internally by dpkg.

Note though, that the API is to be considered volatile, and might change at any
time, use at your own risk.

%package dev
Summary:    Debian package development tools
BuildArch:  noarch
Requires:   binutils
Requires:   bzip2
Requires:   dpkg-perl = %{version}-%{release}
Requires:   gcc
Requires:   lzma
Requires:   make
Requires:   patch
Requires:   xz
Requires:   zstd
%description dev
This package provides the development tools (including dpkg-source) required to
unpack, build and upload Debian source packages.

Most Debian source packages will require additional tools to build; for example,
most packages need make and the C compiler gcc.

%package perl
Summary:    Dpkg perl modules
BuildArch:  noarch
Requires:   dpkg = %{version}-%{release}
Requires:   perl-TimeDate
Requires:   perl(Digest::MD5)
Requires:   perl(Digest::SHA)
Requires:   perl(Digest::SHA1)
%description perl
This package provides the perl modules used by the scripts in dpkg-dev. They
cover a wide range of functionality. Among them there are the following public
modules:

 - Dpkg: core variables
 - Dpkg::Arch: architecture handling functions
 - Dpkg::BuildFlags: set, modify and query compilation build flags
 - Dpkg::BuildInfo: build information functions
 - Dpkg::BuildOptions: parse and manipulate DEB_BUILD_OPTIONS
 - Dpkg::BuildProfiles: parse and manipulate build profiles
 - Dpkg::Changelog: parse changelogs
 - Dpkg::Changelog::Entry: represents a changelog entry
 - Dpkg::Changelog::Parse: generic changelog parser for dpkg-parsechangelog
 - Dpkg::Checksums: generate and parse checksums
 - Dpkg::Compression: simple database of available compression methods
 - Dpkg::Compression::FileHandle: transparently (de)compress files
 - Dpkg::Compression::Process: wrapper around compression tools
 - Dpkg::Conf: parse dpkg configuration files
 - Dpkg::Control: parse and manipulate Debian control information
   (.dsc, .changes, Packages/Sources entries, etc.)
 - Dpkg::Control::Changelog: represent fields output by dpkg-parsechangelog
 - Dpkg::Control::Fields: manage (list of known) control fields
 - Dpkg::Control::Hash: parse and manipulate a block of RFC822-like fields
 - Dpkg::Control::Info: parse files like debian/control
 - Dpkg::Control::Tests: parse files like debian/tests/control
 - Dpkg::Control::Tests::Entry: represents a debian/tests/control stanza
 - Dpkg::Deps: parse and manipulate dependencies
 - Dpkg::Deps::Simple: represents a single dependency statement
 - Dpkg::Deps::Multiple: base module to represent multiple dependencies
 - Dpkg::Deps::Union: list of unrelated dependencies
 - Dpkg::Deps::AND: list of AND dependencies
 - Dpkg::Deps::OR: list of OR dependencies
 - Dpkg::Deps::KnownFacts: list of installed and virtual packages
 - Dpkg::Exit: push, pop and run exit handlers
 - Dpkg::Gettext: wrapper around Locale::gettext
 - Dpkg::IPC: spawn sub-processes and feed/retrieve data
 - Dpkg::Index: collections of Dpkg::Control (Packages/Sources files for
   example)
 - Dpkg::Interface::Storable: base object serializer
 - Dpkg::Path: common path handling functions
 - Dpkg::Source::Format: manipulate debian/source/format files
 - Dpkg::Source::Package: extract Debian source packages
 - Dpkg::Substvars: substitute variables in strings
 - Dpkg::Vendor: identify current distribution vendor
 - Dpkg::Version: parse and manipulate Debian package versions

All the packages listed in Suggests or Recommends are used by some of the
modules.

%package -n dselect
Summary:  Debian package management front-end
Requires: %{name} = %{version}-%{release}
%description -n dselect
dselect is a high-level interface for managing the installation and removal of
Debian software packages. Many users find dselect intimidating and new users may
prefer to use apt-based user interfaces.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vif
%configure \
    --disable-linker-optimizations \
    --disable-rpath \
    --disable-update-alternatives \
    --runstatedir=/run \
    --with-admindir=%{_localstatedir}/lib/dpkg \
    --with-libbz2 \
    --with-liblzma \
    --with-libselinux \
    --with-libz-ng \
    --with-libzstd
%make_build
%install
%make_install
mkdir -p %{buildroot}/%{pkgconfdir}/origins
cat <<EOF > %{buildroot}/%{pkgconfdir}/origins/fedora
Vendor: Fedora
Vendor-URL: http://www.fedoraproject.org/
Bugs: https://bugzilla.redhat.com
EOF
install -pm0644 debian/dpkg.cfg %{buildroot}/%{pkgconfdir}
install -pm0644 debian/dselect.cfg %{buildroot}/%{pkgconfdir}
install -pm0644 debian/shlibs.default %{buildroot}/%{pkgconfdir}
install -pm0644 debian/shlibs.override %{buildroot}/%{pkgconfdir}
install -D -pm0644 debian/dpkg.logrotate %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}
for file in diversions statoverride status; do
    touch %{buildroot}%{_localstatedir}/lib/dpkg/$file
done
mkdir -p %{buildroot}%{_localstatedir}/log/
touch %{buildroot}%{_localstatedir}/log/dpkg.log
%find_lang dpkg
%find_lang dpkg-dev
%find_lang dselect
rm %{buildroot}%{_libdir}/libdpkg.la
%oreon_autofiles dselect usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make TEST_PARALLEL=4 check
%files -f %{oreon_filedir}/main.list
%files -n dpkg-devel -f %{oreon_filedir}/dpkg-devel.list
%files -n dpkg-dev -f %{oreon_filedir}/dpkg-dev.list
%files -n dpkg-perl -f %{oreon_filedir}/dpkg-perl.list
%files -n dselect -f %{oreon_filedir}/dselect.list

%changelog

%autochangelog
