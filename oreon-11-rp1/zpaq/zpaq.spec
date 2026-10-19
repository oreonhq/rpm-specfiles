%global source0_hash e85ec2529eb0ba22ceaeabd461e55357ef099b80f61c14f377b429ea3d49d418
%ifarch %{ix86} x86_64
%bcond_without jit
%else
%bcond_with jit
%endif
Name:           zpaq
Version:        7.15
Release:        1%{?dist}
Summary:        Incremental journaling back-up archiver
License:        Unlicense AND LicenseRef-Fedora-Public-Domain
URL:            http://mattmahoney.net/dc/%{name}.html
Source0:        http://mattmahoney.net/dc/%{name}715.zip
Patch0:         zpaq-7.15-Build-a-shared-library.patch
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-podlators
# /oreon:deps
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

%{make_build} \
    CXXFLAGS='%{optflags}' \
    LDFLAGS='%{?__global_ldflags} -Wl,--as-needed' \
    CPPFLAGS="${CPPFLAGS} -Dunix %{!?with_jit: -DNOJIT}"
%check

make check %{?_smp_mflags}
%install
%{make_install} PREFIX=%{_prefix} LIBDIR=%{_libdir}
%ldconfig_scriptlets libs
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n zpaq-libs -f %{oreon_filedir}/zpaq-libs.list
%files -n zpaq-devel -f %{oreon_filedir}/zpaq-devel.list

%changelog

%autochangelog
