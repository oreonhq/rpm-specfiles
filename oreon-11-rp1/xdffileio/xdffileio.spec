%global source0_hash 63a69abcc1a2e0fb629cdb29e90a3f85c5e8f9c809040234da2d2934ecfb3254
Name:           xdffileio
Version:        1.0
Release:        1%{?dist}
Summary:        Unified interface to read/write EEG file format in realtime
License:        LGPL-3.0-or-later
URL:            http://cnbi.epfl.ch/software/xdffileio.html
Source0:        https://github.com/nbourdau/xdffileio/archive/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gnulib-devel
BuildRequires:  make
# /oreon:deps
%description
xdffileio provides a unified interface to read/write EEG file format in
realtime. It has been designed to provide a consistent and common interface
to all supported file formats while minimizing the CPU cost on the main loop.
It thus performs all the expensive operation (scaling, data convertion and
file operation) in a separated thread.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{name}-%{version}
%oreon_prep
%build

./autogen.sh
%configure \
%ifarch %{ix86}
        CFLAGS='%{optflags} -march=pentium4'
%endif
%make_build V=1
%install
%make_install
rm -f %{buildroot}%{_libdir}/lib%{name}.la
rm -vrf %{buildroot}%{_docdir}/%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check V=1
rm -vrf doc/example/{.dirstamp,.deps,*.o}
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n xdffileio-devel -f %{oreon_filedir}/xdffileio-devel.list

%changelog

%autochangelog
