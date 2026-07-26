%global source0_hash 6bc60fe53c9e9c828a6d7f3675da11ad7fb54491863584e01c1051740fe2a286

Summary: Tools to support ATM networking under Linux
Name: linux-atm
Version: 2.5.1
Release: 46%{?dist}
# The licensing here is a mess. This is as close to accurate as possible.
License: GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL: http://linux-atm.sourceforge.net/
Source0: http://downloads.sf.net/%{name}/%{name}-%{version}.tgz

BuildRequires: automake
BuildRequires: byacc
BuildRequires: flex
BuildRequires: flex-static
# Older kernel headers had broken ATM includes
BuildRequires: glibc-kernheaders >= 2.4-9.1.88
BuildRequires: libtool
BuildRequires: make

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

# Patch from Debian to sanify syslogging
Patch2: linux-atm-2.5.0-open-macro.patch
Patch3: linux-atm-2.5.0-disable-ilmidiag.patch
Patch4: linux-atm-gcc43.patch
Patch5: man-pages.patch
Patch6: add-string-formatting-to-build-with-gcc7.patch
Patch7: remove-define-hacks.patch
Patch8: siocgstamp.patch
# The ZeitNet ZN122x ATM driver was dropped in kernel 5.19, so the zntune binary
# can't be built anymore
# See: https://github.com/torvalds/linux/commit/052e1f01bfae8be6f31b61ed3a2356edfca855dc
Patch9: linux-atm-2.5.1-disable-zntune.patch
Patch10: linux-atm-c99.patch
Patch11: linux-atm-use_socklen_t.patch
Patch12: linux-atm-dont-use-bool-keyword.patch

%description
Tools to support ATM networking under Linux.

%package libs
Summary: Linux ATM API library
License: LGPL-2.0-or-later

%description libs
This package contains the ATM library required for user space ATM tools.

%package libs-devel
Summary: Development files for Linux ATM API library
Requires: linux-atm-libs = %{version}-%{release}
Requires: glibc-kernheaders >= 2.4-9.1.88

%description libs-devel
This package contains header files and libraries for development using the
Linux ATM API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

iconv -f iso8859-1 -t utf8 < src/extra/ANS/e164_cc > src/extra/ANS/e164_cc.1
mv src/extra/ANS/e164_cc.1 src/extra/ANS/e164_cc
iconv -f iso8859-1 -t utf8 < doc/atm-linux-howto.txt > doc/atm-linux-howto.txt.1
mv doc/atm-linux-howto.txt.1 doc/atm-linux-howto.txt

%build
./autotools
CFLAGS="%optflags -D_LINUX_TIME_H"
%configure --disable-static
# Drop the default RPATH
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/#_beware_of_rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make

%install
#rm -rf $RPM_BUILD_ROOT _doc CVS ANS doc/{\.cvsignore,CVS} init-redhat/{CVS,\.cvsignore}
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT/%{_libdir}/libatm.{a,la}
install -m 0644 src/config/hosts.atm $RPM_BUILD_ROOT/etc/
# Selectively sort what we want included in %%doc
mkdir _doc
cp -a doc/ src/config/init-redhat/ src/extra/ANS/ _doc/
rm -f _doc/Makefile* _doc/*/Makefile* _doc/doc/*.sgml
chmod 0644 src/extra/ANS/{atm,pdf2e164_cc.pl,hosts2ans.pl}
chmod 0644 _doc/{ANS/pdf2e164_cc.pl,ANS/hosts2ans.pl,init-redhat/atm,doc/atm-linux-howto.txt}

# remove CVS files from installation
rm -rf _doc/ANS
rm -rf _doc/doc/{.cvsignore,CVS}
rm -rf _doc/init-redhat/{CVS,.cvsignore}

%ldconfig_scriptlets libs

%files
%{!?_licensedir:%global license %%doc}
%license COPYING*
%doc AUTHORS BUGS ChangeLog NEWS README THANKS _doc/*
%config(noreplace) /etc/atmsigd.conf
%config(noreplace) /etc/hosts.atm
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man4/*
%{_mandir}/man7/*
%{_mandir}/man8/*

%files libs
%{!?_licensedir:%global license %%doc}
%license COPYING.LGPL
%{_libdir}/libatm.so.*

%files libs-devel
%{_includedir}/*
%{_libdir}/libatm.so

%changelog
%autochangelog
