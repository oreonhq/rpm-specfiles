%global source0_hash none

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

%global	baserelease	4

Name:		oniguruma
Version:	%{mainver}%{?postver:.%postver}%{?gitversion:^%{?gitversion}}
Release:	%{?prerelease:0.}%{baserelease}%{?dist}
Summary:	Regular expressions library

# SPDX confirmed
License:	BSD-2-Clause
URL:		https://github.com/kkos/oniguruma/
Source0:	https://github.com/kkos/oniguruma/releases/download/v%{mainver}%{?betaver:_%betaver}/onig-%{mainver}%{?postver:.%postver}%{?betaver:-%betaver}%{?gitversion:-%{?gitversion}}.tar.gz
Source1:	create-tarball-from-git.sh

BuildRequires:	make
BuildRequires:	gcc
%if 0%{?git_snapshot}
BuildRequires:  automake
BuildRequires:  libtool
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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{mainver}%{?postver:.%postver}%{?gitversion:^%{?gitversion}}-1
- Prepare for Oreon 11 (RP1)
