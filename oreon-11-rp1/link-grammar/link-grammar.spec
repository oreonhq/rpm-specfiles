%global source0_hash d9572ab811aedcbdb102d5d97b9f2c1fc4f491616a507de8d5c6d1388d5adda5
%ifarch %{java_arches}
%global JAVA 1
%else
%global JAVA 0
%endif
Summary:        A full-service natural language dependency parser
Name: link-grammar
Version: 5.99.42
Release:        1%{?dist}
License: LGPL-2.1-or-later
Source0:        https://www.gnucash.org/link-grammar/downloads/%{version}/link-grammar-%{version}.tar.gz
URL: https://opencog.github.io/link-grammar-website/
# oreon:deps
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  hunspell-devel
BuildRequires:  libedit-devel
BuildRequires:  make
BuildRequires:  minisat2-devel
BuildRequires:  pcre2-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  swig
# /oreon:deps
%description
A full-service natural language dependency parser for
English and Russian, with prototypes for other assorted languages.

%package devel
Summary: Support files necessary to compile applications with liblink-grammar
Requires: link-grammar = %{version}-%{release}
%description devel
Libraries, headers, and support files needed for using liblink-grammar.

%package perl
Summary: Perl libraries for liblink-grammar
Requires: perl-interpreter
Requires: link-grammar = %{version}-%{release}
%description perl
Perl libraries for liblink-grammar

%package python3
Summary: Python 3 libraries for liblink-grammar
Requires: link-grammar = %{version}-%{release}
%description python3
Python 3 libraries for liblink-grammar

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

PYTHON_NOVERSIONCHECK=1 PYTHON=%{__python3} PYTHON_VERSION=%{python3_version} %configure --disable-static --enable-pthreads --disable-aspell --enable-perl-bindings
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
%install
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/perl5/
mv $RPM_BUILD_ROOT%{_prefix}/local/lib*/perl5/* $RPM_BUILD_ROOT/%{_libdir}/perl5/
find $RPM_BUILD_ROOT/%{_libdir}/ -name '*.la' | xargs rm -f
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n link-grammar-devel -f %{oreon_filedir}/link-grammar-devel.list
%files -n link-grammar-perl -f %{oreon_filedir}/link-grammar-perl.list
%files -n link-grammar-python3 -f %{oreon_filedir}/link-grammar-python3.list

%changelog

%autochangelog
