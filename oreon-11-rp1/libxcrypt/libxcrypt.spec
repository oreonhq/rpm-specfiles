%global source3_hash 3b86e778174be05eb880a4f2411796b23bffe4649f8e19ba902dc6d9ca76b17e
%global source2_hash 3a2b9dd46fcb218a5ec628452db45bb14825a9f2d0a7301ec154cf87897eec0e
%global source1_hash 11df2b889929d4923eed6298ba44c6e746c9ca5b9de41bd9b1b1a694a2aea65e
%global source0_hash 71513a31c01a428bccd5367a32fd95f115d6dac50fb5b60c779d5c7942aec071
%bcond_with    new_api
%bcond_without compat_pkg
%if %{with new_api} && %{with compat_pkg}
%bcond_without enosys_stubs
%else
%bcond_with    enosys_stubs
%endif
%bcond_without staticlib
%bcond_with    bootstrap
%if %{with new_api}
%global soc  2
%global sol  0
%global sof  0
%global sov  %{soc}.%{sol}.%{sof}
%else
%global soc  1
%global sol  1
%global sof  0
%global sov  %{soc}.%{sol}.%{sof}
%endif
%if %{with compat_pkg}
%global csoc 1
%global csol 1
%global csof 0
%global csov %{csoc}.%{csol}.%{csof}
%endif
%global glibc_minver     2.28
%global perl_minver      5.14
%global man_pages_minver 4.15-3
%global hash_methods   all
%if %{with new_api}
%global obsolete_api   no
%else
%global obsolete_api   glibc
%endif
%if %{with compat_pkg}
%global compat_methods all
%global compat_api     glibc
%endif
%if %{with enosys_stubs}
%global enosys_stubs   yes
%else
%global enosys_stubs   no
%endif
%global distname .distribution
%global _configure "$(realpath ../configure)"
%global nvrt_str %{name}-%{version}-%{release}.%{_target_cpu}
%global mktemplate %{nvrt_str}-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
%global config_cache %(mktemp -tu %{mktemplate}-config.cache)
%global common_configure_options           \\\
  --cache-file=%{config_cache}             \\\
  --disable-failure-tokens                 \\\
  --disable-silent-rules                   \\\
  --enable-shared                          \\\
%if %{with staticlib}                      \
  --enable-static                          \\\
%else                                      \
  --disable-static                         \\\
%endif                                     \
  --disable-valgrind                       \\\
  --srcdir=$(realpath ..)                  \\\
  --with-pkgconfigdir=%{_libdir}/pkgconfig
%global _fipsdir %{_libdir}/fipscheck
%define __spec_install_post                 \
%{?__debug_package:%{__debug_install_post}} \
%{__arch_install_post}                      \
%{__os_install_post}                        \
libdir="%{buildroot}%{_libdir}"             \
fipsdir="$libdir/fipscheck"                 \
mkdir -p $fipsdir                           \
fipshmac -d $fipsdir                        \\\
  $libdir/libcrypt.so.%{sov}                \
ln -s libcrypt.so.%{sov}.hmac               \\\
  $fipsdir/libcrypt.so.%{soc}.hmac          \
if [[ %{with staticlib} == 1 ]]; then       \
  fipshmac -d $fipsdir                      \\\
    $libdir/libcrypt.a                      \
  if [[ %{without new_api} == 1 ]]; then    \
    ln -s .libcrypt.a.hmac                  \\\
      $fipsdir/libxcrypt.a.hmac             \
  fi                                        \
fi                                          \
if [[ %{with compat_pkg} == 1 ]]; then      \
  fipshmac -d $fipsdir                      \\\
    $libdir/libcrypt.so.%{csov}             \
  ln -s libcrypt.so.%{csov}.hmac            \\\
    $fipsdir/libcrypt.so.%{csoc}.hmac       \
