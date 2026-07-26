%global source0_hash cf37ef00ac8efb28821dac1ad49e2c6b23b242d9d961fab6fcda72fc73a7291b

%global abi_ver 2

Name:           libscfg
Version:        0.2.0
Release:        %autorelease
Summary:        C library for a simple configuration file format

License:        MIT
URL:            https://codeberg.org/emersion/libscfg
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_libdir}/libscfg.so.%{abi_ver}
%{_libdir}/libscfg.so.%{version}

%files devel
%{_includedir}/scfg.h
%{_libdir}/libscfg.so
%{_libdir}/pkgconfig/scfg.pc

%changelog
%autochangelog
