%global source1_hash 9ca688129da714713d5c8b125d86e7a04232d07b336a62e83b7fba90716b9c88
%global source0_hash 0b266adcfef8c11eed690187e71494baea539efbd632fe221181063ba09508df
Name:           john
Summary:        John the Ripper password cracker
Version:        1.9.0
Release:        1%{?dist}
%bcond_without  check
URL:            https://www.openwall.com/john
License:        GPL-2.0-only
Source0:        https://www.openwall.com/john/k/john-%{version}.tar.xz
Source1:        https://www.openwall.com/john/k/john-%{version}.tar.xz.sign
Source2:        gpgkey-297AD21CF86C948081520C1805C027FD4BDC136E.gpg
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libxcrypt-devel
BuildRequires:  make
# /oreon:deps
%description
John the Ripper is a fast password cracker (password security auditing
tool). Its primary purpose is to detect weak Unix passwords, but a number
of other hash types are supported as well.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#check signature
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p 1

chmod 0644 doc/*
sed -i 's#\$JOHN/john.conf#%{_sysconfdir}/john.conf#' src/params.h

# Extra charsets - not needed anymore, part of 1.9.0 core release
# tar --strip-components 1 --directory run -xf "%%{SOURCE2}"

%build

%set_build_flags
ORIGCPU=$(echo "$CFLAGS" | grep -o -E -e '-m(sse2|avx|avx2|avx512|avx512f|xop)( |$)' | tr -d '\n' )
CFLAGS=$(echo "$CFLAGS" | sed -E 's/-m(sse2|avx|avx2|avx512|avx512f|xop)( |$)//;' )
export CFLAGS="$CFLAGS -c -DJOHN_SYSTEMWIDE=1"
export ASFLAGS="-c $LDFLAGS"
ARCH_CHAIN="generic"
%global with_fallback 0
Q='"'
%ifarch %{ix86} || x86_64
Q='\"'
%endif
%ifarch %{ix86}
ARCH_CHAIN="linux-x86-any linux-x86-sse2 linux-x86-avx linux-x86-xop linux-x86-avx2"
%global with_fallback 1
%endif
%ifarch x86_64
ARCH_CHAIN="linux-x86-64 linux-x86-64-avx linux-x86-64-xop linux-x86-64-avx2"
%global with_fallback 1
%endif
%ifarch ppc
ARCH_CHAIN="linux-ppc32 linux-ppc32-altivec"
%endif
%ifarch ppc64
ARCH_CHAIN="linux-ppc64 linux-ppc64-altivec"
%endif
ARCH_FIRST=$( echo "${ARCH_CHAIN}" | cut -d ' ' -f 1 )
make -C src "${ARCH_FIRST}" CFLAGS="${CFLAGS}" LDFLAGS="${LDFLAGS}" ASFLAGS="${ASFLAGS}"
mv run/john "run/john-${ARCH_FIRST}-non-omp"
set $ARCH_CHAIN
while true ; do
    if [ -z $2 ] ; then
        break
    fi
    PREV="$1"
    TARGET="$2"
    CPU_FALLBACK="${Q}john-${PREV}-non-omp${Q}"
    make -C src clean
    make -C src "${TARGET}" CFLAGS="${CFLAGS} -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='${CPU_FALLBACK}'" LDFLAGS="${LDFLAGS}" ASFLAGS="${ASFLAGS}"
    mv run/john "run/john-${TARGET}-non-omp"
    shift
done
make -C src clean
ARCH_FIRST=$( echo "${ARCH_CHAIN}" | cut -d ' ' -f 1 )
OMP_FALLBACK="${Q}john-${ARCH_FIRST}${Q}"
make -C src "${ARCH_FIRST}" CFLAGS="${CFLAGS} -fopenmp -DOMP_FALLBACK=1 -DOMP_FALLBACK_BINARY='${OMP_FALLBACK}'" OMPFLAGS=-fopenmp LDFLAGS="${LDFLAGS} -fopenmp" ASFLAGS="${ASFLAGS} -fopenmp"
mv run/john "run/john-${ARCH_FIRST}-omp"
set $ARCH_CHAIN
while true ; do
    if [ -z $2 ] ; then
        break
    fi
    PREV="$1"
    TARGET="$2"
    CPU_FALLBACK="${Q}john-${PREV}-omp${Q}"
    OMP_FALLBACK="${Q}john-${TARGET}-non-omp${Q}"
    make -C src clean
    make -C src "${TARGET}" CFLAGS="${CFLAGS} -fopenmp -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='${CPU_FALLBACK}' -DOMP_FALLBACK=1 -DOMP_FALLBACK_BINARY='${OMP_FALLBACK}'" OMPFLAGS=-fopenmp LDFLAGS="${LDFLAGS} -fopenmp" ASFLAGS="${ASFLAGS} -fopenmp"
    mv run/john "run/john-${TARGET}-omp"
    shift
done
%install
install -d -m 755 %{buildroot}%{_sysconfdir}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/john
install -p -m 755 run/mailer %{buildroot}%{_bindir}
install -p -m 644 run/{*.chr,password.lst} %{buildroot}%{_datadir}/john
install -p -m 644 run/john.conf %{buildroot}%{_sysconfdir}
LASTJOHN=$(ls -t run/john-* | head -n 1)
LASTJOHN=$(basename "$LASTJOHN")
install -d -m 755 %{buildroot}%{_libexecdir}/john
install -p -m 755 run/john-* %{buildroot}%{_libexecdir}/john/
pushd %{buildroot}%{_bindir}
ln -s %{_libexecdir}/john/${LASTJOHN} john
ln -s john unafs
ln -s john unique
ln -s john unshadow
popd
rm doc/INSTALL
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
