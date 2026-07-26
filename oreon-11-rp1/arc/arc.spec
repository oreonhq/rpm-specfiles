%global source0_hash eacf870a245f155a4ba8c6f8e0fbb2e8a267aafa157f56ba7a8cb1d74fd8b5a1

Name:      arc
Version:   5.21p
Release:   33%{?dist}
Summary:   Arc archiver
License:   GPL-1.0-or-later
URL:       http://arc.sourceforge.net/
Source0:   http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# 2 small polish patches courtesy of Debian
Patch0:    arc-5.21p-spelling.patch
Patch1:    arc-5.21p-manpage-section-fix.patch
# Arc was once shareware, but has been relicensed to the GPL with permission
# of its original author. But there still is some confusing license text in the
# docs this clarifies those parts of the text (rhbz#947786)
Patch2:    arc-5.21p-clarify-license.patch
# Fix reading v1 headers
Patch3:    arc-5.21p-hdrv1-read-fix.patch
# Fix arcdie crash
Patch4:    arc-5.21p-fix-arcdie.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1179143
Patch5:    arc-5.21p-directory-traversel.patch
Patch6:    arc-5.21p-compiler-warn.patch
Patch7:    arc-5.21p-fcommon-fix.patch
# Fix compilation with newer gcc which demands proper function protypes
Patch8:    arc-5.21p-fix-function-prototypes.patch
# Fix sharing differently sized storage to avoid LTO aliasing issues
Patch9:    arc-5.21p-aliasing-fix.patch
# Fix compilation with glibc-2.43
Patch10:   arc-5.21p-glibc-2.43.patch

BuildRequires: gcc make

%description
Arc file archiver and compressor. Long since superseded by zip/unzip
but useful if you have old .arc files you need to unpack.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i -e 's,^OPT =.*$,OPT = ${RPM_OPT_FLAGS},' Makefile

%build
make %{?_smp_mflags} LIBS="$LDFLAGS"

%install
install -m 0755 -d %{buildroot}{%{_bindir},%{_mandir}/man1}
install -m 0755 arc marc %{buildroot}%{_bindir}
install -m 0644 arc.1 marc.1 %{buildroot}%{_mandir}/man1/

%files
%doc LICENSE PATCHLEVEL Readme Arc521.doc
%license COPYING
%{_bindir}/arc
%{_bindir}/marc
%{_mandir}/man1/*

%changelog
%autochangelog
