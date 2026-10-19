%global source0_hash 3de8028664faf2d065ee5a5e8f974ce189b93a192517fb1474e135eba7daf05b
%global debug_package %{nil}
Name:           ell
Version:        0
Release:        1%{?dist}
Summary:        Header-only C++ library to write EBNF grammars
License:        LGPL-3.0-or-later
URL:            http://code.google.com/p/ell/
Source0:        ell-20130617.tar.xz
# oreon:deps

# /oreon:deps
%description
Embedded LL library is pure-header library to write EBNF grammars as C++ code.
It eases the development of parser or similar applications, while removing the
need to write a lexer.

%package        devel
BuildArch:      noarch
Summary:        Development files for ELL
Provides:       %{name}-static = %{version}-%{release}
%description devel
%{name}-devel is only required for building software that uses the ELL library.
Because ELL is a header-only library, there is no matching run-time package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ell-20130617

%build

%install
mkdir -p %{buildroot}%{_includedir}/ell
cp -pr libELL/Include/ell/*.h %{buildroot}%{_includedir}/ell
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ell-devel -f %{oreon_filedir}/ell-devel.list

%changelog

%autochangelog
