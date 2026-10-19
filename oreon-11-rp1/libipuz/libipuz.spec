%global source0_hash 305a83e76b7c683b5cdd71f60d5c232c6f8fa3015cd4269b8b246d702c83ea85
%bcond docs 1
%bcond introspection 1
%global soversion 0.5
Name:           libipuz
Version:        0.5.5
Release:        1%{?dist}
Summary:        Library for parsing .ipuz puzzle files
License:        %{shrink:
    (LGPL-2.1-or-later OR MIT) 
AND (Apache-2.0 OR MIT)
AND (BSD-2-Clause OR Apache-2.0 OR MIT)
AND MIT
AND (MIT OR Apache-2.0)
AND (Unlicense OR MIT)
}
URL:            https://gitlab.gnome.org/jrb/libipuz
Source0:        https://gitlab.gnome.org/jrb/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
%if %{with docs}
%endif
%if %{with introspection}
%endif
# oreon:deps
BuildRequires:  cargo-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  json-glib-devel
BuildRequires:  meson
BuildRequires:  python3
BuildRequires:  python3dist(myst-parser)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  sed
# /oreon:deps
%description
This is a library for parsing .ipuz puzzle files, for crossword puzzles,
sudokus, etc. The library only handles crosswords for now.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if %{with docs}
Suggests:       %{name}-doc = %{version}-%{release}
%endif
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with docs}
%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc
This package contains additional documentation for %{name}.
%endif

%package        tests
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    tests
The %{name}-tests package contains tests for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Drop version locks
rm libipuz/rust/Cargo.lock
sed -i '/Cargo.lock/d' libipuz/rust/meson.build

%build

%meson
%meson_build
pushd libipuz/rust >/dev/null
%{cargo_license_summary}
%{cargo_license} > ../../LICENSE.dependencies
popd >/dev/null
%if %{with docs}
sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}
%endif
%install
%meson_install
%find_lang %{name}-1.0
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%check

%meson_test --timeout-multiplier 10
%files -f %{oreon_filedir}/main.list
%files -n libipuz-devel -f %{oreon_filedir}/libipuz-devel.list
%files -n libipuz-doc -f %{oreon_filedir}/libipuz-doc.list
%files -n libipuz-tests -f %{oreon_filedir}/libipuz-tests.list

%changelog

%autochangelog
