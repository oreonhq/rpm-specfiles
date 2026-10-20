%global source0_hash 4d62ff37342ec7aed748535323930c7cf94acf71c3591882b26a7ea50f3edc16
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: tar
Version: 1.35
Release: 1%{?dist}
Summary: GNU tar
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/tar/
Source0: https://ftp.gnu.org/gnu/tar/tar-1.35.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
GNU 'tar' saves many files together into a single tape or disk archive, and can restore individual files from the archive. It includes multivolume support, the ability to archive sparse files, automatic archive compression/decompression, remote archives and special features that allow 'tar' to be used for incremental and full backups. This distribution also includes 'rmt', the remote tape server.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure
%oreon_make

%install
%oreon_make_install
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
