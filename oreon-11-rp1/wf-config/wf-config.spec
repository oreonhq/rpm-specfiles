%global source0_hash 4264edf9f5f5ff9bccaee1ab3f5b2613a0db526bc90c15d7c82eb05a3fc81307

# Tests fails on s390x arch since 0.10.0
%ifnarch s390x
%bcond_without test
%else
%bcond_with test
%endif

%global forgeurl https://github.com/WayfireWM/wf-config

Name:           wf-config
Version:        0.10.0
%forgemeta
Release:        %autorelease
Summary:        Library for managing configuration files, written for wayfire

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  cmake(glm)
%if %{with test}
BuildRequires:  cmake(doctest)
%endif
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libxml-2.0)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%if %{with test}
%meson \
    -Dtests=enabled
%else
%meson \
    -Dtests=disabled
%endif

%meson_build

%install
%meson_install

%if %{with test}
%check
%meson_test
%endif

%files
%license LICENSE
%{_libdir}/lib%{name}.so.0*
%{_libdir}/lib%{name}.so.1*

%files devel
%{_includedir}/wayfire/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
