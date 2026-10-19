%global source0_hash d4d1a62766695455f1b616f5f7603458e6d23df787ebabc31ffda1c6298d0509
Name:           libpri
Version:        1.6.1
%global so_version 1.4
Release:        1%{?dist}
Summary:        An implementation of Primary Rate ISDN
License:        %{shrink:
                GPL-2.0-only WITH libpri-OpenH323-exception AND
                GPL-2.0-only WITH Asterisk-exception
                }
SourceLicense:  %{license} AND GPL-2.0-or-later
URL:            https://www.asterisk.org/
%global src_base https://downloads.asterisk.org/pub/telephony/libpri/releases
Source0:        %{src_base}/%{name}-%{version}.tar.gz
Source1:        %{src_base}/libpri-%{version}.tar.gz.asc
Source2:        libpri.gpg
Patch:          zero-sized-members.patch
# oreon:deps
BuildRequires:  dahdi-tools-devel
BuildRequires:  gcc
BuildRequires:  gpgverify
BuildRequires:  make
# /oreon:deps
%description
libpri is a C implementation of the Primary Rate ISDN specification. It was
based on the Bellcore specification SR-NWT-002343 for National ISDN. As of May
12, 2001, it has been tested work to with NI-2, Nortel DMS-100, and Lucent 5E
Custom protocols on switches from Nortel and Lucent.

%package devel
Summary:        Development files for libpri
Requires:       libpri%{?_isa} = %{version}-%{release}
%description devel
The libpri-devel package contains libraries and header files for developing
applications that use libpri.

%package doc
Summary:        Documentation for libpri
BuildArch:      noarch
%description doc
Currently, the libpri-doc package contains the pseudocode for the finite state
machines used in its implementation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

%make_build
%install
%make_install INSTALL_BASE=%{_prefix} libdir=%{_libdir}
find %{buildroot} -name '*.a' -print -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

./rosetest
./testprilib
%files -f %{oreon_filedir}/main.list
%files -n libpri-devel -f %{oreon_filedir}/libpri-devel.list
%files -n libpri-doc -f %{oreon_filedir}/libpri-doc.list

%changelog

%autochangelog
