# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 71b8d6e8f5fe81f6c6d0d110e3892251f6ce76ed095abd315e26e6e1193af3af

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%bcond check 1

Name:           jq
Version:        1.8.2
Release:        1%{?dist}
Summary:        Command-line JSON processor

License:        MIT AND ICU AND CC-BY-3.0
URL:            https://jqlang.org/
Source0:        https://github.com/jqlang/jq/releases/download/jq-%{version}/jq-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  oniguruma-devel

%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif
BuildRequires:  make
BuildRequires:  tzdata
BuildRequires:  oreon-rpm-macros



%description
lightweight and flexible command-line JSON processor

 jq is like sed for JSON data – you can use it to slice
 and filter and map and transform structured data with
 the same ease that sed, awk, grep and friends let you
 play with text.

 It is written in portable C, and it has zero runtime
 dependencies.

 jq can mangle the data format that you have into the
 one that you want with very little effort, and the
 program to do so is often shorter and simpler than
 you'd expect.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}


%prep
%oreon_sha256

%autosetup -p1

%build
%configure --disable-static
%make_build
# Docs already shipped in jq's tarball.
# In order to build the manual page, it
# is necessary to install rake, rubygem-ronn
# and do the following steps:
#
# # yum install rake rubygem-ronn
# $ cd docs/
# $ curl -L https://get.rvm.io | bash -s stable --ruby=1.9.3
# $ source $HOME/.rvm/scripts/rvm
# $ bundle install
# $ cd ..
# $ ./configure
# $ make real_docs

%install
%make_install
find %{buildroot} -name '*.la' -delete
rm -f %{buildroot}%{_docdir}/%{name}/COPYING

%if %{with check}
%check
# Valgrind used, so restrict architectures for check
%ifarch x86_64
make check
%endif
%endif

%files
%license COPYING
%doc AUTHORS NEWS.md README.md
%{_bindir}/%{name}
%{_libdir}/libjq.so.*
%{_datadir}/man/man1/jq.1.gz

%files devel
%{_includedir}/jq.h
%{_includedir}/jv.h
%{_libdir}/libjq.so
%{_libdir}/pkgconfig/libjq.pc

