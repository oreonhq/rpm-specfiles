%global source0_hash ed98c7a7f1d5a4148b02fef1b16aee4a6a6d8658d01a80cf5c503015ef01afa5
%global _smp_build_ncpus 1
Name:           regina-rexx
Version:        3.9.6
Release:        1%{?dist}
Summary:        Regina Rexx Interpreter
License:        LGPL-2.0-only and LGPL-2.0-or-later and LGPL-2.1-or-later and MPL-1.0 and GPL-2.0-or-later and BSD-4-Clause and Unlicense
URL:            https://regina-rexx.sourceforge.io
Source0:        https://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  sed
BuildRequires:  systemd-devel
# /oreon:deps
%description
Regina is a Rexx interpreter that has been ported to most Unix platforms and
operating systems. Rexx is a programming language that was designed to be easy
to use for inexperienced programmers yet powerful enough for experienced users.
It is also a language ideally suited as a macro language for other applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        libs
Summary:        Shared libraries for %{name}
%description    libs
The %{name}-libs package contains shared libraries for %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains additional documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Do not strip on install
sed -i Makefile.in -e 's:$(INSTALL) -s:$(INSTALL):g'
# Fix permissions
chmod -x BUGS
# Fix encoding
iconv -f iso8859-1 -t utf-8 README.38 > README.38.conv && mv -f README.38.conv README.38
# Fix scripts shebangs
sed -i 's:/usr/bin/env regina:/usr/bin/regina:' demo/*.rexx regutil/*.rexx

%build

export CFLAGS="%{build_cflags} -std=gnu17"
%configure
%make_build
%install
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mkdir -p %{buildroot}%{_libdir}/%{name}/%{version}
%make_install
install -Dpm0644 -t %{buildroot}%{_unitdir} rxstack.service
rm %{buildroot}%{_libdir}/libregina.a
mv %{buildroot}%{_datadir}/%{name}/examples .
ln -sf regina.1.gz %{buildroot}%{_mandir}/man1/rexx.1.gz
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post rxstack.service
%preun

%systemd_preun rxstack.service
%postun

%systemd_postun_with_restart rxstack.service
%files -f %{oreon_filedir}/main.list
%files -n regina-rexx-devel -f %{oreon_filedir}/regina-rexx-devel.list
%files -n regina-rexx-libs -f %{oreon_filedir}/regina-rexx-libs.list
%files -n regina-rexx-doc -f %{oreon_filedir}/regina-rexx-doc.list

%changelog

%autochangelog
