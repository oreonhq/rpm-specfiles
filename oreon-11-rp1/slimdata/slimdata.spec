%global source0_hash 9c73f5c7d46d10395fbd54585d0070dfec639f92d9dd3dc8f27d4315bd97f068

Name:           slimdata
Version:        2.7.1
Release:        14%{?dist}
Summary:        Tools and library for reading and writing slim compressed data

License:        GPL-3.0-or-later
URL:            http://slimdata.sourceforge.net/
Source0:        http://dl.sf.net/sourceforge/%{name}/slim_v2_7_1.tgz

Patch0:         slimdata-name-change.diff

BuildRequires: make
BuildRequires:     gcc-c++
#BuildRequires:     python3-numpy
BuildRequires:     texlive-latex doxygen texlive-metafont texlive-mfware texlive-geometry

#The current slim algorithm assumes little-endian.  Upstream is (slowly) working on this.
ExcludeArch: ppc64 ppc sparcv9 sparc64

%description
Slim is a data compression system for scientific data sets, both a binary and a
library with C linkage. Slim works with integer data from one or more channels
in a file, which it can compress more rapidly than general tools like gzip.

%package devel
Summary: Headers required when building programs against getdata
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Headers required when building projects that use the slimdata library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n slim_v2_7_1
#%patch0 -p1

#Remove included 64-bit biniary
rm -f test/generate_random_data

%build
CPPFLAGS="$RPM_OPT_FLAGS $CPPFLAGS -std=c++98"
export CPPFLAGS

%configure
make %{?_smp_mflags}
make doc

#Rebuild above binary.
#pushd test
#make
#popd

#%check
#make test

%install
mkdir -p %{buildroot}
make DESTDIR=%{buildroot} SUID_ROOT="" install

#delete static lib
rm -f %{buildroot}/%{_libdir}/libslim.a
chmod a+x %{buildroot}/%{_libdir}/libslim.so.0.0

#Rename binary to slimdata; upstream will follow in subsequent releases.
mv %{buildroot}/%{_bindir}/slim %{buildroot}/%{_bindir}/slimdata
rm %{buildroot}/%{_bindir}/unslim %{buildroot}/%{_bindir}/slimcat
#Don't forget the man page: BZ 506141
mv %{buildroot}/%{_mandir}/man1/slim.1 %{buildroot}/%{_mandir}/man1/slimdata.1
pushd .
cd %{buildroot}/%{_bindir}
ln -s slimdata unslim
ln -s slimdata slimcat
popd

%ldconfig_scriptlets

%files
%license COPYING
%doc README AUTHORS TODO VERSIONS
%{_bindir}/*slim*
%{_libdir}/libslim.so.0*
%{_mandir}/man1/*slim*

%files devel
%doc doc/slim_format.pdf doc/html/*
%{_includedir}/version.h
%{_includedir}/slim*.h
%{_libdir}/libslim.so

%changelog
%autochangelog
