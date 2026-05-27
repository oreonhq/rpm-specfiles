%global source0_hash 4edf9989499e8bc95085c9f7108ed41d69546c34c6eea81da0fa22d95043bf72

# Currently fails on s390x and ARMv7
%if ! 0%{?_module_build}
%global with_tests 0
%else
%global with_tests 0
%endif

Name:          xapian-core
Version:       1.4.30
Release:       2%{?dist}
Summary:       The Xapian Probabilistic Information Retrieval Library
License:       GPL-2.0-or-later
URL:           https://www.xapian.org/
Source0:       https://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libuuid-devel
BuildRequires: make
BuildRequires: zlib-devel
%if 0%{?with_tests}
BuildRequires: valgrind-devel
%endif
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}


%description
Xapian is an Open Source Probabilistic Information Retrieval Library. It
offers a highly adaptable toolkit that allows developers to easily add advanced
indexing and search facilities to applications

%package libs
Summary:       Xapian search engine libraries

%description libs
Xapian is an Open Source Probabilistic Information Retrieval framework. It
offers a highly adaptable toolkit that allows developers to easily add advanced
indexing and search facilities to applications. This package provides the
libraries for applications using Xapian functionality

%package devel
Summary:       Files needed for building packages which use Xapian
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
Requires:      libuuid-devel

%description devel
Xapian is an Open Source Probabilistic Information Retrieval framework. It
offers a highly adaptable toolkit that allows developers to easily add advanced
indexing and search facilities to applications. This package provides the
files needed for building packages which use Xapian

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
%configure

%{make_build}

%install
%{make_install}

# Remove libtool archives
find $RPM_BUILD_ROOT -name '*.la' -delete

# Remove the dev docs, we pick them up below
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%if 0%{?with_tests}
%check
make check %{?_smp_mflags}
%endif

%ldconfig_scriptlets libs

%files
%doc AUTHORS NEWS README
%{_bindir}/xapian*
%{_bindir}/quest
%{_bindir}/copydatabase
%{_bindir}/simpleindex
%{_bindir}/simplesearch
%{_bindir}/simpleexpand
%{_datadir}/xapian-core/
%{_mandir}/man1/xapian*
%{_mandir}/man1/quest.1*
%{_mandir}/man1/copydatabase.1*

%files libs
%license COPYING
%{_libdir}/libxapian.so.*

%files devel
%doc HACKING PLATFORMS docs/*html docs/apidoc
%{_bindir}/xapian-config
%{_includedir}/xapian
%{_includedir}/xapian.h
%{_libdir}/libxapian.so
%{_libdir}/cmake/xapian
%{_libdir}/pkgconfig/xapian-core.pc
%{_datadir}/aclocal/xapian.m4
%{_mandir}/man1/xapian-config.1*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.30-2
- Import
