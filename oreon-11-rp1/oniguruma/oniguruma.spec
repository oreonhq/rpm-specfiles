%global source0_hash 2a5cfc5ae259e4e97f86b68dfffc152cdaffe94e2060b770cb827238d769fc05
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
%global	baserelease	4
Name:		oniguruma
Version:	%{mainver}%{?postver:.%postver}%{?gitversion:^%{?gitversion}}
Release:        1%{?dist}
Summary:        Regular expressions library
License:	BSD-2-Clause
URL:		https://github.com/kkos/oniguruma/
Source0:        https://github.com/kkos/%{name}/releases/download/v%{mainver}/onig-%{mainver}.tar.gz
Source1:	create-tarball-from-git.sh
%if 0%{?git_snapshot}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n onig-%{mainver}%{?gitversion:-%{?gitversion}}
%{__sed} -i.multilib -e 's|-L@libdir@||' onig-config.in

%build

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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{__make} check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n oniguruma-devel -f %{oreon_filedir}/oniguruma-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{mainver}%{?postver:.%postver}%{?gitversion:^%{?gitversion}}-1
- Prepare for Oreon 11 (RP1)
