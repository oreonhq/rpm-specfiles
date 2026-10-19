%global source0_hash 07eb52274e1c25c6ff9ab4800909c7d1a0c4b728c1b0269ee281bcb3de52f8a5
%bcond_with zlib
%global makeflags PREFIX=%{_prefix} LIBRARY_FOLDER=%{_libdir} SHARED_ROOT_FOLDER=%{_libdir} DOCUMENT_FOLDER=%{_docdir}/hashcat-doc SHARED=1 USE_SYSTEM_OPENCL=1 USE_SYSTEM_XXHASH=1 ENABLE_UNRAR=0 MAINTAINER_MODE=1
%if %{with zlib}
%global makeflags %(echo %{makeflags} USE_SYSTEM_ZLIB=1)
%else
%global makeflags %(echo %{makeflags} USE_SYSTEM_ZLIB=0)
%endif
Name: hashcat
Version: 7.1.2
Release:        1%{?dist}
License: MIT AND LicenseRef-Fedora-Public-Domain AND BSD-2-Clause AND Apache-2.0
URL: https://github.com/%{name}/%{name}
Summary:        Advanced password recovery utility
Source0:        %{name}-%{version}-clean.tar.xz
Source1: make_tarball.sh
Patch0: %{name}-build-fixes.patch
%ifarch aarch64
%endif
%if %{with zlib}
%else
Provides: bundled(zlib) = 1.2.11
Provides: bundled(minizip) = 1.2.11
%endif
Provides: bundled(lzma-sdk) = 24.09
Provides: bundled(scrypt-jane)
Provides: bundled(yescrypt)
Provides: bundled(libargon2) = 20190702
Recommends: %{name}-doc
ExcludeArch: %{ix86} ppc64 s390x ppc64le
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  minizip-compat-devel
BuildRequires:  opencl-headers
BuildRequires:  xxhash-devel
BuildRequires:  zlib-ng-compat-devel
# /oreon:deps
%description
Hashcat is the world's fastest and most advanced password recovery
utility, supporting five unique modes of attack for over 200
highly-optimized hashing algorithms. hashcat currently supports
CPUs, GPUs, and other hardware accelerators on Linux, Windows,
and Mac OS, and has facilities to help enable distributed password
cracking.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
%{summary}.

%package doc
Summary: Documentation files for %{name}
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch: noarch
%description doc
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
rm -rf deps/{OpenCL-Headers,xxHash,sse2neon}
%if %{with zlib}
rm -rf deps/zlib
%endif
sed -e 's/\.\/hashcat/hashcat/' -i *.sh
chmod -x *.sh
rm -f modules/.lock

%build

%set_build_flags
%make_build %{makeflags}
%install
%make_install %{makeflags}
ln -s lib%{name}.so.%{version} %{buildroot}%{_libdir}/lib%{name}.so
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
install -m 0744 -p extra/tab_completion/hashcat.sh %{buildroot}%{_datadir}/bash-completion/completions/%{name}
find %{buildroot}%{_libdir}/%{name}/ -name '.gitkeep' -type f -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n hashcat-devel -f %{oreon_filedir}/hashcat-devel.list
%files -n hashcat-doc -f %{oreon_filedir}/hashcat-doc.list

%changelog

%autochangelog
