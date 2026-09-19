%global source0_hash 0efe6cbd7bff31983e0d416df0436767665cc4cd70d278c06ce0e83e0eeab5db

Name:          tinycompress
Version:       1.2.13
Release:       4%{?dist}
Summary:       A library for compress audio offload in alsa
# Automatically converted from old format: BSD and LGPLv2 - review is highly recommended.
License:       LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2
URL:           http://alsa-project.org/
Source0:       ftp://ftp.alsa-project.org/pub/tinycompress/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires: gcc

%description
tinycompress is a library for compress audio offload in alsa

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
Files for development with %{name}.

%package utils
Summary: Utilities for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Utilies for testing of compressed audio with %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-static

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete

%check
make check

%ldconfig_scriptlets

%files
%license COPYING
%doc README
%{_libdir}/*.so.*

%files devel
%{_includedir}/tinycompress*
%{_libdir}/*.so
%{_libdir}/pkgconfig/tinycompress.pc

%files utils
%{_bindir}/cplay
%{_bindir}/crecord

%changelog
%autochangelog
