%global source0_hash 036d96991646d0449ed0aa952e4fbe21b476ce994abc276e49d30e686708bd37
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: unzip
Version: 6.0
Release: 1%{?dist}
Summary: Extract files from zip archives
License: Info-ZIP
URL: http://infozip.sourceforge.net/
Source0: https://downloads.sourceforge.net/infozip/unzip60.tar.gz
Patch0: unzip-6.0-bzip2-configure.patch
Patch1: unzip-6.0-exec-shield.patch
Patch2: unzip-6.0-close.patch
Patch3: unzip-6.0-attribs-overflow.patch
Patch4: unzip-6.0-configure.patch
Patch5: unzip-6.0-manpage-fix.patch
Patch6: unzip-6.0-fix-recmatch.patch
Patch7: unzip-6.0-symlink.patch
Patch8: unzip-6.0-caseinsensitive.patch
Patch9: unzip-6.0-format-secure.patch
Patch10: unzip-6.0-valgrind.patch
Patch11: unzip-6.0-x-option.patch
Patch12: unzip-6.0-overflow.patch
Patch13: unzip-6.0-cve-2014-8139.patch
Patch14: unzip-6.0-cve-2014-8140.patch
Patch15: unzip-6.0-cve-2014-8141.patch
Patch16: unzip-6.0-overflow-long-fsize.patch
Patch17: unzip-6.0-heap-overflow-infloop.patch
Patch18: unzip-6.0-alt-iconv-utf8.patch
Patch19: unzip-6.0-alt-iconv-utf8-print.patch
Patch20: 0001-Fix-CVE-2016-9844-rhbz-1404283.patch
Patch21: unzip-6.0-timestamp.patch
Patch22: unzip-6.0-cve-2018-1000035-heap-based-overflow.patch
Patch23: unzip-6.0-cve-2018-18384.patch
Patch24: unzip-6.0-COVSCAN-fix-unterminated-string.patch
Patch25: unzip-zipbomb-part1.patch
Patch26: unzip-zipbomb-part2.patch
Patch27: unzip-zipbomb-part3.patch
Patch28: unzip-zipbomb-manpage.patch
Patch29: unzip-zipbomb-part4.patch
Patch30: unzip-zipbomb-part5.patch
Patch31: unzip-zipbomb-part6.patch
Patch32: unzip-zipbomb-part7.patch
Patch33: unzip-zipbomb-switch.patch
Patch34: unzip-gnu89-build.patch
Patch35: unzip-6.0-wcstombs-fortify.patch

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: bzip2-devel
%endif

%description
unzip lists, tests, and extracts zip archives.

%prep
%oreon_sha256
%autosetup -n unzip60 -p1

%build
%{_oreon_flags} make -f unix/Makefile \
  CF_NOOPT="-I. -DUNIX %{_oreon_cflags} -DNOMEMCPY -DIZ_HAVE_UXUIDGID -DNO_LCHMOD" \
  LFLAGS2="%{_oreon_ldflags}" generic_gcc

%install
make -f unix/Makefile prefix=%{buildroot}%{_prefix} MANDIR=%{buildroot}%{_mandir}/man1 INSTALL="cp -p" install
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license LICENSE COPYING.OLD
