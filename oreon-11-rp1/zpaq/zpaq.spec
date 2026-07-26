%global source0_hash e85ec2529eb0ba22ceaeabd461e55357ef099b80f61c14f377b429ea3d49d418

# JIT is supported on x86 and x86_64 only, bug #1309772
%ifarch %{ix86} x86_64
%bcond_without jit
%else
%bcond_with jit
%endif

Name:           zpaq
Version:        7.15
Release:        25%{?dist}
Summary:        Incremental journaling back-up archiver
# COPYING:      Unlicense text AND MIT text
# Parts of libzpaq.cpp: LicenseRef-Fedora-Public-Domain
#               <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/306>
## In zpaq-libs package
# libzpaq.cpp:  Unlicense AND MIT AND LicenseRef-Fedora-Public-Domain
License:        Unlicense AND LicenseRef-Fedora-Public-Domain
URL:            http://mattmahoney.net/dc/%{name}.html
Source0:        http://mattmahoney.net/dc/%{name}%(echo %{version}|tr -d .).zip
# Do not bundle zpaq library into zpaq tool, upstream does not want it
# <http://encode.ru/threads/456-zpaq-updates?s=8510051f0caeb4c019c6d0af1dd6f585&p=47379&viewfull=1#post47379>
Patch0:         zpaq-7.15-Build-a-shared-library.patch
BuildRequires:  coreutils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-podlators
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
This is a journaling archiver optimized for user-level incremental backup of
directory trees. It supports AES-256 encryption, 5 multi-threaded compression
levels, and content-aware file fragment level deduplication. For backups it
adds only files whose date has changed, and keeps both old and new versions.
You can roll back the archive date to restore from old versions of the
archive. The default compression level is faster than zip usually with better
compression. zpaq uses a self-describing compressed format to allow for future
improvements without breaking compatibility with older versions of the
program.

%package        libs
Summary:        Library for ZPAQ compression and decompression
License:        Unlicense AND MIT AND LicenseRef-Fedora-Public-Domain
# libdivsufsort-lite-2.00 is bundled to libzpaq.cpp from
# <https://libdivsufsort.googlecode.com/files/libdivsufsort-lite.zip> that
# is simplified version of
# <http://libdivsufsort.googlecode.com/files/libdivsufsort-2.0.0.tar.bz2>.
# New libdivsufsort upstream is <https://github.com/y-256/libdivsufsort>.
Provides:       bundled(libdivsufsort-lite) = 2.00

%description    libs
This is a library for ZPAQ compression a decompression.

%package        devel
Summary:        Development files for ZPAQ library
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       gcc-c++%{?_isa}

%description    devel
These are header files for developing applications that support ZPAQ
compression.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -c -n %{name}-%{version}
# Normalize EOLs
for F in readme.txt; do
    tr -d "\r" < "${F}" > "${F}.new"
    touch -r "$F" "${F}.new"
    mv "${F}.new" "$F"
done

%build
# -Wl,--as-needed to not require unused libm, bug #1310128
%{make_build} \
    CXXFLAGS='%{optflags}' \
    LDFLAGS='%{?__global_ldflags} -Wl,--as-needed' \
    CPPFLAGS="${CPPFLAGS} -Dunix %{!?with_jit: -DNOJIT}"

%check
make check %{?_smp_mflags}

%install
%{make_install} PREFIX=%{_prefix} LIBDIR=%{_libdir}

%ldconfig_scriptlets libs

%files
%doc readme.txt
%{_bindir}/zpaq
%{_mandir}/man1/zpaq.1*

%files libs
%license COPYING
%{_libdir}/libzpaq.so.0.1

%files devel
%{_includedir}/libzpaq.h
%{_libdir}/libzpaq.so

%changelog
%autochangelog
