%global source0_hash b865299ffd45d73412293369c9754b07637680e5c826915f097577cd27350348

Name:           ucl
Version:        1.03
Release:        41%{?dist}
Summary:        Portable lossless data compression library

License:        GPL-2.0-or-later
URL:            http://www.oberhumer.com/opensource/ucl/
Source0:        http://www.oberhumer.com/opensource/ucl/download/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
UCL is a portable lossless data compression library written in ANSI C.
UCL implements a number of compression algorithms that achieve an
excellent compression ratio while allowing *very* fast decompression.
Decompression requires no additional memory.

%package        devel
Summary:        UCL development files
Requires:       %{name} = %{version}-%{release}

%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
CPPFLAGS="$RPM_OPT_FLAGS $CPPFLAGS -std=c90 -fPIC"
export CPPFLAGS
%configure --disable-dependency-tracking --enable-shared --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/libucl.la

%ldconfig_scriptlets

%files
%doc COPYING NEWS README THANKS TODO
%{_libdir}/libucl.so.*

%files devel
%{_includedir}/ucl/
%{_libdir}/libucl.so

%changelog
%autochangelog
