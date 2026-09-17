%global source0_hash 0128f19c3419fbd84f7e6d46b13a33ef7bda9b9f5e493bc5ae1882d087514b71

Name:           libnetfilter_acct
Version:        1.0.2
Release:        27%{?dist}
Summary:        A library providing interface to extended accounting infrastructure

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.netfilter.org/projects/libnetfilter_acct/index.html
Source0:        http://www.netfilter.org/projects/libnetfilter_acct/files/libnetfilter_acct-1.0.2.tar.bz2

BuildRequires:  gcc
BuildRequires:  libmnl-devel
BuildRequires: make

%description
libnetfilter_acct is the userspace library providing interface to extended
accounting infrastructure.

libnetfilter_acct is used by nfacct.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find examples '(' -name Makefile.in -o -name Makefile.am ')' -exec rm -f {} ';'
mv examples examples-%{_arch}

%ldconfig_scriptlets

%files
%doc COPYING README
%{_libdir}/*.so.*

%files devel
%doc COPYING
%doc examples-%{_arch}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
