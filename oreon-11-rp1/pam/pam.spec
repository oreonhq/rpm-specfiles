%global source18_hash edaef632cbb643e4e7a221717a6c441a4c1a7c918e6e4d56debc3d8739b233f6
%global source1_hash e5f228456fcb94766e3360a4b3dc50b20af5be4bc08fd77f7c0df7488fa87908
%global source0_hash 2ce4765fd49df6693771ef2941f81e33d8ee14b94a81a5c7b369aa3b137b85a5
%global source2_hash 894213fafbb557d40fba28dcc66f557fa0b4bf0ab32b0e4931b1d2be47e381fc
%bcond nis %[!(0%{?rhel} >= 9)]
%global so_ver 0
%global pam_redhat_version 1.3.1
%ifarch %{java_arches}
%global build_pdf %[0 && %{undefined rhel}]
%else
%global build_pdf 0
%endif
Summary:        An extensible library which provides authentication for applications
Name: pam
Version: 1.7.3
Release:        1%{?dist}
License: BSD-3-Clause AND GPL-2.0-or-later
URL: http://www.linux-pam.org/
Source0:        https://github.com/linux-pam/linux-pam/releases/download/v%{version}/Linux-PAM-%{version}.tar.xz
Source1:        https://github.com/linux-pam/linux-pam/releases/download/v%{version}/Linux-PAM-%{version}.tar.xz.asc
Source2:        https://releases.pagure.org/pam-redhat/pam-redhat-1.3.1.tar.xz
Source3: macros.%{name}
Source5: other.pamd
Source10: config-util.pamd
Source11: dlopen.sh
Source12: system-auth.5
Source13: config-util.5
Source15: pamtmp.conf
Source17: postlogin.5
Source18: https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
Patch1:  pam-1.7.0-redhat-modules.patch
Patch2:  pam-1.5.3-unix-nomsg.patch
%global _pam_libdir %{_libdir}
%global _pam_moduledir %{_libdir}/security
%global _pam_secconfdir %{_sysconfdir}/security
%global _pam_confdir %{_sysconfdir}/pam.d
%global _pam_vendordir %{_datadir}/pam.d
Requires(meta): authselect >= 1.3
Requires: gdbm
Requires: libpwquality%{?_isa}
Requires: pam-libs%{?_isa} = %{version}-%{release}
Requires: setup
Suggests: libdb-convert-util
%if %{with nis}
%endif
# oreon:deps
BuildRequires:  audit-libs-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  docbook5-schemas
BuildRequires:  docbook5-style-xsl
BuildRequires:  elinks
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gdbm-devel
BuildRequires:  gettext-devel
BuildRequires:  libeconf-devel
BuildRequires:  libnsl2-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  openssl-devel
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig
BuildRequires:  sed
BuildRequires:  systemd
# /oreon:deps
%description
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policy without
having to recompile programs that handle authentication.

%package devel
Summary: Files needed for developing PAM-aware applications and modules for PAM
Requires: pam-libs%{?_isa} = %{version}-%{release}
%description devel
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policy without
having to recompile programs that handle authentication. This package
contains header files used for building both PAM-aware applications
and modules for use with the PAM system.

%package doc
Summary: Extra documentation for PAM.
Requires: pam = %{version}-%{release}
Obsoletes: pam-docs < 1.5.2-6
Provides: pam-docs = %{version}-%{release}
BuildArch: noarch
BuildRequires: docbook5-schemas
BuildRequires: docbook5-style-xsl
BuildRequires: elinks
BuildRequires: libxslt
%description doc
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policy without
having to recompile programs that handle authentication. The pam-doc
contains extra documentation for PAM. Currently, this includes additional
documentation in txt and html format.

%package libs
Summary: Shared libraries of the PAM package
Conflicts: pam < 1.5.2-11
%description libs
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policy without
having to recompile programs that handle authentication. The pam-libs
contains the shared libraries for PAM.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
%setup -q -n Linux-PAM-%{version} -a 2

