%global source0_hash 937610b97c329a1ec9268553fb780037bcfff0dcffe9725ebc4fd9c1aa9075db
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: cpio
Version: 2.15
Release: 1%{?dist}
Summary: GNU cpio
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/cpio/
Source0: https://ftp.gnu.org/gnu/cpio/cpio-%{version}.tar.bz2
Source1: cpio-%{version}.tar.bz2.sig
Source2: gray-key.gpg
Patch0: cpio-2.14-rh.patch
Patch1: cpio-2.14-exitCode.patch
Patch2: cpio-2.14-dev_number.patch
Patch3: cpio-2.9.90-defaultremoteshell.patch
Patch4: cpio-2.14-patternnamesigsegv.patch
Patch5: cpio-2.10-longnames-split.patch
Patch6: cpio-2.11-crc-fips-nit.patch

Provides: bundled(gnulib)
Provides: bundled(paxutils)

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: texinfo
%endif

%description
GNU cpio copies files into and out of cpio and tar archives.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1

%build
%oreon_configure --with-rmt=%{_sysconfdir}/rmt
%oreon_make

%install
%oreon_make_install
%oreon_filelist

%check
%oreon_make check

%files -f %{_builddir}/%{name}.files
%license COPYING
