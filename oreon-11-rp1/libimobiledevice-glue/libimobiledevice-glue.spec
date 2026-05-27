%global source0_hash 6e2849f221e6ab970566a115d42f3c20f8848e4d40c2ed61ac20dc85f40fa54f

Name:           libimobiledevice-glue
Version:        1.3.1
Release:        1%{?dist}
Summary:        Library with common code among libimobiledevice projects

License:        LGPL-2.1-or-later
URL:            https://github.com/libimobiledevice/libimobiledevice-glue
Source:        https://github.com/libimobiledevice/libimobiledevice-glue/releases/download/1.3.1/libimobiledevice-glue-1.3.1.tar.bz2

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  libplist-devel

%description
The libimobiledevice-glue library is library with common code used by libraries
and tools around the libimobiledevice project.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup

%build
%configure --disable-static
%make_build

%install
%make_install

%files
%license COPYING
%doc NEWS README.md
%{_libdir}/%{name}-1.0.so.0*

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}-1.0.so
%{_libdir}/pkgconfig/%{name}-1.0.pc

%changelog
* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.1-1
- Prepare for Oreon 11 (RP1)
