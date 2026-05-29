%global source0_hash f9145054ae131973c61208ea82486d5dd10e3c5cdad23b7c4a0617743c8f5a18

%if 0%{?fedora:1} || 0%{?oreon}
%bcond_without oniguruma
%else
%bcond_with oniguruma
%endif

Summary:	Shared library for the S-Lang extension language
Name:		slang
Version:	2.3.3
Release:	9%{?dist}
License:	GPL-2.0-or-later
URL:		https://www.jedsoft.org/slang/
Source:        https://www.jedsoft.org/releases/slang/slang-2.3.3.tar.bz2
# disable test that fails with SIGHUP ignored (e.g. in koji)
Patch2:		slang-sighuptest.patch
BuildRequires: make
BuildRequires:	gcc libpng-devel zlib-devel
%{?with_oniguruma:BuildRequires: oniguruma-devel}
# static removed in 2.3.1a-3
Obsoletes:	 slang-static < 2.3.1a-3

%description
S-Lang is an interpreted language and a programming library.  The
S-Lang language was designed so that it can be easily embedded into
a program to provide the program with a powerful extension language.
The S-Lang library, provided in this package, provides the S-Lang
extension language.  S-Lang's syntax resembles C, which makes it easy
to recode S-Lang procedures in C if you need to.

%package slsh
Summary:	Interpreter for S-Lang scripts
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description slsh
slsh (slang-shell) is a program for interpreting S-Lang scripts. 
It supports dynamic loading of S-Lang modules and includes a readline
interface for interactive use.

This package also includes S-Lang modules that are distributed with
the S-Lang distribution.

%package devel
Summary:	Development files for the S-Lang extension language
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains files which you'll need if you want to
develop S-Lang based applications.  Documentation which may help
you write S-Lang based applications is also included.

Install the slang-devel package if you want to develop applications
based on the S-Lang extension language.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
%patch -P2 -p1 -b .sighuptest

%build
%configure \
	--with-{png,z}lib=%{_libdir} \
	--with-{png,z}inc=%{_includedir} \
	--without-pcre \
%if %{with oniguruma}
	--with-oniglib=%{_libdir} \
	--with-oniginc=%{_includedir} \
%else
	--without-onig \
%endif
;

# fails with %%{?_smp_mflags}
# install_doc_dir sets SLANG_DOC_DIR macro
make RPATH="" install_doc_dir=%{_pkgdocdir} all

%install
make install-all INSTALL="install -p" RPATH="" DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_docdir}/{slang,slsh}
rm -f $RPM_BUILD_ROOT%{_libdir}/libslang.a

mkdir $RPM_BUILD_ROOT%{_includedir}/slang
for h in slang.h slcurses.h; do
	ln -s ../$h $RPM_BUILD_ROOT%{_includedir}/slang/$h
done

%check
make check

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS
%{_libdir}/libslang*.so.2*

%files slsh
%doc slsh/doc/html/slsh*.html
%config(noreplace) %{_sysconfdir}/slsh.rc
%{_bindir}/slsh
%{_libdir}/slang
%{_mandir}/man1/slsh.1*
%{_datadir}/slsh

%files devel
%doc doc/*/cslang*.txt doc/*/cref.txt doc/README doc/*/slang*.txt doc/*.txt
%{_libdir}/libslang*.so
%{_libdir}/pkgconfig/slang.pc
%{_includedir}/sl*.h
%{_includedir}/slang

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.3-9
- Import
