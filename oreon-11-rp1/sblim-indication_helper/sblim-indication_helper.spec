Name:		sblim-indication_helper
Version:	0.5.0
Release:	17%{?dist}
Summary:	Toolkit for CMPI indication providers

License:	EPL-1.0
URL:		https://sourceforge.net/projects/sblim/
Source0:	http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
# oreon url source checksums begin
%global source0_sha256 542df88238429144d8f8f2712701f455e563bf5026d01e131224ae319b697622
%global source0_file sblim-indication_helper-0.5.0.tar.bz2
# oreon url source checksums end
BuildRequires: make
BuildRequires:	sblim-cmpi-devel 
BuildRequires:	gcc gcc-c++

%description
This package contains a developer library for helping out when writing
CMPI providers. This library polls the registered functions for data
and, if it changes, a CMPI indication is set with the values of the
indication class properties (also set by the developer).

%Package	devel
Summary:	Toolkit for CMPI indication providers (Development Files)
Requires:	%{name} = %{version}-%{release} sblim-cmpi-devel glibc-devel

%description devel
This package contain developer library for helping out when writing
CMPI providers. This library polls the registered functions for data
and if they change an CMPI indication is set with the values of the
indication class properties (also set by the developer).

This package holds the development files for sblim-indication_helper.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/sblim-indication_helper-0.5.0.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "542df88238429144d8f8f2712701f455e563bf5026d01e131224ae319b697622" || { echo "oreon: Source0 SHA256 mismatch for sblim-indication_helper-0.5.0.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
%configure --disable-static --with-pic
%make_build

%install
%make_install
rm $RPM_BUILD_ROOT/%{_libdir}/libind_helper.la

%ldconfig_scriptlets

%files
%license COPYING
%doc README ChangeLog TODO
%{_libdir}/libind_helper.so.*

%files devel
%{_includedir}/sblim
%{_libdir}/libind_helper.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.0-17
- Prepare for Oreon 11 (RP1)
