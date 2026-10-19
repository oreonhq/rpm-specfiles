%global source0_hash 17f8a7a88758f5fe67c3e2f304f549b1543c3abfadf1d01053b280369238005f
%global _hardened_build 1
Name:		ebtree
Version:	6.0.8
Release:        1%{?dist}
Summary:        Elastic binary tree library
License:	LicenseRef-Callaway-LGPLv2
URL:		http://1wt.eu/articles/ebtree/
Source0:        http://1wt.eu/tools/%{name}/%{name}-%{version}.tar.gz
Patch1:		ebtree-6.0.8.build_shared_libs.patch
Patch2:		ebtree-6.0.8.add_test_script.patch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  util-linux
# /oreon:deps
%description
ebtree is a binary search tree specially optimized to very
frequently store, retrieve and delete discrete integer or binary
data without having to deal with memory allocation.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
License:	LicenseRef-Callaway-LGPLv2 AND GPL-2.0-or-later
%description devel
Development files for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 
%patch -P2

%build

export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
make %{?_smp_mflags} PREFIX=%{_prefix}
make test
head -245 ebtree.h > README
%check

bash tests.sh
%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pkgconfig
%{make_install} PREFIX=%{_prefix}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ebtree-devel -f %{oreon_filedir}/ebtree-devel.list

%changelog

%autochangelog
