%global source0_hash 668cbc6d2c0a065bb6abe8494d5a1bb3549a14cd956a44a2df9095045623ea47
%global debug_package %{nil}
%bcond check 0
Name:          jpcre2
Version:       10.32.01
Release:        1%{?dist}
Summary:        C++ wrapper for PCRE2 library
License:       LicenseRef-Callaway-BSD
URL:           https://docs.neurobin.org/jpcre2/%{version}/
Source0:        https://github.com/jpcre2/jpcre2/archive/%{version}/jpcre2-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pcre2-devel
BuildRequires:  valgrind
# /oreon:deps
%description
PCRE2 is the name used for a revised API for the PCRE library, which is a set of
functions, written in C, that implement regular expression pattern matching
using the same syntax and semantics as Perl, with just a few differences. Some
features that appeared in Python and the original PCRE before they appeared in
Perl are also available using the Python syntax.

This provides some C++ wrapper classes/functions to perform regex operations
such as regex match and regex replace.

This project currently only contains header files, which can be found in the
%{name}-devel package.

%package    devel
Summary:    %{summary}
BuildArch:  noarch
Provides:   %{name}-static = %{version}-%{release}
Requires:   pcre2-devel
%description devel
PCRE2 is the name used for a revised API for the PCRE library, which is a set of
functions, written in C, that implement regular expression pattern matching
using the same syntax and semantics as Perl, with just a few differences. Some
features that appeared in Python and the original PCRE before they appeared in
Perl are also available using the Python syntax.

This provides some C++ wrapper classes/functions to perform regex operations
such as regex match and regex replace.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure \
    --enable-cpp11 \
    --enable-test \
%if %{with check}
    --enable-thread-check \
    --enable-valgrind \
%endif
%make_build
%install
%make_install
pushd %{buildroot}
mkdir -p ./%{_defaultlicensedir}/jpcre2
mv ./{%{_defaultdocdir},%{_defaultlicensedir}}/jpcre2/COPYING
rm ./%{_defaultdocdir}/jpcre2/NEWS
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%make_build check
%files -f %{oreon_filedir}/main.list
%files -n jpcre2-devel -f %{oreon_filedir}/jpcre2-devel.list

%changelog

%autochangelog
