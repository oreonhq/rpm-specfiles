%global source0_hash 17f8a7a88758f5fe67c3e2f304f549b1543c3abfadf1d01053b280369238005f

%global _hardened_build 1

Name:		ebtree
Version:	6.0.8
Release:	27%{?dist}
Summary:	Elastic binary tree library

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2
URL:		http://1wt.eu/articles/ebtree/
Source0:	http://1wt.eu/tools/%{name}/%{name}-%{version}.tar.gz

# Build shared libraries. Upstream is asked for this in private mail.
# No mailing list nor bug tracker available
Patch1:		ebtree-6.0.8.build_shared_libs.patch

# There is no real test, just some binaries to run. So add a script to run them
Patch2:		ebtree-6.0.8.add_test_script.patch

BuildRequires:	make
BuildRequires:	coreutils
BuildRequires:	gcc
BuildRequires:	util-linux

# For epel5 support

%description
ebtree is a binary search tree specially optimized to very
frequently store, retrieve and delete discrete integer or binary
data without having to deal with memory allocation.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
# Automatically converted from old format: LGPLv2 and GPLv2+ - review is highly recommended.
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

# Some hardening on epel5,6
%if 0%{?rhel} == 5 || 0%{?rhel} == 6
export CFLAGS="%{optflags} -fPIC -DPIC -fPIE"
export LDFLAGS="%{?__global_ldflags} -Wl,-z,relro -z,now"
%endif
make %{?_smp_mflags} PREFIX=%{_prefix}
make test
head -245 ebtree.h > README

%check
bash tests.sh

%install
# For el5,6,7 support
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pkgconfig

%{make_install} PREFIX=%{_prefix}

%files
%doc VERSION README
%{_libdir}/*.so.*
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 7
%license LICENSE
%else
%doc LICENSE
%endif

%files devel
%doc VERSION README examples
%{_includedir}/%{name}/*.h
%{_datadir}/pkgconfig/%{name}.pc
%{_libdir}/*.so
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 7
%license LICENSE
%else
%doc LICENSE
%endif

%ldconfig_scriptlets

%changelog
%autochangelog
