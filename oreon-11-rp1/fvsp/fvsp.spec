%global source0_hash cca8b9a962914de0835d9f9b4c0493bf5e26b79236e6c1f7bde88b9cf384517e

Name:           fvsp
Version:        0.1
Release:        25%{?dist}
Summary:        Convert Perl version string into RPM-compatible version string
License:        LGPL-3.0-or-later
URL:            https://ppisar.fedorapeople.org/%{name}/
Source0:        %{url}%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

%description
This is a tool and library for converting Perl version strings into RPM
version strings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
autoreconf -f

%build
%configure \
    --enable-shared \
    --disable-static
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -delete

%files
%license COPYING
%doc README AUTHORS NEWS
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%{_includedir}/fvsp.h
%{_libdir}/*.so
%{_mandir}/man3/*

%changelog
%autochangelog
