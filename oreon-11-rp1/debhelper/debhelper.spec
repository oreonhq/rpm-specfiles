%global source0_hash 69bfb9686cbd449dfdd68de2fa27ec7adab4d61cef17f47653e9fb609722812e
%global __provides_exclude_from ^%{_docdir}/.*$
%global __requires_exclude_from ^%{_docdir}/.*$
%bcond_without tests
Name:           debhelper
Version:        13.30
Release:        1%{?dist}
Summary:        Helper programs for debian/rules
License:        GPL-2.0-or-later
URL:            https://tracker.debian.org/pkg/debhelper
BuildArch:      noarch
ExcludeArch:    ppc64le
Source0:        https://snapshot.debian.org/archive/debian/20260215T142834Z/pool/main/d/%{name}/%{name}_%{version}.tar.xz
Patch0:         no_layout_deb.patch
%if %{with tests}
%endif
Requires:       binutils
Requires:       dh-autoreconf >= 17
Requires:       dpkg >= 1.18.0
Requires:       dpkg-dev >= 1.18.2
Requires:       dpkg-perl >= 1.17.14
Requires:       gzip
Requires:       perl(Carp)
Requires:       perl(Digest::SHA)
Requires:       perl(Dpkg::Arch)
Requires:       perl(Dpkg::BuildProfiles)
Requires:       perl(Dpkg::Changelog::Parse)
Requires:       perl(Dpkg::Deps)
Requires:       perl(File::Copy)
Requires:       perl(File::Path)
Requires:       po-debconf
Suggests:       dh-make
Suggests:       perl(Dpkg::BuildFlags)
Suggests:       perl(Dpkg::Changelog::Debian)
# oreon:deps
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  dpkg-dev
BuildRequires:  fakeroot
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  grep
BuildRequires:  gzip
BuildRequires:  make
BuildRequires:  man-db
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Dpkg::Arch)
BuildRequires:  perl(Dpkg::BuildFlags)
BuildRequires:  perl(Dpkg::Changelog::Debian)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(autodie)
BuildRequires:  perl(constant)
BuildRequires:  perl(feature)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-podlators
BuildRequires:  po4a
BuildRequires:  sed
# /oreon:deps
%description
A collection of programs that can be used in a debian/rules file to automate
common tasks related to building Debian packages. Programs are included to
install various files into your package, compress files, fix file permissions,
integrate your package with the Debian menu system, debconf, doc-base, etc.
Most Debian packages use debhelper as part of their build process.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir work
%oreon_prep
%build

%make_build build
%install
%make_install
./run dh_installman -P %{buildroot} --verbose -p debhelper
%oreon_autofiles main
%if %{with tests}
%check

make test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
