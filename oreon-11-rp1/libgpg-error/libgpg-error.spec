%global source2_hash 6f57d0e17fefd2238bd037aebf03efa960641629dd61dd9d47f122a829f6e375
%global source1_hash 9b20f1e6046aaa3fe16fcd65587fd0fa5e34ceb4830f8eadc856c3e80ad57ad3
%global source0_hash 7a85413f2bc354f4f8aa832b718af122e48965e9e0eb9012ee659c13c6385c93
Name: libgpg-error
Version: 1.61
Release:        1%{?dist}
Summary:        Library for error values used by GnuPG components
URL: https://www.gnupg.org/related_software/libgpg-error/
License: LGPL-2.1-or-later AND (BSD-3-Clause OR LGPL-2.1-or-later) AND FSFULLR AND GPL-2.0-or-later
Source0:        https://www.gnupg.org/ftp/gcrypt/libgpg-error/%{name}-%{version}.tar.bz2
Source1:        https://www.gnupg.org/ftp/gcrypt/libgpg-error/%{name}-%{version}.tar.bz2.sig
Source2: https://gnupg.org/signature_key.asc
Patch1: libgpg-error-1.29-multilib.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-autopoint
BuildRequires:  gettext-devel
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  texinfo
# /oreon:deps
%description
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon and possibly more in the future.

%package devel
Summary: Development files for the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
%description devel
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon and possibly more in the future. This package
contains files necessary to develop applications using libgpg-error.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch 1 -p1 -b .multilib

autoreconf -f

# The config script already suppresses the -L if it's /usr/lib, so cheat and
# set it to a value which we know will be suppressed.
sed -i -e 's|^libdir=@libdir@$|libdir=@exec_prefix@/lib|g;s|@GPG_ERROR_CONFIG_HOST@|none|g' src/gpg-error-config.in
sed -i -e '/--variable=host/d' src/gpg-error-config-test.sh.in

# Modify configure to drop rpath for /usr/lib64
sed -i -e 's|sys_lib_dlsearch_path_spec="/lib /usr/lib|sys_lib_dlsearch_path_spec="/lib /usr/lib %{_libdir}|g' configure

%build

%configure --disable-static \
	--disable-rpath \
	--disable-languages \
	--enable-install-gpg-error-config
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libgpg-error-devel -f %{oreon_filedir}/libgpg-error-devel.list

%changelog

%autochangelog
