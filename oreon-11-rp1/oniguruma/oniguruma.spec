# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2a5cfc5ae259e4e97f86b68dfffc152cdaffe94e2060b770cb827238d769fc05

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
BuildRequires: oreon-rpm-macros
%undefine	_changelog_trimtime

%global git_snapshot 0

%if 0%{?git_snapshot}
%define apply_git_patch git am
%else
%define apply_git_patch patch -p1
%endif

%if 0%{?git_snapshot}
%global         gitdate       20230501
%global         gitcommit     41a3b802af2155eef6d648aa3608e39605110642
%global         shortcommit   %(c=%{gitcommit}; echo ${c:0:7})

%global         gitversion    %{gitdate}git%{shortcommit}
%endif

%global	mainver	6.9.10
#%%global	postver	1
#%%global	betaver	rc4
#%%define	prerelease	1

%global	baserelease	5

Name:		oniguruma
Version:        6.9.10
Release:        1%{?dist}
Summary:	Regular expressions library

# SPDX confirmed
License:	BSD-2-Clause
URL:		https://github.com/kkos/oniguruma/
Source0:        https://github.com/kkos/oniguruma/releases/download/v%{version}/onig-%{version}.tar.gz
Source1:	create-tarball-from-git.sh

BuildRequires:	make
BuildRequires:	gcc
%if 0%{?git_snapshot}
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  oreon-rpm-macros
%endif

%description
Oniguruma is a regular expressions library.
The characteristics of this library is that different character encoding
for every regular expression object can be specified.
(supported APIs: GNU regex, POSIX and Oniguruma native)


%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%oreon_sha256

%setup -q -n onig-%{mainver}%{?gitversion:-%{?gitversion}}
%{__sed} -i.multilib -e 's|-L@libdir@||' onig-config.in

%build
# This package fails its testsuite when compiled with LTO, but the real problem
# is that it ends up mixing and matching regexp bits between itself and glibc.
# Disable LTO
%define _lto_cflags %{nil}

%if 0%{?git_snapshot}
autoreconf -fi
%endif

%configure \
	--enable-posix-api \
	--enable-binary-compatible-posix-api \
	--disable-silent-rules \
	--disable-static \
	--with-rubydir=%{_bindir} \
	%{nil}
%make_build

%install
%make_install

%check
%{__make} check

%ldconfig_scriptlets


%files
%defattr(-,root,root,-)
%doc	AUTHORS
%license	COPYING
%doc	HISTORY
%doc	README.md
%doc	index.html
%lang(ja)	%doc	README_japanese
%lang(ja)	%doc	index_ja.html

%{_libdir}/libonig.so.5*

%files devel
%defattr(-,root,root,-)
%doc	doc/API
%doc	doc/CALLOUTS.API
%doc	doc/CALLOUTS.BUILTIN
%doc	doc/FAQ
%doc	doc/RE
%doc	doc/SYNTAX.md
%doc	doc/UNICODE_PROPERTIES
%lang(ja)	%doc	doc/API.ja
%lang(ja)	%doc	doc/CALLOUTS.API.ja
%lang(ja)	%doc	doc/CALLOUTS.BUILTIN.ja
%lang(ja)	%doc	doc/FAQ.ja
%lang(ja)	%doc	doc/RE.ja

%{_bindir}/onig-config

%{_libdir}/libonig.so
%{_includedir}/onig*.h
%{_libdir}/pkgconfig/%{name}.pc

