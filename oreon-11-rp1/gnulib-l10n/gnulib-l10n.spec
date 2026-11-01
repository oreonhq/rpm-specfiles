%global source0_hash 155752ba6796aa294cde87c2bf0e771a5891eeeacb131345be0e080a3ec0ceea
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: gnulib-l10n
Version: 20241231
Release: 1%{?dist}
Summary: Translations for Gnulib messages
License: LGPL-2.1-or-later
URL: https://www.gnu.org/software/gnulib/
Source0: https://ftp.gnu.org/gnu/gnulib/gnulib-l10n-%{version}.tar.gz
Source1: gnulib-l10n-%{version}.tar.gz.sig
Source2: gnulib-l10n-key.asc
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: gnupg2
BuildRequires: make
BuildRequires: gettext

%description
Message catalogs for the Gnulib modules used by GNU packages.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n gnulib-l10n-%{version} -p1

%build
./configure --prefix=%{_prefix} --datadir=%{_datadir}
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