# Add custom modules.
mv pam-redhat-%{pam_redhat_version}/* modules

cp %{SOURCE18} .

%patch -P 1 -p1 -b .redhat-modules
%patch -P 2 -p1 -b .nomsg

%build

%meson \
  -Daudit=enabled \
  -Delogind=disabled \
%if %{without nis}
  -Dnis=disabled \
%endif
  -Dlogind=disabled \
  -Dopenssl=enabled \
  -Dpam_userdb=enabled \
  -Dpwaccess=disabled \
  -Ddb=gdbm \
  -Dselinux=enabled \
  -Dvendordir=''
%meson_build
%install
install -D -m 644 %{SOURCE3} %{buildroot}%{_rpmconfigdir}/macros.d/macros.%{name}
%meson_install
ln -sf pam_sepermit.so %{buildroot}%{_pam_moduledir}/pam_selinux_permit.so
rm -rf %{buildroot}%{_datadir}/doc/Linux-PAM
rm -f %{buildroot}%{_sysconfdir}/environment
install -d -m 755 %{buildroot}%{_pam_confdir}
install -d -m 755 %{buildroot}%{_pam_vendordir}
install -m 644 %{SOURCE5} %{buildroot}%{_pam_confdir}/other
install -m 644 %{SOURCE10} %{buildroot}%{_pam_confdir}/config-util
install -m 600 /dev/null %{buildroot}%{_pam_secconfdir}/opasswd
install -d -m 755 %{buildroot}/var/log
install -d -m 755 %{buildroot}/var/run/faillock
install -m 644 %{SOURCE12} %{SOURCE13} %{SOURCE17} %{buildroot}%{_mandir}/man5/
ln -sf system-auth.5 %{buildroot}%{_mandir}/man5/password-auth.5
ln -sf system-auth.5 %{buildroot}%{_mandir}/man5/fingerprint-auth.5
ln -sf system-auth.5 %{buildroot}%{_mandir}/man5/smartcard-auth.5
for phase in auth acct passwd session ; do
  ln -sf pam_unix.so %{buildroot}%{_pam_moduledir}/pam_unix_${phase}.so
done
for lib in libpam libpamc libpam_misc ; do
  rm -f %{buildroot}%{_pam_libdir}/${lib}.la
done
rm -f %{buildroot}%{_pam_moduledir}/*.la
%if "%{_pam_libdir}" != "%{_libdir}"
install -d -m 755 %{buildroot}%{_libdir}
for lib in libpam libpamc libpam_misc ; do
  pushd %{buildroot}%{_libdir}
  ln -sf %{_pam_libdir}/${lib}.so.*.* ${lib}.so
  popd
  rm -f %{buildroot}%{_pam_libdir}/${lib}.so
done
%endif
rm -fr %{buildroot}/usr/share/doc/pam
install -m644 -D %{SOURCE15} %{buildroot}%{_prefix}/lib/tmpfiles.d/pam.conf
install -m644 -D %{_vpath_builddir}/modules/pam_namespace/pam_namespace.service \
  %{buildroot}%{_unitdir}/pam_namespace.service
install -d -m 755 %{buildroot}%{_pkgdocdir}/{adg/html,mwg/html,sag/html}
install -p -m 644 doc/specs/rfc86.0.txt %{buildroot}%{_pkgdocdir}
for i in adg mwg sag; do
  install -p -m 644 %{_vpath_builddir}/doc/$i/*.txt %{buildroot}%{_pkgdocdir}/$i
  cp -pr %{_vpath_builddir}/doc/$i/html/* %{buildroot}%{_pkgdocdir}/$i/html
done
find %{buildroot}%{_pkgdocdir} -type d | xargs chmod 755
find %{buildroot}%{_pkgdocdir} -type f | xargs chmod 644
%find_lang Linux-PAM
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

for dir in modules/pam_* ; do
if [ -d ${dir} ] ; then
  [ ${dir} = "modules/pam_lastlog" ] && continue
  [ ${dir} = "modules/pam_selinux" ] && continue
  [ ${dir} = "modules/pam_sepermit" ] && continue
  [ ${dir} = "modules/pam_tty_audit" ] && continue
  if ! ls -1 %{buildroot}%{_pam_moduledir}/`basename ${dir}`*.so ; then
    echo ERROR `basename ${dir}` did not build a module.
    exit 1
  fi
fi
done
/sbin/ldconfig -n %{buildroot}%{_pam_libdir}
for module in %{buildroot}%{_pam_moduledir}/pam*.so ; do
  if ! env LD_LIBRARY_PATH=%{buildroot}%{_pam_libdir} \
       %{SOURCE11} -ldl -lpam -L%{buildroot}%{_libdir} ${module} ; then
    echo ERROR module: ${module} cannot be loaded.
    exit 1
  fi
done
%files -f %{oreon_filedir}/main.list
%files -n pam-devel -f %{oreon_filedir}/pam-devel.list
%files -n pam-doc -f %{oreon_filedir}/pam-doc.list
%files -n pam-libs -f %{oreon_filedir}/pam-libs.list

%changelog

%autochangelog
