Summary: A text-based modem control and terminal emulation program
Name: minicom
Version: 2.10
Release: 2%{?dist}
URL: https://salsa.debian.org/minicom-team/minicom
# The file 'src/wildmat.c' is LicenseRef-Fedora-Public-Domain.
# Some LGPL-2.0-or-later files (e.g., 'lib/getopt.c', 'lib/error.c')
# *may* be used in building of certain files (minicom, ascii-xfr, runscript).
# They are probably not actually used, but I wasn't able to exclude them from
# the build process completely yet.
# The rest is simply GPL-2.0-or-later.
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
#ExcludeArch: s390 s390x

Source0: https://salsa.debian.org/minicom-team/minicom/-/archive/%{version}/%{name}-%{version}.tar.gz

# src/sysdep.h: remove cfset{i,o}speed macros for glibc
# https://salsa.debian.org/minicom-team/minicom/-/commit/964ae563cb5a78545ae1a4a3b6784c69ec73bc48
Patch0: minicom-2.10-fix-baudrate-setting.patch
# oreon url source checksums begin
%global source0_sha256 66ff82661c3cc49ab2e447f8a070ec1a64ba71d64219906d80a49da284a5d43e
%global source0_file minicom-2.10.tar.gz
# oreon url source checksums end

BuildRequires: make
BuildRequires: lockdev-devel ncurses-devel autoconf automake gettext-devel
BuildRequires: gcc
# For %%autosetup -S git:
BuildRequires: git-core
Requires: lockdev lrzsz


%description
Minicom is a simple text-based modem control and terminal emulation
program somewhat similar to MSDOS Telix. Minicom includes a dialing
directory, full ANSI and VT100 emulation, an (external) scripting
language, and other features.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/minicom-2.10.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "66ff82661c3cc49ab2e447f8a070ec1a64ba71d64219906d80a49da284a5d43e" || { echo "oreon: Source0 SHA256 mismatch for minicom-2.10.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -S git_am

cp -pr doc doc_
rm -f doc_/Makefile*


%build
#./autogen.sh
autoreconf --verbose --force --install

# Remove unused files to make sure we've got the License tag right.
# It seems this needs to be done after autoreconf, otherwise it will fail.
rm -f lib/snprintf.c

%configure
%make_build


%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}

%find_lang %{name}


%files -f %{name}.lang
%doc ChangeLog AUTHORS NEWS TODO doc_/*
%license COPYING
# DO NOT MAKE minicom SUID/SGID anything.
%{_bindir}/minicom
%{_bindir}/runscript
%{_bindir}/xminicom
%{_bindir}/ascii-xfr
%{_mandir}/man1/*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.10-2
- Prepare for Oreon 11 (RP1)
