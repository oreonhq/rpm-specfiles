%global source0_hash 400f51b59d85116e79b844f2d5dbbad4759442a789b401a94aa5052c3d7a4aa9
%global source1_hash be259fe1f56d721ebf2c9a0a774110cdd2503777c69169abaa1e4477542f7de1
%bcond_without cvs_enables_contrib
%bcond_with cvs_enables_extra_test
%bcond_without cvs_enables_kerberos
%bcond_without cvs_enables_pam
%bcond_without cvs_enables_pdf
%bcond_with cvs_enables_xinetd
Name:       cvs
Version:    1.11.23
Release:        1%{?dist}
Summary:        Concurrent Versions System
URL:        https://cvs.nongnu.org/
License:    GPL-2.0-or-later AND GPL-1.0-or-later AND Latex2e-translated-notice AND LicenseRef-Fedora-Public-Domain
Source0:        https://ftp.gnu.org/non-gnu/cvs/source/stable/%{version}/cvs-%{version}.tar.bz2
Source1:    https://ftp.gnu.org/non-gnu/cvs/source/stable/%{version}/cvs-%{version}.tar.bz2.sig
Source2:    gpgkey-CB6A07CA90C54234E8A3C8D02C3D4E4C17F231A4.gpg
Source3:    cvs.xinetd
Source4:    cvs.pam
Source5:    cvs.sh
Source6:    cvs.csh
Source7:    cvs@.service
Source8:    cvs.socket
Source9:    cvs.target
Source10:   cvs.sh.5
Source11:   cvs.csh.5
Patch0:     cvs-1.11.23-cvspass.patch
Patch1:     cvs-1.11.19-extzlib.patch
Patch2:     cvs-1.11.19-netbsd-tag.patch
Patch3:     cvs-1.11.19-abortabort.patch
Patch4:     cvs-1.11.1p1-bs.patch
Patch5:     cvs-1.11.21-proxy.patch
Patch7:     cvs-1.11.19-logmsg.patch
Patch8:     cvs-1.11.19-tagname.patch
Patch9:     cvs-1.11.19-comp.patch
Patch11:    cvs-1.11.19-tmp.patch
Patch12:    cvs-1.11.21-pam.patch
Patch13:    cvs-1.11.21-diff.patch
Patch14:    cvs-1.11.21-diff-kk.patch
Patch15:    cvs-1.11.21-sort.patch
Patch17:    cvs-1.11.22-ipv6-proxy.patch
Patch19:    cvs-1.11.23-getline64.patch
Patch20:    cvs-1.11.22-stdinargs.patch
Patch21:    cvs-1.11.23-cve-2010-3846.patch
Patch22:    cvs-1.11.23-remove_undefined_date_from_cvs_1_header.patch
Patch23:    cvs-1.11.23-sanity.patch
Patch24:    cvs-1.11.23-make_make_check_sanity_testing_verbose.patch
Patch25:    cvs-1.11.23-Set-PAM_TTY-and-PAM_RHOST-on-PAM-authentication.patch
Patch26:    cvs-1.11.23-Back-port-KeywordExpand-configuration-keyword.patch
Patch27:    cvs-1.11.23-Allow-CVS-server-to-use-any-Kerberos-key-with-cvs-se.patch
Patch28:    cvs-1.11.23-Fix-proxy-response-parser.patch
Patch29:    cvs-1.11.23-doc-Add-mandatory-argument-to-sp.patch
Patch30:    cvs-1.11.23-crypt-2.diff
Patch31:    cvs-1.11.23-Pass-compilation-with-Wformat-security.patch
Patch32:    cvs-1.11.23-Fix-CVE-2017-12836.patch
Patch33:    cvs-1.11.23-Close-a-configuration-file-on-a-syntax-error.patch
Patch34:    cvs-1.11.23-Use-diff-label.patch
Patch35:    cvs-1.11.23-c99.patch
Patch36:    cvs-1.11.23-tests-Call-nonobsolete-grep-F.patch
Patch37:    cvs-1.11.23-Adapt-to-changes-in-GCC-15.patch
%if %{with cvs_enables_pdf}
%endif
%if %{with cvs_enables_kerberos}
%endif
%if %{with cvs_enables_pam}
%endif
%if %{with cvs_enables_contrib}
%endif
Requires:       vim-minimal
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  ghostscript
BuildRequires:  glibc-common
BuildRequires:  gnupg2
BuildRequires:  groff
BuildRequires:  gzip
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  perl-generators
BuildRequires:  systemd
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  vim-minimal
BuildRequires:  zlib-devel
# /oreon:deps
%description
CVS (Concurrent Versions System) is a version control system that can
record the history of your files (usually, but not always, source
code). CVS only stores the differences between versions, instead of
every version of every file you have ever created. CVS also keeps a log
of who, when, and why changes occurred.

CVS is very helpful for managing releases and controlling the
concurrent editing of source files among multiple authors. Instead of
providing version control for a collection of files in a single
directory, CVS provides version control for a hierarchical collection
of directories consisting of revision controlled files. These
directories and files can then be combined together to form a software
release.

%if %{with cvs_enables_contrib}
%package contrib
Summary: Unsupported contributions collected by CVS developers
License: GPL-2.0-or-later AND check-cvs
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
%description contrib
Scripts sent to CVS developers by contributors around the world. These
contributions are really unsupported.
%endif

%if %{with cvs_enables_xinetd}
%package inetd
Summary: CVS server configuration for xinetd
License: GPL-1.0-or-later
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires: xinetd
%description inetd
A CVS server can be run locally, via a remote shell or by an inetd server.
This package provides a configuration for xinetd, an inetd implementation.
%endif

