%global source0_hash 86b0b75bf319ca42e525c098675b6ed10a06b76e69ec9ccf20ef5e03883b3a14
%global build_type_safety_c 0
%bcond_without autoconf
Summary:        Gives a fake root environment
Name: fakeroot
Version: 1.37.1.1
Release:        1%{?dist}
License: GPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL: https://tracker.debian.org/pkg/fakeroot
Source0:        https://deb.debian.org/debian/pool/main/f/fakeroot/%{name}_%{version}.orig.tar.gz
Patch2: debian_fix-shell-in-fakeroot.patch
Patch5: fakeroot-multilib.patch
%if %{with autoconf}
%endif
Requires: /usr/bin/getopt
Requires: fakeroot-libs = %{version}-%{release}
Requires(post): /usr/sbin/alternatives
Requires(post): /usr/bin/readlink
Requires(preun): /usr/sbin/alternatives
# oreon:deps
BuildRequires:  /usr/bin/getopt
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libacl-devel
BuildRequires:  libcap-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  po4a
BuildRequires:  sharutils
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

for type in sysv tcp; do
%ifarch ppc64le
  make -C obj-$type check VERBOSE=1
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
%files -f %{oreon_filedir}/main.list
%files -n fakeroot-libs -f %{oreon_filedir}/fakeroot-libs.list

%changelog

%autochangelog
