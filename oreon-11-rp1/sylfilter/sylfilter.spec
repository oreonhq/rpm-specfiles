%global source0_hash e1a4bf0df666acf4a1ee8ba41d077a3e59a8c1f9f35f62c5d960548f9c2e74b5

###  for Fedora  ###

Name:     sylfilter
Summary:  A generic message filter library and command-line tools
Version:  0.8
Release:  31%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:  LicenseRef-Callaway-BSD
URL:      http://sylpheed.sraoss.jp/sylfilter/
Source0:  http://sylpheed.sraoss.jp/sylfilter/src/sylfilter-%{version}.tar.xz
BuildRequires: make
BuildRequires:  gcc
BuildRequires: sqlite-devel
BuildRequires: glib2-devel
BuildRequires: sylpheed-devel

%package devel
Summary: Development files for sylfilter
Requires: sylfilter%{?_isa} = %{version}-%{release}
Requires: sqlite-devel
Requires: glib2-devel

%description
This is SylFilter, a generic message filter library, and some command-line tools
that provide a Bayesian filter which is very popular as a spam filtering
algorithm.

SylFilter is also internationalized and can be applied to any languages.

The SylFilter library provides simple but powerful C APIs and can be used from
C programs. 

SylFilter can be used as a command-line tool inside a junk filter mail program
similar to major tools such as bogofilter and bsfilter etc.

For further details, see http://sylpheed.sraoss.jp/sylfilter/

%description devel
Development files for sylfilter

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --with-libsylph=sylpheed --with-libsylph-dir=/usr --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%{make_build}

%install
%{make_install}
rm %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc README
%{_bindir}/sylfilter
%{_libdir}/libsylfilter.*
%{_libdir}/libsylfilter.so.*
%license COPYING

%files devel
%{_libdir}/libsylfilter.so
%{_includedir}/sylfilter

%changelog
%autochangelog
