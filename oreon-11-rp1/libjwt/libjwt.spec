%global source0_hash d29e4250d437340b076350e910e69fd5539ef8b92528d0306745cec0e343cc17

Name:           libjwt
Version:        1.12.1
Release:        21%{?dist}
Summary:        A Javascript Web Token library in C

License:        MPL-2.0
URL:            https://github.com/benmcollins/libjwt
Source0:        https://github.com/benmcollins/libjwt/archive/v%{version}.tar.gz

Patch0:         without_examples.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  jansson-devel
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel

%description
A Javascript Web Token library in C

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
autoreconf -i

%build
%configure --disable-static --without-examples
%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%files
%license LICENSE
%doc *.md
%{_libdir}/*.so.1*

%files devel
%doc *.md
%{_includedir}/jwt.h
%{_libdir}/libjwt.so
%{_libdir}/pkgconfig/libjwt.pc

%changelog
%autochangelog
