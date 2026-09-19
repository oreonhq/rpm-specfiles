%global source0_hash 8683d2286d663a46412c12a0c789e755e7fd77088fb3bc0342bb71667f05a3ee

Name:		clustal-omega
Version:	1.2.4
Release:	25%{?dist}
Summary:	Clustal Omega is a command-line multiple sequence alignment tool

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.clustal.org/omega/clustal-omega-1.2.0.tar.gz
Source0:	http://www.clustal.org/omega/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	argtable-devel
BuildRequires: make

# bundled library exception provided by FPC
# https://fedorahosted.org/fpc/ticket/399
Provides:	bundled(squid) = 1.9

%description
Clustal Omega is a command-line multiple sequence alignment tool.
The tool is widely used in molecular biology for multiple alignment of
both nucleic acid and protein sequences. Clustal Omega is the latest version
in the clustal tools for the sequence alignment.

%package devel
Summary:	Development files for Clustal Omega
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development package for Clustal Omega

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i 's/\r$//' README
sed -i 's/mktemp/mkstemp/g' src/clustal-omega.c
# disable -O3 compiler flags
sed -i 's/\${AM_CFLAGS} -O3/${AM_CFLAGS}/g' configure
sed -i 's/\${AM_CXXFLAGS} -O3/${AM_CXXFLAGS}/g' configure

# fix for GCC-6 FTBFS
sed -i '/inline float log/d' src/hhalign/util-C.h

%build
export CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LDFLAGS="%{optflags}"
%configure --disable-static
make V=1 %{?_smp_mflags}

%install
%make_install
# removing libtool generated static libs
rm -f %{buildroot}%{_libdir}/libclustalo.la %{buildroot}%{_libdir}/libclustalo.a

%files
%doc COPYING README
%{_bindir}/clustalo

%files devel
%{_libdir}/pkgconfig/clustalo.pc
%{_includedir}/clustalo/

%changelog
%autochangelog
