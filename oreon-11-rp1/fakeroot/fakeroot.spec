%global source0_hash 86b0b75bf319ca42e525c098675b6ed10a06b76e69ec9ccf20ef5e03883b3a14

%global build_type_safety_c 0

%bcond_without autoconf

Summary: Gives a fake root environment
Name: fakeroot
Version: 1.37.1.1
Release: 1%{?dist}
# setenv.c: LGPLv2+
# contrib/Fakeroot-Stat-1.8.8: Perl (GPL+ or Artistic)
# the rest: GPLv3+
# Automatically converted from old format: GPLv3+ and LGPLv2+ and (GPL+ or Artistic) - review is highly recommended.
License: GPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
# Source code: https://salsa.debian.org/clint/fakeroot/-/tree/upstream
URL: https://tracker.debian.org/pkg/fakeroot
Source0: https://deb.debian.org/debian/pool/main/f/fakeroot/%{name}_%{version}.orig.tar.gz

# Debian package patches, from debian.tar.xz
Patch2: debian_fix-shell-in-fakeroot.patch
# git commit 8ce7846 2013-07-26  Address some POSIX-types related problems.
# Patch4: fakeroot-inttypes.patch
# Fix LD_LIBRARY_PATH for multilib: https://bugzilla.redhat.com/show_bug.cgi?id=1241527
Patch5: fakeroot-multilib.patch
# Patch7: relax_tartest.patch


BuildRequires: make
%if %{with autoconf}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  po4a
%endif
BuildRequires: /usr/bin/getopt
BuildRequires: gcc
# https://bugzilla.redhat.com/show_bug.cgi?id=887001
BuildRequires: libacl-devel
BuildRequires: libcap-devel
# uudecode used by tests/tartest
BuildRequires: sharutils
Requires: /usr/bin/getopt
Requires: fakeroot-libs = %{version}-%{release}
Requires(post): /usr/sbin/alternatives
Requires(post): /usr/bin/readlink
Requires(preun): /usr/sbin/alternatives


%description
fakeroot runs a command in an environment wherein it appears to have
root privileges for file manipulation. fakeroot works by replacing the
file manipulation library functions (chmod(2), stat(2) etc.) by ones
that simulate the effect the real library functions would have had,
had the user really been root.

%package libs
Summary: Gives a fake root environment (libraries)

%description libs
This package contains the libraries required by %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's#AC_PREREQ(\[2.71\])#AC_PREREQ([2.69])#' configure.ac
# this test fails on s390x, i don't know or care why
%ifarch s390x
sed -i -e '/^ *t\.tar/d' test/Makefile.am
%endif

%build
%if %{with autoconf}
./bootstrap
pushd doc
po4a -k 0 --rm-backups --variable "srcdir=../doc/" po4a/po4a.cfg
popd
%endif

for file in ./doc/{*.1,*/*.1}; do
  iconv -f latin1 -t utf8 < $file > $file.new && \
  mv -f $file.new $file
done

for type in sysv tcp; do
mkdir obj-$type
cd obj-$type
cat >> configure << 'EOF'
#!/bin/sh
exec ../configure "$@"
EOF
chmod +x configure
%configure \
  --disable-dependency-tracking \
  --disable-static \
  --libdir=%{_libdir}/libfakeroot \
  --with-ipc=$type \
  --program-suffix=-$type
make
cd ..
done

%install
for type in sysv tcp; do
  make -C obj-$type install libdir=%{_libdir}/libfakeroot DESTDIR=%{buildroot}
  mv %{buildroot}%{_libdir}/libfakeroot/libfakeroot-0.so \
     %{buildroot}%{_libdir}/libfakeroot/libfakeroot-$type.so
  rm -f %{buildroot}%{_libdir}/libfakeroot/libfakeroot.so
  rm -f %{buildroot}%{_libdir}/libfakeroot/libfakeroot.*la
  %find_lang faked-$type --without-mo --with-man
  %find_lang fakeroot-$type --without-mo --with-man
done

rm %{buildroot}%{_mandir}{,/*}/man1/fake{d,root}-sysv.1
rename -- -tcp '' %{buildroot}%{_mandir}{,/*}/man1/fake{d,root}-tcp.1
sed -e 's/-tcp//g' fake{d,root}-tcp.lang > fakeroot.lang

%check
for type in sysv tcp; do
%ifarch ppc64le
%if 0%{?rhel}
  make -C obj-$type check VERBOSE=1 || :
%else
  make -C obj-$type check VERBOSE=1
%endif
%else
  make -C obj-$type check VERBOSE=1
%endif
done

%post
link=$(readlink -e "/usr/bin/fakeroot")
if [ "$link" = "/usr/bin/fakeroot" ]; then
  rm -f /usr/bin/fakeroot
fi
link=$(readlink -e "%{_bindir}/faked")
if [ "$link" = "%{_bindir}/faked" ]; then
  rm -f "%{_bindir}/faked"
fi
link=$(readlink -e "%{_libdir}/libfakeroot/libfakeroot-0.so")
if [ "$link" = "%{_libdir}/libfakeroot/libfakeroot-0.so" ]; then
  rm -f "%{_libdir}/libfakeroot/libfakeroot-0.so"
fi

alternatives --install "%{_bindir}/fakeroot" fakeroot \
  "%{_bindir}/fakeroot-tcp" 50 \
  --follower %{_bindir}/faked faked %{_bindir}/faked-tcp \
  --follower %{_libdir}/libfakeroot/libfakeroot-0.so libfakeroot.so %{_libdir}/libfakeroot/libfakeroot-tcp.so

alternatives --install "%{_bindir}/fakeroot" fakeroot \
  "%{_bindir}/fakeroot-sysv" 40 \
  --follower %{_bindir}/faked faked %{_bindir}/faked-sysv \
  --follower %{_libdir}/libfakeroot/libfakeroot-0.so libfakeroot.so %{_libdir}/libfakeroot/libfakeroot-sysv.so || :

%preun
if [ $1 = 0 ]; then
  alternatives --remove fakeroot "%{_bindir}/fakeroot-tcp"
  alternatives --remove fakeroot "%{_bindir}/fakeroot-sysv" || :
fi

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING AUTHORS BUGS DEBUG doc/README.saving
%{_bindir}/faked-*
%ghost %{_bindir}/faked
%{_bindir}/fakeroot-*
%ghost %{_bindir}/fakeroot
%{_mandir}/man1/faked.1*
%{_mandir}/man1/fakeroot.1*

%files libs
%dir %{_libdir}/libfakeroot
%{_libdir}/libfakeroot/libfakeroot-sysv.so
%{_libdir}/libfakeroot/libfakeroot-tcp.so
%ghost %{_libdir}/libfakeroot/libfakeroot-0.so

%changelog
%autochangelog
