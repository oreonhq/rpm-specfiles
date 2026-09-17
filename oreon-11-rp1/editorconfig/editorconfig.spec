%global source0_hash ab9f897a90fb36cfc34e5b67221e55ab0e3119b3512de8e31029d376c6bab870

# do not require a standalone uthash when built as part of RHEL
%bcond system_uthash %[0%{?fedora} || 0%{?epel}]

# build process has race conditions, force single thread
%global _smp_mflags -j1

%global srcname editorconfig-core-c

%global common_description %{expand:
EditorConfig makes it easy to maintain the correct coding style when
switching between different text editors and between different projects.
The EditorConfig project maintains a file format and plugins for various
text editors which allow this file format to be read and used by those
editors.}

Name:           editorconfig
Summary:        Parser for EditorConfig files written in C
Version:        0.12.10
Release:        1%{?dist}

# The entire source is BSD-2-Clause, except:
#   BSD-3-Clause: src/lib/ini.h
#                 src/lib/ini.c
#   BSD-1-Clause: src/lib/utarray.h
# Additionally, the following build-system files do not contribute to the
# licenses of the binary RPMs:
#   MIT: CMake_Modules/FindPCRE2.cmake
# The file src/lib/utarray.h is unbundled in %%prep, as part of the uthash
# header-only library; however, since packaging guidelines treat header-only
# libraries as a kind of static library, and the entire contents are still
# compiled into the binary RPMs, its license still contributes to the overall
# license of the binary RPMs.
License:        BSD-2-Clause AND BSD-3-Clause AND BSD-1-Clause
URL:            https://github.com/editorconfig/editorconfig-core-c
Source0:        https://github.com/editorconfig/editorconfig-core-c/archive/refs/tags/v0.12.10.tar.gz#/editorconfig-core-c-0.12.10.tar.gz

# Downstream-only: Do not compile with -Werror
#
# This makes sense upstream, but is too strict for downstream packaging
# across various architectures, compiler versions, and so on.
Patch0:         0001-Downstream-only-Do-not-compile-with-Werror.patch

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  pcre2-devel
%if %{with system_uthash}
# Header-only library; BR on -static required by guidelines
BuildRequires:  uthash-static
%endif

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description %common_description


%package        libs
Summary:        Parser library for EditorConfig files (shared library)

# Files src/lib/ini.h and src/lib/ini.c are a forked copy of inih:
#   https://src.fedoraproject.org/rpms/inih
#   https://github.com/benhoyt/inih
# Since it has different hard-coded limits, among other changes from upstream,
# we expect that it will not be possible to unbundle it. Still, we have
# contacted upstream as required in
#   https://docs.fedoraproject.org/en-US/packaging-guidelines/#bundling
# via a GitHub issue:
#   Path to using a system copy of inih?
#   https://github.com/editorconfig/editorconfig-core-c/issues/91
# Upstream agreed that the bundled version has diverged too much.
#
# The files were added in commit 24cc68431848c6d53a877ff82a4ee4ce7ff67b7f on
# 2011-10-23; their contents at that time were an exact match for the
# then-latest commit in inih, 328c3d4f8ac3715fc7024af09372a479f028450f in
# today’s git repository. Since inih did not carry a version number, and the
# Google Code SVN hash at the time is lost to history, we use the git hash in
# the current repository to indicate the snapshot from which the bundled
# version was forked.
Provides:       bundled(inih) = 0^20110627git328c3d4
%if %{without system_uthash}
# src/lib/utarray.h:UTARRAY_VERSION
Provides:       bundled(uthash) = 2.3.0
%endif

%description    libs %common_description

This package contains the shared library.


%package        devel
Summary:        Parser library for EditorConfig files (development files)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake

%description    devel %common_description

This package contains the files needed for development.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{srcname}-%{version} -p1
%if %{with system_uthash}
# Unbundle uthash
rm -vf src/lib/utarray.h
%endif


%build
%cmake
%cmake_build


%install
%cmake_install

# Remove static library
rm %{buildroot}/%{_libdir}/libeditorconfig_static.a


%files
%doc README.md
%license LICENSE

%{_bindir}/editorconfig
%{_bindir}/editorconfig-%{version}

%{_mandir}/man1/editorconfig.1*

%files libs
%doc README.md
%license LICENSE

%{_libdir}/libeditorconfig.so.0*

%{_mandir}/man3/editorconfig*
%{_mandir}/man5/editorconfig*

%files devel
%{_includedir}/editorconfig/

%{_libdir}/libeditorconfig.so
%{_libdir}/cmake/EditorConfig/
%{_libdir}/pkgconfig/editorconfig.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.12.10-1
- Prepare for Oreon 11 (RP1)
