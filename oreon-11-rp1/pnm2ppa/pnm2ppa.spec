%global source0_hash 1c50ea2c97b232f5bee6ac3fab408d64b6f1380f1e289ac278778a7e368e7379
Name: pnm2ppa
Summary:        Drivers for printing to HP PPA printers
Epoch: 1
Version: 1.13
Release:        1%{?dist}
URL: http://sourceforge.net/projects/pnm2ppa 
Source0:        https://downloads.sourceforge.net/pnm2ppa/pnm2ppa-1.13.tar.gz
Patch2: pnm2ppa-redhat.patch
Patch3: pnm2ppa-coverity-return-local.patch
Patch4: pnm2ppa-gcc10.patch
Patch5: pnm2ppa-ldflags.patch
Patch6: pnm2ppa-aarch-help-crash.patch
Patch7: pnm2ppa-c23.patch
License: GPL-2.0-or-later
Requires: foomatic
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Pnm2ppa is a color driver for HP PPA host-based printers such as the
HP710C, 712C, 720C, 722C, 820Cse, 820Cxi, 1000Cse, and 1000Cxi.
Pnm2ppa accepts Ghostscript output in PPM format and sends it to the
printer in PPA format.

Install pnm2ppa if you need to print to a PPA printer.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%patch -P 2 -p1 -b .rh
%patch -P 3 -p1 -b .coverity-return-local
%patch -P 4 -p1 -b .gcc10
%patch -P 5 -p1 -b .ldflags
%patch -P 6 -p1 -b .help-aarch-crash
%patch -P 7 -p1 -b .c23

for file in docs/en/LICENSE; do
 sed "s|\r||g" $file > $file.new && \
 touch -r $file $file.new && \
 mv $file.new $file
done

autoreconf -vfi

%build

%set_build_flags
%configure
%make_build
%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_mandir}/man1
make INSTALLDIR=%{buildroot}%{_bindir} CONFDIR=%{buildroot}%{_sysconfdir} DESTDIR=%{buildroot} \
    MANDIR=%{buildroot}%{_mandir}/man1 install
install -p -m 0755 utils/Linux/detect_ppa %{buildroot}%{_bindir}
install -p -m 0755 utils/Linux/test_ppa %{buildroot}%{_bindir}
chmod 644 docs/en/LICENSE
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:1.13-8
- Import