fi                                          \
%{nil}
%global _ld_strict_symbol_defs 1
Name:           libxcrypt
Version:        4.5.2
Release:        3%{?dist}
Summary:        Extended crypt library for descrypt, md5crypt, bcrypt, and others
License:        LGPL-2.1-or-later AND BSD-3-Clause AND BSD-2-Clause AND BSD-2-Clause-FreeBSD AND 0BSD AND CC0-1.0 AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/besser82/%{name}
Source0:        https://github.com/besser82/libxcrypt/releases/download/v4.5.2/libxcrypt-4.5.2.tar.xz
Source1:        https://github.com/besser82/libxcrypt/releases/download/v4.5.2/libxcrypt-4.5.2.tar.xz.asc
Source2:        https://github.com/besser82/libxcrypt/releases/download/v4.5.2/libxcrypt-gpgkey.asc
Source3:        https://github.com/besser82/libxcrypt/releases/download/v4.5.2/libxcrypt-4.5.2.tar.xz.sha256sum
Patch0000:        https://github.com/besser82/libxcrypt/commit/174c24d6e87a.patch#/libxcrypt-4.5.2-Werror_discarded-qualifiers.patch
Patch3000:        https://github.com/besser82/libxcrypt/archive/refs/tags/v4.5.2.tar.gz
%if %{without bootstrap}
%endif
%if 0%{?trans_pkg}
%endif
%if 0%{?trans_pkg}
Obsoletes:      libcrypt-nss           < %{glibc_minver}
Provides:       libcrypt-nss           = %{glibc_minver}
Provides:       libcrypt-nss%{?_isa}   = %{glibc_minver}
Obsoletes:      libcrypt               < %{glibc_minver}
Provides:       libcrypt               = %{glibc_minver}
Provides:       libcrypt%{?_isa}       = %{glibc_minver}
Obsoletes:      %{name}-common         < 4.3.3-4
Provides:       %{name}-common         = %{version}-%{release}
Requires:       glibc%{?_isa}         >= %{glibc_minver}
%endif
%if %{with new_api} && %{without compat_pkg}
Obsoletes:      %{name}-compat         < %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  fipscheck
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  libxcrypt-compat
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-interpreter
# /oreon:deps
%description
libxcrypt is a modern library for one-way hashing of passwords.
It supports a wide variety of both modern and historical hashing
methods: yescrypt, gost-yescrypt, sm3-yescrypt, scrypt, bcrypt,
sha512crypt, sha256crypt, sm3crypt, md5crypt, SunMD5, sha1crypt,
NT, bsdicrypt, bigcrypt, and descrypt.  It provides the traditional
Unix crypt and crypt_r interfaces, as well as a set of extended
interfaces pioneered by Openwall Linux, crypt_rn, crypt_ra,
crypt_gensalt, crypt_gensalt_rn, and crypt_gensalt_ra.

libxcrypt is intended to be used by login(1), passwd(1), and other
similar programs; that is, to hash a small number of passwords during
an interactive authentication dialogue with a human.  It is not suitable
for use in bulk password-cracking applications, or in any other situation
where speed is more important than careful handling of sensitive data.
However, it is intended to be fast and lightweight enough for use in
servers that must field thousands of login attempts per minute.

%if %{with new_api}
This version of the library does not provide the legacy API functions
that have been provided by glibc's libcrypt.so.1.
%endif

%if %{with compat_pkg}
%package        compat
Summary:        Compatibility library providing legacy API functions
%if %{without bootstrap}
BuildRequires:  libxcrypt-compat
%endif
Requires:       %{name}%{?_isa}        = %{version}-%{release}
%description    compat
This package contains the library providing the compatibility API
for applications that are linked against glibc's libxcrypt, or that
are still using the unsafe and deprecated, encrypt, encrypt_r,
setkey, setkey_r, and fcrypt functions, which are still required by
recent versions of POSIX, the Single UNIX Specification, and various
other standards.

All existing binary executables linked against glibc's libcrypt should
work unmodified with the library supplied by this package.
%endif

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa}        = %{version}-%{release}
Requires:       glibc-devel%{?_isa}
%if 0%{?trans_pkg}
Conflicts:      man-pages              < %{man_pages_minver}
Requires:       glibc-devel%{?_isa}   >= %{glibc_minver}
%endif
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with staticlib}
%package        static
Summary:        Static library for -static linking with %{name}
Requires:       %{name}-devel%{?_isa}  = %{version}-%{release}
Requires:       glibc-static%{?_isa}
%if 0%{?trans_pkg}
Requires:       glibc-static%{?_isa}  >= %{glibc_minver}
%endif
%description    static
This package contains the libxcrypt static library for -static
linking.

