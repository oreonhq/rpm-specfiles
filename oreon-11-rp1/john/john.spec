%global source0_hash 0b266adcfef8c11eed690187e71494baea539efbd632fe221181063ba09508df

Name:           john
Summary:        John the Ripper password cracker
Version:        1.9.0
Release:        12%{?dist}

%bcond_without  check

URL:            https://www.openwall.com/john
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
Source0:        https://www.openwall.com/john/k/john-%{version}.tar.xz
Source1:        https://www.openwall.com/john/k/john-%{version}.tar.xz.sign

# The authenticator public key obtained from https://www.openwall.com/signatures/
# https://www.openwall.com/signatures/openwall-offline-signatures.asc
# gpg --keyid-format long --list-options show-keyring  openwall-offline-signatures.asc
# it's ID 05C027FD4BDC136E resp. 297AD21CF86C948081520C1805C027FD4BDC136E
# uid "Openwall offline signing key"
#
# Compared to public records of pgp.mit.edu
# gpg2 --keyserver pgp.mit.edu --search-key 297AD21CF86C948081520C1805C027FD4BDC136E
# gpg2 --list-public-keys 297AD21CF86C948081520C1805C027FD4BDC136E
#
# Verified manually signature on tarball
# gpg --verify john-1.9.0.tar.xz.sign john-1.9.0.tar.xz
# OK
#
# gpg2 -vv john-1.9.0.tar.xz.sign
# Signed by 05C027FD4BDC136E which belongs to "Openwall offline signing key"
# gpg2 --export --export-options export-minimal 297AD21CF86C948081520C1805C027FD4BDC136E > gpgkey-297AD21CF86C948081520C1805C027FD4BDC136E.gpg
Source2:        gpgkey-297AD21CF86C948081520C1805C027FD4BDC136E.gpg

# Align the naming of the fallback binaries with jumbo patch + kali
# https://github.com/openwall/john/issues/5233

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gnupg2
BuildRequires:  libxcrypt-devel

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

# WARNING - john makefile is defining -c on the level of CFLAGS and not the compile lines
# when overriding the Makefile we need to keep this logic
ORIGCPU=$(echo "$CFLAGS" | grep -o -E -e '-m(sse2|avx|avx2|avx512|avx512f|xop)( |$)' | tr -d '\n' )
CFLAGS=$(echo "$CFLAGS" | sed -E 's/-m(sse2|avx|avx2|avx512|avx512f|xop)( |$)//;' )
export CFLAGS="$CFLAGS -c -DJOHN_SYSTEMWIDE=1"

# ASFLAGS needs info about libraries same as LDFLAGS, but needs -c for compilation only
export ASFLAGS="-c $LDFLAGS"

# By default build with "make generic"
ARCH_CHAIN="generic"
%global with_fallback 0

# By default quote fallback binary name with just "
Q='"'
%ifarch %{ix86} || x86_64
# on intel quote with '\"' ... do not ask me why
Q='\"'
%endif

# i686 settings
%ifarch %{ix86}
# Fedora current settings starts on sse2 so it is not necessary going bellow that
# ARCH_CHAIN="linux-x86-any linux-x86-mmx linux-x86-sse2 linux-x86-avx linux-x86-xop linux-x86-avx2"
ARCH_CHAIN="linux-x86-any linux-x86-sse2 linux-x86-avx linux-x86-xop linux-x86-avx2"
%if (0%{?fedora}) || ( 0%{?rhel} >= 8 )
ARCH_CHAIN="$ARCH_CHAIN linux-x86-avx512"
%endif
%global with_fallback 1
%endif

%ifarch x86_64
ARCH_CHAIN="linux-x86-64 linux-x86-64-avx linux-x86-64-xop linux-x86-64-avx2"
%if (0%{?fedora}) || ( 0%{?rhel} >= 8 )
ARCH_CHAIN="$ARCH_CHAIN linux-x86-64-avx512"
%endif
%global with_fallback 1
%endif

%ifarch ppc
ARCH_CHAIN="linux-ppc32 linux-ppc32-altivec"
%endif

%ifarch ppc64
ARCH_CHAIN="linux-ppc64 linux-ppc64-altivec"
%endif

# Compile the fallback binary
ARCH_FIRST=$( echo "${ARCH_CHAIN}" | cut -d ' ' -f 1 )

# WARNING: original LDFLAGS in Makefile contain -s to strip the binaries
# We need to override that
make -C src "${ARCH_FIRST}" CFLAGS="${CFLAGS}" LDFLAGS="${LDFLAGS}" ASFLAGS="${ASFLAGS}"
mv run/john "run/john-${ARCH_FIRST}-non-omp"

# Compile whole chain of binaries, if configured
set $ARCH_CHAIN
while true ; do
    if [ -z $2 ] ; then
        break
    fi
    PREV="$1"
    TARGET="$2"
    # Fallback binary definition is used in #define as a string, pre-procesor seamlessly joins the strings together without using string functions like:
    # gcc -DCPU_FALLBACK_BINARY='"john-linux-x86-64-xop"' ...
    # #define OMP_FALLBACK_PATHNAME JOHN_SYSTEMWIDE_EXEC "/" OMP_FALLBACK_BINARY
    # needs to be double quoted here as one layer is stripped by shell and one by make
    CPU_FALLBACK="${Q}john-${PREV}-non-omp${Q}"
    make -C src clean
    make -C src "${TARGET}" CFLAGS="${CFLAGS} -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='${CPU_FALLBACK}'" LDFLAGS="${LDFLAGS}" ASFLAGS="${ASFLAGS}"
    mv run/john "run/john-${TARGET}-non-omp"
    shift
done

# Compile the OMP binary with fallback to CPU binary
make -C src clean
ARCH_FIRST=$( echo "${ARCH_CHAIN}" | cut -d ' ' -f 1 )
OMP_FALLBACK="${Q}john-${ARCH_FIRST}${Q}"
make -C src "${ARCH_FIRST}" CFLAGS="${CFLAGS} -fopenmp -DOMP_FALLBACK=1 -DOMP_FALLBACK_BINARY='${OMP_FALLBACK}'" OMPFLAGS=-fopenmp LDFLAGS="${LDFLAGS} -fopenmp" ASFLAGS="${ASFLAGS} -fopenmp"
mv run/john "run/john-${ARCH_FIRST}-omp"

# Compile whole chain of OMP binaries
set $ARCH_CHAIN
while true ; do
    if [ -z $2 ] ; then
        break
    fi
    PREV="$1"
    TARGET="$2"
    # fallback to previous CPU optimization, if OMP is present
    CPU_FALLBACK="${Q}john-${PREV}-omp${Q}"
    # fallback to same CPU optimization, if OMP is broken
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

%files
%doc doc/*
%config(noreplace) %{_sysconfdir}/john.conf
%{_bindir}/john
%{_bindir}/mailer
%{_bindir}/unafs
%{_bindir}/unique
%{_bindir}/unshadow
%{_datadir}/john/
%{_libexecdir}/john/

%changelog
%autochangelog
