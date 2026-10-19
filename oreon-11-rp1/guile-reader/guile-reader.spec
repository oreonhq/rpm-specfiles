%global source0_hash b4353e89699eb3f05b492cc2b2721580da68468a39c278545e02e344c0e64728
%define       mver 3.0
Name:         guile-reader
Version:      0.6.3
Release:        1%{?dist}
Summary:        A simple framework for building readers for GNU Guile
License:      GPL-3.0-or-later
URL:          https://www.nongnu.org/guile-reader/%{name}
Source0:        https://git.savannah.nongnu.org/cgit/%{name}.git/snapshot/%{name}-%{version}.tar.gz
Patch0:       config.patch
Patch1:       header.patch
Requires:       info
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  gperf
BuildRequires:  guile30-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  texinfo
# /oreon:deps
%package devel
Summary: Development files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description
The idea is to make it easy to build procedures that extend
Guile’s read procedure. Readers supporting various syntax
variants can easily be written, possibly by re-using existing
“token readers” of a standard Scheme readers.

%description devel
Files to allow guile-reader to be used from other applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoupdate
autopoint
libtoolize
autoreconf -fi --verbose --warnings=none
%configure --with-guilemoduledir=%{_datadir}/guile/site/%{mver} \
	   GUILE=/usr/bin/guile3.0
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check  

make check
%files -f %{oreon_filedir}/main.list
%files -n guile-reader-devel -f %{oreon_filedir}/guile-reader-devel.list

%changelog

%autochangelog
