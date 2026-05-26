# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 f095f9cbb539cd48b75cec6fe2f844ba0cb8866ce5e4318ad4ca5ba0224396d4
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global version_no_dot 27

Name:           c2esp
Version:        2.7
Release:        37%{?dist}
Summary:        CUPS driver for Kodak AiO printers

License:        GPL-2.0-or-later
URL:            http://sourceforge.net/projects/cupsdriverkodak/
Source0:        http://downloads.sourceforge.net/cupsdriverkodak/c2esp-%{version_no_dot}.tar.gz

Patch01: c2esp-ftbfs-gcc7.patch
Patch02: c2esp-gcc10.patch
Patch03: c2esp-c99.patch
Patch04: c2esp-use-libcupsfilters.patch


# for autoreconf
BuildRequires: autoconf
BuildRequires: automake
# _cups_serverbin macro
BuildRequires: cups-devel
# Needs gcc for compilation
BuildRequires: gcc
# for autosetup
BuildRequires: git-core
# JBIG1 lossless image compression
BuildRequires: jbigkit-devel
# cupsfilters/image.h
BuildRequires: libcupsfilters-devel
# for ppdCMYKLoad()
BuildRequires: libppd-devel
# uses make
BuildRequires: make
# postscriptdriver tags
BuildRequires: python3-cups

# directory structure
Requires: cups-filesystem

%description
CUPS filters and drivers for Kodak ESP and Hero all in one printers.

%prep
%oreon_verify_sources
%autosetup -n c2esp-%{version_no_dot} -S git


%build
# c2esp-use-libcupsfilters.patch changes configure.ac, regenerate configure script
autoreconf -vfi

%configure
make %{_smp_mflags} -C src/

%install
# do not install doc/ or scripts/
make -C src/ install DESTDIR=%{buildroot}

%files
%license doc/COPYING
%doc doc/README
%{_cups_serverbin}/filter/c2esp
%{_cups_serverbin}/filter/c2espC
%{_cups_serverbin}/filter/command2esp
%{_datadir}/cups/drv/c2esp

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.7-37
- Prepare for Oreon 11 (RP1)
