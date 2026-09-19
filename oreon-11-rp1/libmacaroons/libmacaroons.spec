%global source0_hash e1db403c01b0407a276a84b2aaf54515faebe1a5c1a31ec10857a1917161d109

Name:		libmacaroons
Version:	0.3.0
Release:	24%{?dist}
Summary:	C library supporting generation and use of macaroons

License:	BSD-3-Clause AND ISC
URL:		https://github.com/rescrv/libmacaroons
Source0:	%url/archive/releases/%{version}/%{name}-%{version}.tar.gz
# Fix for the inspect() method triggering an assert on newer versions of libsodium.
# See the upstream PR: https://github.com/rescrv/libmacaroons/pull/52
Patch0:		libmacaroons-hex-encoding.patch

# Fix for the memory leak when the deserialize routine succeeds.
# See the upstream PR: https://github.com/rescrv/libmacaroons/pull/56
Patch1:		libmacaroons-deserialize-memleak.patch

BuildRequires:	libsodium-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	python3
BuildRequires:	make

%description
%{summary}

%package devel
Summary:	Development libraries linking against libmacaroons
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-releases-%{version}
%patch -P0 -p 1
%patch -P1 -p 1

%build
autoreconf -i
%configure --disable-static
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/%{name}.la

%files
%license LICENSE
%doc README
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/macaroons.h

%changelog
%autochangelog
