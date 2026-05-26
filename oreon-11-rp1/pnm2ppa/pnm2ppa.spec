Name: pnm2ppa
Summary: Drivers for printing to HP PPA printers
Epoch: 1
Version: 1.13
Release: 8%{?dist}
URL: http://sourceforge.net/projects/pnm2ppa 
Source: http://download.sourceforge.net/pnm2ppa/pnm2ppa-%{version}.tar.gz
# Following sourcelink is dead currently.
Source1: http://www.httptech.com/ppa/files/ppa-0.8.6.tar.gz
# Upstream sync.
Patch1: pbm2ppa-20000205.diff
# Use RPM_OPT_FLAGS.
Patch2: pnm2ppa-redhat.patch
# Don't return a local variable out of scope (bug #704568).
Patch3: pnm2ppa-coverity-return-local.patch
# FTBFS with GCC10
Patch4: pnm2ppa-gcc10.patch
# add ldflags to Makefile
Patch5: pnm2ppa-ldflags.patch
# match NOPRINTER enum with its position in global printer table
# fixes crash on aarch64
Patch6: pnm2ppa-aarch-help-crash.patch
# GCC 15 defaults to C23
Patch7: pnm2ppa-c23.patch
# oreon url source checksums begin
%global source0_sha256 1c50ea2c97b232f5bee6ac3fab408d64b6f1380f1e289ac278778a7e368e7379
%global source0_file pnm2ppa-1.13.tar.gz
%global source1_sha256 101fbb63ca49506c7d9217ff82d6f344b80df29e81e43105115002888048f72b
%global source1_file ppa-0.8.6.tar.gz
# oreon url source checksums end
# pbm2ppa, pnm2ppa - GPL-2.0-or-later
# pdq/* - GPL-2.0, but not shipped, thus not mentioned in license tag
License: GPL-2.0-or-later

# for autoreconf
BuildRequires: autoconf
# for autoreconf
BuildRequires: automake
# gcc is no longer in buildroot by default
BuildRequires: gcc
# uses make
BuildRequires: make

# foomatic is needed for using the filters in CUPS
Requires: foomatic

%description
Pnm2ppa is a color driver for HP PPA host-based printers such as the
HP710C, 712C, 720C, 722C, 820Cse, 820Cxi, 1000Cse, and 1000Cxi.
Pnm2ppa accepts Ghostscript output in PPM format and sends it to the
printer in PPA format.

Install pnm2ppa if you need to print to a PPA printer.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/pnm2ppa-1.13.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1c50ea2c97b232f5bee6ac3fab408d64b6f1380f1e289ac278778a7e368e7379" || { echo "oreon: Source0 SHA256 mismatch for pnm2ppa-1.13.tar.gz" >&2; exit 1; })
%(f=%{_sourcedir}/ppa-0.8.6.tar.gz; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "101fbb63ca49506c7d9217ff82d6f344b80df29e81e43105115002888048f72b" || { echo "oreon: Source1 SHA256 mismatch for ppa-0.8.6.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

#pbm2ppa source
%setup -q -T -D -a 1 
%patch -P 1 -p0 -b .20000205
%patch -P 2 -p1 -b .rh
%patch -P 3 -p1 -b .coverity-return-local
%patch -P 4 -p1 -b .gcc10
%patch -P 5 -p1 -b .ldflags
%patch -P 6 -p1 -b .help-aarch-crash
%patch -P 7 -p1 -b .c23

for file in docs/en/LICENSE pbm2ppa-0.8.6/LICENSE; do
 sed "s|\r||g" $file > $file.new && \
 touch -r $file $file.new && \
 mv $file.new $file
done

autoreconf -vfi

%build
# set redhat build flags
%set_build_flags
%configure
%make_build
pushd pbm2ppa-0.8.6
%make_build
popd


%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_mandir}/man1
make INSTALLDIR=%{buildroot}%{_bindir} CONFDIR=%{buildroot}%{_sysconfdir} DESTDIR=%{buildroot} \
    MANDIR=%{buildroot}%{_mandir}/man1 install
install -p -m 0755 utils/Linux/detect_ppa %{buildroot}%{_bindir}
install -p -m 0755 utils/Linux/test_ppa %{buildroot}%{_bindir}
install -p -m 0755 pbm2ppa-0.8.6/pbm2ppa  %{buildroot}%{_bindir}
install -p -m 0755 pbm2ppa-0.8.6/pbmtpg   %{buildroot}%{_bindir}
install -p -m 0644 pbm2ppa-0.8.6/pbm2ppa.conf %{buildroot}%{_sysconfdir}
install -p -m 0644 pbm2ppa-0.8.6/pbm2ppa.1   %{buildroot}%{_mandir}/man1

chmod 644 docs/en/LICENSE
mkdir -p pbm2ppa
for file in CALIBRATION CREDITS INSTALL INSTALL-MORE LICENSE README ; do
  install -p -m 0644 pbm2ppa-0.8.6/$file pbm2ppa/$file
done


%files 
%license docs/en/LICENSE
%doc docs/en/CREDITS docs/en/INSTALL docs/en/README
%doc docs/en/RELEASE-NOTES docs/en/TODO
%doc docs/en/INSTALL.REDHAT.txt docs/en/COLOR.txt docs/en/CALIBRATION.txt
%doc docs/en/INSTALL.REDHAT.html docs/en/COLOR.html docs/en/CALIBRATION.html
%doc test.ps
%doc pbm2ppa
%{_bindir}/pnm2ppa
%{_bindir}/pbm2ppa
%{_bindir}/pbmtpg
%{_bindir}/calibrate_ppa
%{_bindir}/test_ppa
%{_bindir}/detect_ppa
%{_mandir}/man1/pnm2ppa.1*
%{_mandir}/man1/pbm2ppa.1*
%config(noreplace) %{_sysconfdir}/pnm2ppa.conf
%config(noreplace) %{_sysconfdir}/pbm2ppa.conf

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:1.13-8
- Import