You don't need this, unless you link statically, which is highly
discouraged.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%if %{without bootstrap}
# Omitted during bootstrap.
%{gpgverify} --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}
pushd %{_sourcedir}
sha256sum -c %{SOURCE3}
popd
%endif

%autosetup -p 1

# Regen Autotools.
autoreconf -fiv -Wall,error

%if %{with new_api}
cat << EOF >> README%{distname}
This version of the %{name} package ships the libcrypt.so.2
library and does not provide the legacy API functions that have
been provided by glibc's libcrypt.so.1.  The removed functions
by name are encrypt, encrypt_r, setkey, setkey_r, and fcrypt.
%if %{with compat_pkg}

If you are using a third-party application that links against
those functions, or that is linked against glibc's libcrypt,
you may need to install the %{name}-compat package manually.

All existing binary executables linked against glibc's libcrypt
should work unmodified with the libcrypt.so.1 library supplied
by the %{name}-compat package.
%endif
EOF
%endif

%if %{with enosys_stubs}
cat << EOF >> README.posix
This version of the libcrypt.so.1 library has entirely removed
the functionality of the encrypt, encrypt_r, setkey, and setkey_r
functions, while keeping fully binary compatibility with existing
(third-party) applications possibly still using those funtions.
If such an application attemps to call one of these functions, the
corresponding function will indicate that it is not supported by
the system in a POSIX-compliant way.

For security reasons, the encrypt and encrypt_r functions will
also overwrite their data-block argument with random bits.

All existing binary executables linked against glibc's libcrypt
should work unmodified with the provided version of the
libcrypt.so.1 library in place.
EOF
%endif

%if %{with staticlib}
cat << EOF >> README.static
Applications that use certain legacy APIs supplied by glibc’s
libcrypt (encrypt, encrypt_r, setkey, setkey_r, and fcrypt)
cannot be compiled nor linked against the supplied build of
the object files provided in the static library libcrypt.a.
EOF
%endif

%build

touch %{config_cache}
mkdir -p %{_vpath_builddir}
pushd %{_vpath_builddir}
%configure                                       \
  %{common_configure_options}                    \
  --enable-hashes=%{hash_methods}                \
  --enable-obsolete-api=%{obsolete_api}          \
%if %{with new_api}
  --enable-obsolete-api-enosys=%{obsolete_api}
%else
  --enable-obsolete-api-enosys=%{enosys_stubs}
%endif
%make_build
popd
%if %{with compat_pkg}
mkdir -p %{_vpath_builddir}-compat
pushd %{_vpath_builddir}-compat
%configure                                       \
  %{common_configure_options}                    \
  --enable-hashes=%{compat_methods}              \
  --enable-obsolete-api=%{compat_api}            \
  --enable-obsolete-api-enosys=%{enosys_stubs}
%make_build
popd
%endif
rm -f %{config_cache}
%install
%if %{with compat_pkg}
%make_install -C %{_vpath_builddir}-compat
find %{buildroot}                                               \
  -not -type d -not -name 'libcrypt.so.%{csoc}*' -delete -print
%endif
%make_install -C %{_vpath_builddir}
find %{buildroot} -name '*.la' -delete -print
install -Dpm 0644 -t %{buildroot}%{_pkgdocdir} \
  ChangeLog NEWS README* THANKS TODO
rm -f %{buildroot}%{_pkgdocdir}/README.md
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

build_dirs="%{_vpath_builddir}"
%if %{with compat_pkg}
build_dirs="${build_dirs} %{_vpath_builddir}-compat"
%endif
for dir in ${build_dirs}; do
  %make_build -C ${dir} check || \
    {
      rc=$?;
      echo "-----BEGIN TESTLOG: ${dir}-----";
      cat ${dir}/test-suite.log;
      echo "-----END TESTLOG: ${dir}-----";
      exit $rc;
    }
done
%ldconfig_scriptlets
%if %{with compat_pkg}
%ldconfig_scriptlets compat
%endif
%files -f %{oreon_filedir}/main.list
%files -n libxcrypt-compat -f %{oreon_filedir}/libxcrypt-compat.list
%files -n libxcrypt-devel -f %{oreon_filedir}/libxcrypt-devel.list
%files -n libxcrypt-static -f %{oreon_filedir}/libxcrypt-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.5.2-3
- Prepare for Oreon 11 (RP1)
