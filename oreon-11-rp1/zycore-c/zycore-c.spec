%global source0_hash bac3ca7a3f19b67579d7504180ddca788470fb8749889c6bafeea99bdee2da69

Name:           zycore-c
Version:        1.5.2

%global forgeurl https://github.com/zyantific/%{name}
%global commit ba34692d371cde5f45539b5fa26ea11b09721751 
%forgemeta

Release:        %autorelease
Summary:        Zyan Core Library for C

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson >= 1.3
BuildRequires:  pkgconfig(gtest)
BuildRequires:  doxygen

%description
The Zyan Core Library for C is an internal library providing platform
independent types, macros and a fallback for environments without LibC.

%package        devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains the documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
%meson \
    -Ddoc=enabled \
    -Dtests=enabled \
    -Dexamples=enabled \
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_libdir}/libZycore.so.1*

%files devel
%{_includedir}/Zycore/
%{_libdir}/pkgconfig/zycore.pc
%{_libdir}/libZycore.so

%files doc
%license LICENSE
%{_docdir}/Zycore/

%changelog
%autochangelog
