%global source0_hash 9db179cc4ca37dcf21f58b8320e33f626a275df8560c688c88c51797e02a04d6
Name:           pstreams-devel
Version:        1.0.4
Release:        1%{?dist}
Summary:        POSIX Process Control in C++
License:        BSL-1.0
URL:            http://pstreams.sourceforge.net/
Source0:        http://downloads.sourceforge.net/pstreams/pstreams-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  hostname
BuildRequires:  make
BuildRequires:  perl
# /oreon:deps
%description
PStreams classes are like C++ wrappers for the POSIX.2 functions
popen(3) and pclose(3), using C++ iostreams instead of C's stdio
library.

%package -n pstreams-doc
Summary: Documentation for pstreams
%description -n pstreams-doc
API documentation for the pstreams-devel package, in HTML format.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n pstreams-%{version}

%build

make %{?_smp_mflags} docs
%check

make %{?_smp_mflags} EXTRA_CXXFLAGS="$CXXFLAGS" check
%install
make install  DESTDIR=$RPM_BUILD_ROOT includedir=%{_includedir}
%oreon_autofiles pstreams-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n pstreams-doc -f %{oreon_filedir}/pstreams-doc.list

%changelog

%autochangelog
