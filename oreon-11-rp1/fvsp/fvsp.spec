%global source0_hash cca8b9a962914de0835d9f9b4c0493bf5e26b79236e6c1f7bde88b9cf384517e
Name:           fvsp
Version:        0.1
Release:        1%{?dist}
Summary:        Convert Perl version string into RPM-compatible version string
License:        LGPL-3.0-or-later
URL:            https://ppisar.fedorapeople.org/%{name}/
Source0:        https://ppisar.fedorapeople.org/%{name}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n fvsp-devel -f %{oreon_filedir}/fvsp-devel.list

%changelog

%autochangelog
