%global source0_hash 051b903b34bbdd98af2bc94558119f48b81bfa382a3ea8c507788f0751ddeda4
%ifarch %{ix86} x86_64
%bcond_without jit
%else
%bcond_with jit
%endif
%global toolchain gcc
%bcond_with toolchain_clang
%bcond_with toolchain_gcc
Name:           zpaqfranz
Epoch:          1
Version:        64.8
Release:        1%{?dist}
Summary:        Advanced multiversioned archiver with hardware acceleration
License:        MIT AND Apache-2.0 AND BSD-2-Clause AND Ferguson-Twofish AND (LicenseRef-Fedora-Public-Domain OR WTFPL) AND Unlicense AND Zlib AND LicenseRef-Fedora-Public-Domain
SourceLicense:  %{license} AND curl
URL:            https://github.com/fcorbelli/%{name}
Source0:        https://github.com/fcorbelli/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         zpaqfranz-64.6-Unbundle-curl.h-and-load-curl-DSO-by-a-bare-file-nam.patch
Provides:       bundled(libdivsufsort-lite) = 2.00
Provides:       bundled(lz4)
Recommends:     libcurl-full
%if 0%(/usr/lib/rpm/elfdeps --provides --soname-only %{_libdir}/libcurl.so.4 >/dev/null 2>&1 && echo 1)
Recommends:     %(/usr/lib/rpm/elfdeps --provides --soname-only %{_libdir}/libcurl.so.4)
%endif
Recommends:     libssh
%if 0%(/usr/lib/rpm/elfdeps --provides --soname-only %{_libdir}/libssh.so.4 >/dev/null 2>&1 && echo 1)
Recommends:     %(/usr/lib/rpm/elfdeps --provides --soname-only %{_libdir}/libssh.so.4)
%endif
Recommends:     (mariadb or mysql)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libssh-devel
BuildRequires:  perl-podlators
BuildRequires:  rpm-build
BuildRequires:  sed
# /oreon:deps
%description
This is a Swiss army knife for backup and disaster recovery with deduplicated
snapshots. It efficiently keeps backups, without a need to ever prune. Handles
millions of files and terabytes of data. Non-Latin support. Backups with full
encryption. Data integrity check with CRC32 and XXHASH or SHA-1, SHA-2, SHA-3,
MD5, XXH3, or BLAKE3. Multithread support. Specific ZFS handling functions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
# Remove pregenerated files
rm man/zpaqfranz.1
# Remove precompiled code
sed -i -e '/zsfx_mime64\[\]={/d' zpaqfranz.cpp
# Normalize EOLs
for F in CHANGELOG.md; do
    tr -d "\r" < "${F}" > "${F}.new"
    touch -r "$F" "${F}.new"
    mv "${F}.new" "$F"
done
# Extract license texts
sed -n -e '/^Credits and copyrights and licenses/,/^   _____ _____/ p' \
    < zpaqfranz.cpp > LICENSES

%build

%{build_cxx} %{optflags} \
    -DIPV6 \
    -Dunix \
%if %{without jit}
    -DNOJIT \
%endif
%ifarch x86_64
    -DHWSHA2 \
%endif
%ifarch s390x
    -DBIG \
%endif
    -DSFTP \
    zpaqfranz.cpp %{?__global_ldflags} -ldl -pthread -o zpaqfranz
pod2man --utf8 man/zpaqfranz.pod man/zpaqfranz.1
%check

./zpaqfranz autotest
./zpaqfranz a test.zpaq LICENSE
./zpaqfranz v test.zpaq
%install
install -m 0755 -D -t %{buildroot}%{_bindir} zpaqfranz
install -m 0644 -D -t %{buildroot}%{_mandir}/man1 man/zpaqfranz.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
