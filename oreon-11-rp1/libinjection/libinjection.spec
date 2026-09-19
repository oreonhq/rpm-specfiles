%global source0_hash 9dd7ae68a21a3c50f705c383b1b714c77fd4093b0a561a5400f0cb0ad79b1ae7

Summary: SQL / SQLI tokenizer parser analyzer library
Name: libinjection
Version: 3.10.0
Release: 15%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: https://github.com/libinjection/libinjection
Source0: https://github.com/libinjection/libinjection/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: Makefile-libinjection
Patch0: libinjection-3.10.0-use_correct_version.patch
Patch1: 0001-Cosmetics-addresses-some-issues-reported-by-cppcheck.patch
Patch2: 0002-Specify-Python-version-explicitly-in-shebangs.patch
Patch3: 0003-Adds-usage-info-libinjection_xss.patch
Patch4: 0004-Fix-cppcheck-errors.patch
Patch5: 0005-Pass-the-correct-pointer-to-memmem.patch
Patch6: 0006-feat-py3-update-build-syntax-to-py3.patch
Buildrequires: gcc make libtool python3

%description
SQL / SQLI tokenizer parser analyzer library

%package tests
Summary: Various tools for testing %{name}
Requires: %{name}%{_isa} = %{version}-%{release}

%description tests
The %{name}-tests package contains various tools for testing.

Use it like:
reader -m 21 %{_datadir}/%{name}/false_*.txt

%package devel
Summary: Development files for %{name}
Requires: %{name}%{_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
cp %{SOURCE1} src/Makefile

%build
%{__make} \
    CFLAGS="%{build_cflags}" \
    LDFLAGS="%{build_ldflags}" \
    -C src

%install
%makeinstall -C src

install -d %{buildroot}%{_datadir}/%{name}/
install -m0644 data/* %{buildroot}%{_datadir}/%{name}/

install -d %{buildroot}%{_libdir}/pkgconfig

cat > %{buildroot}%{_libdir}/pkgconfig/libinjection.pc << EOF
# libinjection pkg-config file

prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: libinjection
Description: SQL / SQLI tokenizer parser analyzer library
URL: https://github.com/libinjection/libinjection
Version: %{version}
Requires:
Conflicts:
Libs: -L\${libdir} -linjection
Cflags: -I\${includedir}
EOF

# cleanup
rm -f %{buildroot}%{_libdir}/libinjection.*a

# For EPEL7 compatibility
%ldconfig_scriptlets

%files
%license COPYING
%doc README*
%{_bindir}/fptool
%{_bindir}/html5
%{_bindir}/sqli
%{_libdir}/*.so.*

%files tests
%{_bindir}/reader
%{_bindir}/testdriver
%{_bindir}/testspeedsqli
%{_bindir}/testspeedxss
%{_datadir}/%{name}

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
%autochangelog
