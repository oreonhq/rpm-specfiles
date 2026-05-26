%if 0%{?fedora} >= 42 || 0%{?rhel} >= 10
# Python bindings removed post-0.5.5
# see commit 40c9ff981f1f3bd968af37a50b50c3478d8267cd
%bcond_with python
%else
%bcond_without python
%endif

%global mainlibsover 12
%global addrlibsover 3

Name:           libkdumpfile
Version:        0.5.5
Release:        %autorelease
Summary:        Kernel coredump file access

License:        LGPL-3.0-or-later OR GPL-2.0-or-later
URL:            https://github.com/ptesarik/libkdumpfile
Source:        https://github.com/ptesarik/libkdumpfile/releases/download/v0.5.5/libkdumpfile-0.5.5.tar.gz
# oreon url source checksums begin
%global source0_sha256 16415528e870791ac8d392422f0986b4c3f83e6cb4267b4daffe6982fc5f4a3a
%global source0_file libkdumpfile-0.5.5.tar.gz
# oreon url source checksums end

BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  binutils-devel
BuildRequires:  libzstd-devel
BuildRequires:  lzo-devel
%if %{with python}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%else
Obsoletes:      python3-libkdumpfile < 0.5.5-1
%endif
BuildRequires:  snappy-devel
BuildRequires:  zlib-devel

%global _description %{expand:
libkdumpfile is a library to read kdump-compressed kernel core dumps.}

%description %{_description}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel %{_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
# keep this until F38 is EOL (so Fedora < 41) as 0.5.1 was not noarch due to
# doxygen being run *after* rather than *before* build so it indexes "built"
# Python sources too
# likewise, EPEL 8 and 9 are affected
%if (0%{?fedora} && 0%{?fedora} < 41) || (0%{?rhel} && 0%{?rhel} < 10)
Obsoletes:      %{name}-doc < 0.5.2-1
%endif

%description    doc %{_description}

The %{name}-doc package contains documentation for %{name}.

%if %{with python}
%package -n python3-%{name}
Summary:        Python bindings for %{name}
Obsoletes:      %{name}-python < 0.4.0-6
Provides:       %{name}-python = %{version}-%{release}
Provides:       %{name}-python%{?_isa} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name} %{_description}

The python3-%{name} package contains Python bindings for %{name}.
%endif

%package        util
Summary:        Utilities to read kernel core dumps
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    util %{_description}
The %{name}-devel package contains misc utilities built with %{name}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libkdumpfile-0.5.5.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "16415528e870791ac8d392422f0986b4c3f83e6cb4267b4daffe6982fc5f4a3a" || { echo "oreon: Source0 SHA256 mismatch for libkdumpfile-0.5.5.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1
# Remove unneeded shebang
sed -e "\|#!/usr/bin/env python|d" -i python/*/*.py


%build
%configure \
%if %{without python}
  --with-python=no \
%endif
%{nil}

%{__make} doxygen-doc
%make_build


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# static artifacts are needed to run tests, but we don't
# want to ship them
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'


%check
%make_build check


%files
%license COPYING COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv3
%doc README.md NEWS
%{_libdir}/libaddrxlat.so.%{addrlibsover}{,.*}
%{_libdir}/libkdumpfile.so.%{mainlibsover}{,.*}

%files devel
%{_includedir}/%{name}/
%{_libdir}/libaddrxlat.so
%{_libdir}/libkdumpfile.so
%{_libdir}/pkgconfig/libaddrxlat.pc
%{_libdir}/pkgconfig/libkdumpfile.pc

%files doc
%license COPYING COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv3
%doc doc/html

%if %{with python}
%files -n python3-%{name}
%{python3_sitearch}/%{name}-%{version}-*.egg-info
%{python3_sitearch}/addrxlat/
%{python3_sitearch}/_addrxlat.*.so
%{python3_sitearch}/kdumpfile/
%{python3_sitearch}/_kdumpfile.*.so
%endif

%files util
%{_bindir}/dumpattr
%{_bindir}/kdumpid
%{_bindir}/listxendoms
%{_bindir}/showxlat
%{_mandir}/man1/kdumpid.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.5-1
- Prepare for Oreon 11 (RP1)
