# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 96d33abb4bb0070c7be0fed4246cd38416188325f820468214471938545b1ac8
%global source1_sha256 b70a224cd52e82b7a8150aedac5efa2d0cb3941696fd829bdbe674f9f65c3926
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })} \
%{?source1_sha256:%(test -z "%{source1_sha256}" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_sha256}" || { echo "oreon: Source1 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# Whether to package the compatibility .so from the previous release.
# This installs self as a build dependency and copies the files.
# Once disabled, it can only be built when the previous version is tagged in.
# It is required to be able to rebuild Pythons with the new library.
%bcond compat 0

Name:           mpdecimal
Version:        4.0.1
Release:        %autorelease
Summary:        Library for general decimal arithmetic
License:        BSD-2-Clause

URL:            https://www.bytereef.org/mpdecimal/index.html
Source0:        https://www.bytereef.org/software/mpdecimal/releases/mpdecimal-%{version}.tar.gz
Source1:        https://speleotrove.com/decimal/dectest.zip

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  unzip
%if %{with compat}
BuildRequires:  %{name}
%endif

%description
The package contains a library libmpdec implementing General Decimal
Arithmetic Specification. The specification, written by Mike Cowlishaw from
IBM, defines a general purpose arbitrary precision data type together with
rigorously specified functions and rounding behavior.

%package -n %{name}++
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Library for general decimal arithmetic (C++)

%description -n %{name}++
The package contains a library libmpdec++ implementing General Decimal
Arithmetic Specification. The specification, written by Mike Cowlishaw from
IBM, defines a general purpose arbitrary precision data type together with
rigorously specified functions and rounding behavior.

%package        devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}++%{?_isa} = %{version}-%{release}
Summary:        Development headers for mpdecimal library

%description devel
The package contains development headers for the mpdecimal library.

%prep
%oreon_verify_sources
%autosetup
unzip -d tests/testdata %{SOURCE1}

%build
%configure --disable-static
# Set LDXXFLAGS to properly pass the buildroot
# linker flags to the C++ extension.
%make_build LDXXFLAGS="%{build_ldflags}"

%check
%make_build check

%install
%make_install

# license will go into dedicated directory
rm %{buildroot}%{_docdir}/%{name}/COPYRIGHT.txt

%if %{with compat}
cp -a %{_libdir}/libmpdec.so.2.5.1 %{buildroot}%{_libdir}/libmpdec.so.3
%endif

%files
%doc README.txt CHANGELOG.txt
%license COPYRIGHT.txt
%{_libdir}/libmpdec.so.%{version}
%{_libdir}/libmpdec.so.4
%if %{with compat}
%{_libdir}/libmpdec.so.3
%endif

%files -n %{name}++
%{_libdir}/libmpdec++.so.%{version}
%{_libdir}/libmpdec++.so.4

%files devel
%{_libdir}/libmpdec.so
%{_libdir}/libmpdec++.so
%{_includedir}/mpdecimal.h
%{_includedir}/decimal.hh
%{_libdir}/pkgconfig/libmpdec.pc
%{_libdir}/pkgconfig/libmpdec++.pc
%{_mandir}/man3/libmpdec.3*
%{_mandir}/man3/libmpdec++.3*
%{_mandir}/man3/mpdecimal*.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.0.1-1
- Prepare for Oreon 11 (RP1)
