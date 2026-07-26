%global source0_hash baac28b60f8f46ae0f273155f4968b20e84380016629247ed2a4d7e3fbeb4d98

Name:			libsafec
Version:		3.7.1
Release:		7%{?dist}
Summary:		Safec fork with all C11 Annex K functions

License:		MIT
URL:			https://github.com/rurban/safeclib
Source0:		%url/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	libtool

%description
This library implements the secure C11 Annex K1 functions on top of most
libc implementations, which are missing from them.

%package -n libsafec-devel
Summary: Development packages for libsafec
Requires:		libsafec%{?_isa} = %{version}-%{release}

%description -n libsafec-devel
Development files for libsafec

%package -n libsafec-check
Summary: Finds unsafe APIs
Requires:		perl-DirHandle

%description -n libsafec-check
Traverses specified directory trees and/or files (cwd by default)
searching for C source files (*.c), rooting out unsafe API calls.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n safeclib-%{version}

%build
autoreconf -Wall --install
%configure --disable-static --disable-doc --enable-strmax=0x8000
%make_build

%install
%make_install

%files -n libsafec
%license COPYING
%{_libdir}/libsafec.so.*

%files -n libsafec-devel
%{_includedir}/safeclib
%{_libdir}/libsafec.so
%{_libdir}/pkgconfig/*.pc

%files -n libsafec-check
%license COPYING
%{_bindir}/check_for_unsafe_apis

%changelog
%autochangelog
