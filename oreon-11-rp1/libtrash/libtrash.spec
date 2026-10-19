%global source0_hash 90081cdd035ceaeb871522b02e65bf53e50d7770728c98b5e08d57d540f93280
Summary:        Libraries to move files to a trash-folder on delete
Name:          libtrash
Version:       3.8
Release:        1%{?dist}
License:       GPL-2.0-or-later
URL:           https://pages.stern.nyu.edu/~marriaga/software/libtrash
Source0:        https://pages.stern.nyu.edu/~marriaga/software/libtrash/%{name}-%{version}.tgz
Patch0:        libtrash-3.2-defaults.patch
Patch1:        libtrash-3.3-license.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Libtrash is the shared library which, when preloaded, implements a trash
can under GNU/Linux. Through the interception of function calls which
might lead to accidental data loss libtrash effectively ensures that your
data remains protected from your own mistakes.

%package devel
Summary: Libraries to move files to a trash-folder on delete
Requires: libtrash%{?_isa} = %{version}-%{release}
%description devel
This package contains the libtrash.so dynamic library which, when preloaded,
implements a trash can under GNU/Linux.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
mkdir -p m4

%build

autoreconf -fi
%configure
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/libtrash.la
rm -f %{buildroot}%{_docdir}/%{name}/AUTHORS
rm -f %{buildroot}%{_docdir}/%{name}/{BUILD,INSTALL}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libtrash-devel -f %{oreon_filedir}/libtrash-devel.list

%changelog

%autochangelog
