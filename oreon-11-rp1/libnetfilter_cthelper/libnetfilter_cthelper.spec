Name:           libnetfilter_cthelper
Version:        1.0.0
Release:        32%{?dist}
Summary:        User-space infrastructure for connection tracking helpers
License:        GPL-2.0-only
URL:            http://www.netfilter.org/projects/libnetfilter_cthelper/index.html
Source0:        http://www.netfilter.org/projects/libnetfilter_cthelper/files/libnetfilter_cthelper-%{version}.tar.bz2
# oreon url source checksums begin
%global source0_sha256 07618e71c4d9a6b6b3dc1986540486ee310a9838ba754926c7d14a17d8fccf3d
%global source0_file libnetfilter_cthelper-1.0.0.tar.bz2
# oreon url source checksums end
BuildRequires:  gcc
BuildRequires:  libmnl-devel >= 1.0.0, pkgconfig, kernel-headers
BuildRequires: make

%description
This library provides the infrastructure for the user-space helper
infrastructure available since the Linux kernel 3.6.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libmnl-devel >= 1.0.0
Requires:       kernel-headers

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libnetfilter_cthelper-1.0.0.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "07618e71c4d9a6b6b3dc1986540486ee310a9838ba754926c7d14a17d8fccf3d" || { echo "oreon: Source0 SHA256 mismatch for libnetfilter_cthelper-1.0.0.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -type f -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc COPYING README
%{_libdir}/*.so.*

%files devel
%doc examples
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/libnetfilter_cthelper
%{_includedir}/libnetfilter_cthelper/*.h
%{_libdir}/*.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.0-32
- Prepare for Oreon 11 (RP1)
