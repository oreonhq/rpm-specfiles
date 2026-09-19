%global source0_hash fe1944cdd42a3aac8872a957bfb2afa2cc0c20d2ec9299a04900dceb02331afc

%bcond_without tests

%global forgeurl https://github.com/armon/libart
%global commit 301046804af165269e37da6725f5a4aec9ecc881
%forgemeta

Name:           libart
Version:        0
Release:        %autorelease
Summary:        Adaptive Radix Trees implemented in C

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  make
%if %{with tests}
BuildRequires:  check-devel
%endif

%description
This library provides a C99 implementation of the Adaptive Radix Tree or ART.
The ART operates similar to a traditional radix tree but avoids the wasted
space of internal nodes by changing the node size. It makes use of 4 node sizes
(4, 16, 48, 256), and can guarantee that the overhead is no more than 52 bytes
per key, though in practice it is much lower.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1
# remove bundled version of check
rm -r deps

%build
%set_build_flags
%make_build \
  SHCFLAGS="%{optflags} -fPIC" \
  SHLINKFLAGS="%{build_ldflags} -shared -Wl,-soname,libart.so.%{version}"

%if %{with tests}
# Based on the scons build config (which is broken in multiple ways)
$CC $CFLAGS -Isrc -o test_runner tests/runner.c -Lsrc -L/usr/lib $LDFLAGS -lcheck -lart
%endif

%install
# make install has several issues so do it by hand instead
install -Dpm0755 src/libart.so %{buildroot}%{_libdir}/libart.so.%{version}
ln -s libart.so.%{version} %{buildroot}%{_libdir}/libart.so
install -Dpm0644 -t %{buildroot}%{_includedir} src/art.h

%if %{with tests}
%check
LD_LIBRARY_PATH="%{buildroot}%{_libdir}" ./test_runner
%endif

%files
%license LICENSE
%doc README.md
%{_libdir}/libart.so.*

%files devel
%{_includedir}/*
%{_libdir}/libart.so

%changelog
%autochangelog
