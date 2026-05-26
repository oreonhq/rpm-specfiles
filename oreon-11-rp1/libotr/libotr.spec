# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 8b3b182424251067a952fb4e6c7b95a21e644fbb27fbd5f8af2b2ed87ca419f5
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global snapshot 0
Summary: Off-The-Record Messaging library and toolkit
Name: libotr
Version: 4.1.1
Release: 25%{?dist}
# Automatically converted from old format: GPLv2 and LGPLv2 - review is highly recommended.
License: GPL-2.0-only AND LicenseRef-Callaway-LGPLv2
Source0: http://otr.cypherpunks.ca/%{name}-%{version}.tar.gz
Url: http://otr.cypherpunks.ca/
Provides: libotr-toolkit = %{version}
Obsoletes: libotr-toolkit < %{version}
Requires: libgcrypt >= 1.2.0
Requires: pkgconfig
BuildRequires: make
BuildRequires:  gcc
BuildRequires: libgcrypt-devel >= 1.2.0, libgpg-error-devel
%if %{snapshot}
Buildrequires: libtool automake autoconf
%endif

Patch: libotr-4.1.1-versioning.patch
Patch: libotr-4.1.1-socket-h.patch

%description
Off-the-Record Messaging Library and Toolkit
This is a library and toolkit which implements Off-the-Record (OTR) Messaging.
OTR allows you to have private conversations over IM by providing Encryption,
Authentication, Deniability and Perfect forward secrecy.

%package devel
Summary: Development library and include files for libotr
Requires: %{name} = %{version}-%{release}, libgcrypt-devel >= 1.2.0
Conflicts: libotr3-devel

%description devel
The devel package contains the libotr library and include files.

%prep
%oreon_verify_sources
%autosetup -p1

%if %{snapshot}
aclocal
intltoolize --force --copy
autoreconf -s -i
%endif

%build
%configure --with-pic --disable-rpath --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} all

%install
rm -rf $RPM_BUILD_ROOT
make \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBINSTDIR=%{_libdir} \
	install
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS README COPYING COPYING.LIB NEWS Protocol*
%{_libdir}/libotr.so.*
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%doc ChangeLog
%{_libdir}/libotr.so
%{_libdir}/pkgconfig/libotr.pc
%dir %{_includedir}/libotr
%{_includedir}/libotr/*
%{_datadir}/aclocal/*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.1.1-25
- Prepare for Oreon 11 (RP1)
