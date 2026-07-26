%global source0_hash 07542b5ea2442143b125ba213b6823ff4a23fff352ecdd84bbebe1d154f4f5c1

Name:           htmlcxx
Version:        0.86
Release:        28%{?dist}
# Automatically converted from old format: LGPLv2 and GPLv2+ and ASL 2.0 and MIT - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2 AND GPL-2.0-or-later AND Apache-2.0 AND LicenseRef-Callaway-MIT
Summary:        A simple non-validating CSS1 and HTML parser for C++
Url:            http://htmlcxx.sourceforge.net/
Source0:        http://sourceforge.net/projects/htmlcxx/files/htmlcxx/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  chrpath

%description
htmlcxx is a simple non-validating html parser library for C++. 
It allows to fully dump the original html document, character by character, 
from the parse tree. It also has an intuitive tree traversal API.

%package devel
Summary:        Headers and Static Library for htmlcxx
BuildRequires:  pkgconfig
BuildRequires: make
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The htmlcxx-devel package contains libraries and header files for
developing applications that use htmlcxx.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# convert to utf8 due rpmlint warning W: file-not-utf8 /usr/share/doc/htmlcxx/AUTHORS
# convert to utf8 due rpmlint warning W: file-not-utf8 /usr/share/doc/htmlcxx/README
iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS
iconv -f iso8859-1 -t utf-8 README > README.conv && mv -f README.conv README

%build
# Build in C89 mode because the lexer/parser integration relies on implicit
# function declarations.
%global build_type_safety_c 0
%set_build_flags
CC="$CC -std=gnu89"
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure --disable-static --enable-shared

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} 
chrpath --delete %{buildroot}%{_bindir}/htmlcxx

# remove all '*.la' files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%check
make check

%ldconfig_scriptlets -n %{name}

%files
%doc AUTHORS ChangeLog README
%license COPYING LGPL_V2 ASF-2.0
%{_bindir}/*
%{_datadir}/*
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
