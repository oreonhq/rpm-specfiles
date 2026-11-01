%global source0_hash aae608dfe8213dfd05d909a57718ef82f30722c392344583d3f39050c7f29a80
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: xxhash
Version: 0.8.3
Release: 1%{?dist}
Summary: Extremely fast hash algorithm
License: BSD-2-Clause AND GPL-2.0-or-later
URL: https://www.xxhash.com/
Source0: https://github.com/Cyan4973/xxHash/archive/refs/tags/v%{version}.tar.gz

Provides: xxhash-libs = %{version}-%{release}
Provides: xxhash-devel = %{version}-%{release}

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: make
%endif

%description
xxHash is a fast non-cryptographic hash. This package ships the library, headers, and xxhsum.

%prep
%oreon_sha256
%autosetup -n xxHash-%{version} -p1

%build
%ifarch x86_64
%global dispatch 1
%else
%global dispatch 0
%endif
%oreon_make MOREFLAGS="%{_oreon_cflags} %{_oreon_ldflags}" DISPATCH=%{dispatch} LIBXXH_DISPATCH=%{dispatch}

%install
%oreon_make_install PREFIX=%{_prefix} LIBDIR=%{_libdir} DISPATCH=%{dispatch} LIBXXH_DISPATCH=%{dispatch}
rm -f %{buildroot}%{_libdir}/libxxhash.a
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license LICENSE cli/COPYING
