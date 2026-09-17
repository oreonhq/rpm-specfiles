%global source0_hash bf2a80d1bacbf10a9fc686870ace4802524ff1b5fd5ba22a9c51b82a4aa718a0

%global somajor 1

Name:           libucontext
Version:        1.5
Release:        2%{?dist}
Summary:        ucontext implementation featuring glibc-compatible ABI

License:        ISC
URL:            https://github.com/kaniini/libucontext
Source:         https://distfiles.ariadne.space/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  gcc

%description
libucontext is a library which provides the ucontext.h C API.
Unlike other implementations, it faithfully follows the Linux
kernel process ABI when doing context swaps.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson -Ddefault_library=shared -Dexport_unprefixed=false -Dfreestanding=true
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_libdir}/%{name}*.so.%{somajor}

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
