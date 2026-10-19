%global source0_hash b8e72182b2ec96a3574e2998c47b7aaa64cc20ce000d8e9ac313cc07cecf28c7
%global source1_hash 5ce64827283cae93885b99db89f94fbdb5de5f9bea26ed0fd99e698b40c61547
Summary:        A GNU stream text editor
Name: sed
Version: 4.10
Release:        1%{?dist}
License: GPL-3.0-or-later
URL: http://sed.sourceforge.net/
Source0:        https://ftp.gnu.org/gnu/sed/sed-%{version}.tar.xz
Source1: http://sed.sourceforge.net/sedfaq.txt
Patch0: sed-b-flag.patch
Patch1: sed-c-flag.patch
Patch3: sed-regexp-cache-size.patch
%ifarch %{valgrind_arches}
%endif
Provides: /bin/sed
Provides: bundled(gnulib)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  glibc-langpack-el
BuildRequires:  glibc-langpack-en
BuildRequires:  glibc-langpack-ru
BuildRequires:  libacl-devel
BuildRequires:  libselinux-devel
BuildRequires:  make
BuildRequires:  perl(FileHandle)
BuildRequires:  perl-Getopt-Long
# /oreon:deps
%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive)
editor.  Sed takes text as input, performs an operation or set of
operations on the text and outputs the modified text.  The operations
that sed performs (substitutions, deletions, insertions, etc.) can be
specified in a script file or from the command line.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure 
%make_build
sed -i s/"SELinux is enabled on this system."// ./doc/sed.1
sed -i s/"SELinux is disabled on this system."// ./doc/sed.1
install -m 644 -p %{SOURCE1} sedfaq.txt
gzip -9 sedfaq.txt
%check

echo ====================TESTING=========================
make check
echo ====================TESTING END=====================
%install
rm -rf ${RPM_BUILD_ROOT}
%make_install
rm -f ${RPM_BUILD_ROOT}/%{_infodir}/dir
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
