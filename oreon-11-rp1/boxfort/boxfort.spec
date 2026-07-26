%global source0_hash 47fde5ce6fbbd7166268e97edc0fc22ed2bf0bf4d93b81ee30d664a8c35a155c

%global forgeurl https://github.com/Snaipe/BoxFort
Version:        0.1.5
%forgemeta

Name:           boxfort
Release:        %autorelease
Summary:        Convenient & cross-platform sandboxing C library
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

# https://github.com/Snaipe/BoxFort/blob/master/meson.build#L81-L93
# ppc64le and s390x are not supported
ExcludeArch:    ppc64le s390x

BuildRequires:  gcc
BuildRequires:  meson

%description
BoxFort is a simple, cross-platform sandboxing C library powering Criterion.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%meson -Ddefault_library=shared
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_libdir}/libboxfort.so.0*

%files devel
%{_includedir}/boxfort.h
%{_libdir}/libboxfort.so
%{_libdir}/pkgconfig/boxfort.pc

%changelog
%autochangelog
