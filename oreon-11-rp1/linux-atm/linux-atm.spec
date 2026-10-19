%global source0_hash 9645481a2b16476b59220aa2d6bc5bc41043f291326c9b37581018fbd16dd53a
Summary:        Tools to support ATM networking under Linux
Name: linux-atm
Version: 2.5.2
Release:        1%{?dist}
License: GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL: http://linux-atm.sourceforge.net/
Source0:        https://sourceforge.net/projects/linux-atm/files/linux-atm/%{version}/%{name}-%{version}.tar.gz/download#/%{name}-%{version}.tar.gz
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Patch2: linux-atm-2.5.0-open-macro.patch
Patch3: linux-atm-2.5.0-disable-ilmidiag.patch
Patch4: linux-atm-gcc43.patch
Patch5: man-pages.patch
Patch6: add-string-formatting-to-build-with-gcc7.patch
Patch7: remove-define-hacks.patch
Patch8: siocgstamp.patch
Patch9: linux-atm-2.5.1-disable-zntune.patch
Patch10: linux-atm-c99.patch
Patch11: linux-atm-use_socklen_t.patch
Patch12: linux-atm-dont-use-bool-keyword.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  flex-static
BuildRequires:  glibc-kernheaders
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
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
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make
%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT/%{_libdir}/libatm.{a,la}
install -m 0644 src/config/hosts.atm $RPM_BUILD_ROOT/etc/
mkdir _doc
cp -a doc/ src/config/init-redhat/ src/extra/ANS/ _doc/
rm -f _doc/Makefile* _doc/*/Makefile* _doc/doc/*.sgml
chmod 0644 src/extra/ANS/{atm,pdf2e164_cc.pl,hosts2ans.pl}
chmod 0644 _doc/{ANS/pdf2e164_cc.pl,ANS/hosts2ans.pl,init-redhat/atm,doc/atm-linux-howto.txt}
rm -rf _doc/ANS
rm -rf _doc/doc/{.cvsignore,CVS}
rm -rf _doc/init-redhat/{CVS,.cvsignore}
%ldconfig_scriptlets libs
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n linux-atm-libs -f %{oreon_filedir}/linux-atm-libs.list
%files -n linux-atm-libs-devel -f %{oreon_filedir}/linux-atm-libs-devel.list

%changelog

%autochangelog
