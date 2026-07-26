%global source0_hash 66fd881f6c68171a1940a73b02a7b687f80e6621dc66a2a3c14fc699b05c92a0

%global forgeurl https://gitlab.freedesktop.org/cangjie/libcangjie
%global archiveext tar.xz

Name:             libcangjie
Summary:          Cangjie Input Method Library
Version:          1.4.0
Release:          %autorelease
License:          LGPL-3.0-or-later
URL:              http://cangjians.github.io/projects/%{name}
Source0:          https://gitlab.freedesktop.org/cangjie/%{name}/-/archive/v%{version}/%{name}-%{version}.%{archiveext}

BuildRequires:    gcc
BuildRequires:    sqlite-devel
BuildRequires:    meson

# Split out so it can be noarch
Requires:         %{name}-data = %{version}-%{release}

%description
Library implementing the Cangjie input method.

%package data
Summary:          Database for %{name}
BuildArch:        noarch

%description data
Database for %{name}.

%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{_isa} = %{version}-%{release}
Requires:         sqlite-devel

%description devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f '{}' \;

%check
%meson_test

%files
%doc AUTHORS COPYING README.md
%{_libdir}/%{name}.so.3*

%files data
%doc data/README.table.md
%{_datadir}/%{name}

%files devel
%doc docs/*.md
%{_bindir}/libcangjie-*
%{_includedir}/cangjie
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/cangjie.pc

%changelog
%autochangelog
