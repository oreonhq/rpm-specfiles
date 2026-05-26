Name:		libhangul
Version:	0.2.0
Release:	3%{?dist}

License:	LGPL-2.1-or-later
URL:		https://github.com/libhangul/libhangul
Source0:	https://github.com/libhangul/libhangul/releases/download/libhangul-%{version}/libhangul-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 ea04e6a0cf4840a2a3b5641c1761068c78691036db839d0838f4e7a6553a5120
%global source0_file libhangul-0.2.0.tar.gz
# oreon url source checksums end

Summary:	Hangul input library
BuildRequires:	  gettext-devel, automake, libtool
BuildRequires:	  make


%description
libhangul provides common features for Hangul input method programs.


%package devel
Summary:	Development files for libhangul
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig
%description devel
This package contains development files necessary to develop programs
providing Hangul input.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libhangul-0.2.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ea04e6a0cf4840a2a3b5641c1761068c78691036db839d0838f4e7a6553a5120" || { echo "oreon: Source0 SHA256 mismatch for libhangul-0.2.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
autoreconf -fi
%configure --disable-static

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

rm $RPM_BUILD_ROOT%{_libdir}/%{name}.la
%find_lang %{name}


%ldconfig_scriptlets


%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/lib*.so.*
%{_datadir}/%{name}
%{_bindir}/hangul

%files devel
%{_includedir}/hangul-*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.0-3
- Import
