%global source0_hash 9c2cd3f82e7891877fa43ccbba5d419f39daf9197db2fa3cec86917f414f4c66

%global		repoid	60140
%undefine		_docdir_fmt

Name:			xyzsh
Version:		1.5.8
Release:		31%{?dist}
Summary:		Interactive shell and text processing tool

# LICENSE		MIT
# src/chared.h	BSD-3-Clause
# src/editline/		BSD-3-Clause
# src/editline/chartype.h	BSD-4-Clause
# src/editline/eln.c	BSD-4-Clause
# src/editline/fgetln.c (and some others)	BSD-2-Clause
# src/editline/strlcat.c	HPND
# SPDX confirmed
License:		MIT AND BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND HPND
URL:			http://sourceforge.jp/projects/xyzsh/
Source0:		http://dl.sourceforge.jp/xyzsh/%{repoid}/%{name}-%{version}.tgz
# -Werror=format-security
Patch0:		xyzsh-1.5.8-format.patch
# -Werror=implicit-function-declaration
Patch1:		xyzsh-1.5.8-implicit-function-declaration.patch
# Support -std=gnu23
Patch2:		xyzsh-1.5.8-c23-compat.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:	cmigemo-devel
BuildRequires:	oniguruma-devel
BuildRequires:	libedit-devel

%description
xyzsh is an interactive shell and a text processing tool.
It contains a text processing inner commands like Perl or Ruby, 
and can be used as a simple objective oriented script language.

%package		devel
Summary:		Development files for cmigemo

Requires:		%{name}%{?isa} = %{version}-%{release}

%description	devel
This package  contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Embed soname anyway
SOVER=$(cat configure.in | sed -n -e 's|^SO_VERSION=\([^\.][^\.]*\)\..*$|\1|p')
sed -i.soname \
	-e "/[ \t]/s|\( -o libxyzsh\.so\)| -Wl,-soname,libxyzsh.so.$SOVER \1|" \
	Makefile.in

# Don't strip binary
sed -i.strip -e '/INSTALL/s|-s -m |-m |' Makefile.in

# CRLF line terminators
touch -r README{,.stamp}
sed -i -e 's|\r||g' README
touch -r README{.stamp,}
rm -f README.stamp

# Change docdir
sed -i.docdir \
	-e '/^CFLAGS=.*DATAROOTDIR=/s|doc/xyzsh/|doc/xyzsh-%{version}/|' \
	configure

# Kill -O3
sed -i.optflags \
	-e 's|-O3|-O2|' \
	configure

%build
%configure \
	--with-migemo \
	--with-system-migemodir=%{_datadir}/cmigemo/

make %{?_smp_mflags} -k \
	CC="gcc %optflags -Werror=implicit-function-declaration" \
	docdir=%{_datadir}/doc/%{name}-%{version} \
	libxyzsh.so

make %{?_smp_mflags} -k \
	CC="gcc %optflags -Werror=implicit-function-declaration" \
	docdir=%{_datadir}/doc/%{name}-%{version} \

%install
make install \
	DESTDIR=%{buildroot} \
	INSTALL="install -p" \
	docdir=%{_datadir}/doc/%{name}-%{version}

%ldconfig_scriptlets

%files
%doc	AUTHORS
%doc	CHANGELOG
%license	LICENSE
%doc	README
%lang(ja)	%doc	README.ja
%doc	USAGE
%lang(ja)	%doc	USAGE.ja

%dir	%{_sysconfdir}/%{name}
%config(noreplace)	%{_sysconfdir}/%{name}/*.xyzsh

%{_bindir}/xyzsh
%{_libdir}/libxyzsh.so.2*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/migemo.so
%{_libdir}/%{name}/migemo.xyzsh
%{_mandir}/man1/xyzsh.1*

%files	devel
%{_libdir}/libxyzsh.so
%{_includedir}/%{name}/

%changelog
%autochangelog
