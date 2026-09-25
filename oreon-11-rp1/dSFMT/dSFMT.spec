%global source0_hash fba11fe3ffbd7c0c82a338f210c1387ed3b4a9a5a73b4a24667e1311d6002475

Name:           dSFMT
Version:        2.2.3
Release:        29%{?dist}
Summary:        Double precision SIMD-oriented Fast Mersenne Twister

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/MersenneTwister-Lab/dSFMT
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Patch0:         %{name}-%{version}_sharedlib.patch
Patch1:         %{name}-%{version}_pkgconfig.patch
Patch2:         %{name}-%{version}_exportfuns.patch

BuildRequires:  gcc
BuildRequires: make
%description
The purpose of dSFMT is to speed up the generation by avoiding
the expensive conversion of integer to double (floating point).
dSFMT directly generates double precision floating point
pseudo-random numbers which have the IEEE Standard for Binary
Floating-Point Arithmetic (ANSI/IEEE Std 754-1985) format.

dSFMT is only available on the CPUs which use IEEE 754 format
double precision floating point numbers.

dSFMT doesn't support integer outputs.
dSFMT supports the output of double precision floating point
pseudo-random numbers which distribute in the range of
[1, 2), [0, 1), (0, 1] and (0, 1).
And it also supports the various periods form 2607-1 to 2132049-1.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        devel-doc
Summary:        Development documentation files for %{name}
BuildArch:      noarch

%description    devel-doc
The %{name}-devel-doc package contains API documentation for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
%patch -P0 -p 1
%patch -P1 -p 0
%patch -P2 -p 1

%build
make %{?_smp_mflags} \
     sharedlib \
     libdir=%{_libdir} CCFLAGS="-fPIC %{optflags} -fno-strict-aliasing"

%install
%make_install \
    DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} libdir=%{_libdir} includedir=%{_includedir}

%check
make std-check

%ldconfig_scriptlets

%files
%doc ./CHANGE-LOG.txt ./LICENSE.txt
%doc README.txt README.jp.txt
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*.h

%files devel-doc
%doc html/

%changelog
%autochangelog