%package doc
Summary: Additional documentation for Concurrent Versions System
License: GPL-1.0-or-later AND Latex2e-translated-notice
%if !%{with cvs_enables_pdf}
BuildArch: noarch
%endif
%description doc
FAQ, RCS format description, parallel development how-to, and Texinfo
pages in PDF.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch -p1 -P 0
%patch -p1 -P 1
%patch -p1 -P 2
%patch -p1 -P 3
%if !%{with cvs_enables_extra_test}
%patch -p1 -P 4
%endif
%patch -p1 -P 5
%patch -p1 -P 7
%patch -p1 -P 8
%patch -p1 -P 9
%patch -p1 -P 11
%if %{with cvs_enables_pam}
%patch -p1 -P 12
%endif
%patch -p1 -P 13
%patch -p1 -P 14
%patch -p1 -P 15
%patch -p1 -P 17
%patch -p1 -P 19
%patch -p1 -P 20
%patch -p1 -P 21
%patch -p1 -P 22
%patch -p1 -P 23
%patch -p1 -P 24
%patch -p1 -P 25
%patch -p1 -P 26
%patch -p1 -P 27
%patch -p1 -P 28
%patch -p1 -P 29
%patch -p1 -P 30
%patch -p1 -P 31
%patch -p1 -P 32
%patch -p1 -P 33
%patch -p1 -P 34
%patch -p1 -P 35
%patch -p1 -P 36
%patch -p1 -P 37

# Remove bundled autotools files, they will be regenerated in %%build phase.
# Keep acinclude.m4 becuse it defines ACX_WITH_GSSAPI.
rm aclocal.m4 compile configure doc/mdate-sh doc/texinfo.tex \
    install-sh mdate-sh missing mkinstalldirs ylwrap
rm {.,contrib,diff,doc,lib,man,src,tools,vms,windows-NT,windows-NT/SCC,zlib}/Makefile.in
# Remove bundled zlib
rm -r zlib
# Remove unused code
find emx -type f \! -name Makefile.in -delete
find os2 -type f \! -name Makefile.in -delete
find vms -type f \! \( -name Makefile.am -o -name config.h.in \) -delete
find windows-NT -type f \! \( -name Makefile.am -o -name config.h.in -o -name fix-msvc-mak\* \) -delete
truncate --size=0 lib/fncase.c lib/fnmatch.c lib/fnmatch.h.in lib/gethostname.c \
    lib/memmove.c lib/mkdir.c lib/rename.c lib/strerror.c
# Remove pregenerated code
rm lib/getdate.c
# Remove pregenerated documentation
%if %{with cvs_enables_pdf}
rm doc/*.pdf
%endif
# Convert files to UTF-8
for F in FAQ; do
    iconv -f ISO-8859-1 -t UTF-8 < "$F" > "${F}.UTF8"
    touch -r "$F"{,.UTF8}
    mv "$F"{.UTF8,}
done

%build

autoreconf --force --install
%if %{with cvs_enables_pam}
    PAM_CONFIG="--enable-pam"
%endif
%if %{with cvs_enables_kerberos}
    k5prefix=`krb5-config --prefix`
    CPPFLAGS=-I${k5prefix}/include/kerberosIV; export CPPFLAGS
    CFLAGS=-I${k5prefix}/include/kerberosIV; export CFLAGS
    LIBS="-lk5crypto"; export LIBS
    KRB_CONFIG="--with-gssapi --without-krb4 --enable-encryption"
%endif
%configure CFLAGS="$CFLAGS $RPM_OPT_FLAGS \
    -D_FILE_OFFSET_BITS=64 %-D_LARGEFILE64_SOURCE" \
    $PAM_CONFIG $KRB_CONFIG CSH=/bin/csh
%{make_build} all doc
%check

if [ $(id -u) -ne 0 ] ; then
    make check
fi
%install
%{make_install}
gzip $RPM_BUILD_ROOT/%{_infodir}/cvs* || true
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
%if %{with cvs_enables_xinetd}
    install -D -m 644 %{SOURCE3} $RPM_BUILD_ROOT/%{_sysconfdir}/xinetd.d/%{name}
%endif
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/%{name}
%if %{with cvs_enables_pam}
    install -D -m 644 %{SOURCE4} $RPM_BUILD_ROOT/%{_sysconfdir}/pam.d/cvs
%endif
install -D -m 644 %{SOURCE5} $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/cvs.sh
install -D -m 644 %{SOURCE6} $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/cvs.csh
install -p -m 644 -D %{SOURCE7} $RPM_BUILD_ROOT%{_unitdir}/cvs\@.service
install -p -m 644 -D %{SOURCE8} $RPM_BUILD_ROOT%{_unitdir}/cvs.socket
install -p -m 644 -D %{SOURCE9} $RPM_BUILD_ROOT%{_unitdir}/cvs.target
install -D -m 644 %{SOURCE10} $RPM_BUILD_ROOT/%{_mandir}/man5/cvs.sh.5
install -D -m 644 %{SOURCE11} $RPM_BUILD_ROOT/%{_mandir}/man5/cvs.csh.5
%if !%{with cvs_enables_contrib}
rm -f $RPM_BUILD_ROOT/%{_bindir}/rcs2log
rm -fr $RPM_BUILD_ROOT/%{_datadir}/%{name}
%oreon_autofiles cvs-contrib usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cvs-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%post

%systemd_post cvs.socket
exit 0
%preun

%systemd_preun cvs.socket
%systemd_preun cvs.target
exit 0
%postun

%systemd_postun_with_restart cvs.socket
%files -f %{oreon_filedir}/main.list
%files -n cvs-contrib -f %{oreon_filedir}/cvs-contrib.list
%files -n cvs-doc -f %{oreon_filedir}/cvs-doc.list

%changelog

%autochangelog
