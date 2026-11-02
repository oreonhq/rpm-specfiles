%global source0_hash 7fec50b27deddab5455a9633780b6341eddfb96215a7619e93a76eb27178f653
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: swig
Version: 4.5.1
Release: 1%{?dist}
Summary: Connects C/C++ programs with scripting languages
License: GPL-3.0-or-later AND BSD-3-Clause
URL: https://www.swig.org
Source0: https://downloads.sourceforge.net/swig/swig-%{version}.tar.gz
Requires: pcre2

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: libstdc++-devel
BuildRequires: make
BuildRequires: pcre2-devel

%description
SWIG generates wrapper code that lets C and C++ programs be called from
scripting and other high-level languages.

%prep
%oreon_sha256
%autosetup -n swig-%{version} -p1

%build
%oreon_configure --disable-ccache --without-alllang
%oreon_make

%install
%oreon_make_install

%files
%license LICENSE LICENSE-GPL LICENSE-UNIVERSITIES COPYRIGHT
%doc README ANNOUNCE CHANGES.current
%{_bindir}/swig
%{_datadir}/swig
