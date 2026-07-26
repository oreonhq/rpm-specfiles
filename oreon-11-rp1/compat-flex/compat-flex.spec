%global source0_hash df53d6b73cb695c24e5edb7c846f5f684513743dedcd73d9e5199303d65686dc

Summary: Legacy version of flex, a tool for creating scanners
Name: compat-flex
Version: 2.5.4a
Release: 33%{?dist}
License: BSD
URL: http://www.gnu.org/software/flex/
Source: http://downloads.sourceforge.net/flex/flex-%{version}.tar.bz2
Source2: README.fedora
Patch0: flex-2.5.4a-skel.patch
Patch1: flex-2.5.4-glibc22.patch
Patch2: flex-2.5.4a-gcc3.patch
Patch3: flex-2.5.4a-gcc31.patch
Patch4: flex-2.5.4a2.patch
Patch5: flex-pic.patch
Patch6: flex-2.5.4a2-std.patch
Patch7: flex-2.5.4a2-warn.patch
Patch8: flex-2.5.4a2-shapwarn.patch
Patch9: flex-2.5.4a2-iniscan.patch
Patch10: flex-2.5.4a-Makefile.in.patch
Patch11: flex-2.5.4a-texinfo-section.patch
BuildRequires:  gcc
BuildRequires: autoconf byacc texinfo info
BuildRequires: make

%description

This is legacy version of flex, a program that generates scanners.
Scanners are programs which can recognize lexical patterns in text.
Flex takes pairs of regular expressions and C code as input and
generates a C source file as output.  The output file is compiled and
linked with a library to produce an executable.  The executable
searches through its input for occurrences of the regular expressions.
When a match is found, it executes the corresponding C code.  Flex was
designed to work with both Yacc and Bison, and is used by many
programs as part of their build process.

You should install flex if you are going to use your system for
application development.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n flex-2.5.4
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
#%patch9 -p1
%patch -P10 -p1
%patch -P11 -p1
cp %{SOURCE2} .

%build
autoconf
%configure
sed -i '/^START-INFO-DIR-ENTRY/,/^END-INFO-DIR-ENTRY/s/[Ff]lex/&-%{version}/g' ./MISC/texinfo/flex.texi
make FLEX=flex-%{version}
makeinfo MISC/texinfo/flex.texi -o MISC/texinfo/flex-%{version}.info

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall} FLEX=flex-%{version} libdir=$RPM_BUILD_ROOT/%{_libdir}/flex-%{version} mandir=$RPM_BUILD_ROOT/%{_mandir}/man1
./mkinstalldirs $RPM_BUILD_ROOT/%{_infodir} $RPM_BUILD_ROOT/%{_includedir}/flex-%{version}
install -m 644 MISC/texinfo/flex-%{version}.info $RPM_BUILD_ROOT/%{_infodir}/flex-%{version}.info
mv ${RPM_BUILD_ROOT}/%{_includedir}/FlexLexer.h ${RPM_BUILD_ROOT}/%{_includedir}/flex-%{version}/FlexLexer.h
ln -s flex-%{version}.1 ${RPM_BUILD_ROOT}/%{_mandir}/man1/flex-%{version}++.1

%check
echo ============TESTING===============
make FLEX=flex-%{version} bigcheck
echo ============END TESTING===========

%files
%doc COPYING NEWS README README.fedora
%{_bindir}/*
%{_mandir}/man1/*
%{_libdir}/flex-%{version}
%{_includedir}/flex-%{version}
%{_infodir}/flex-%{version}.info*

%changelog
%autochangelog
