%global source0_hash dd7a047b9ce28e92ed157fe9c9df6f0131a419548df05e55f0d5da92c5aca29f
Summary:        Parser Generator with Java Extension
Name:           byaccj
Version:        1.15
Release:        1%{?dist}
License:        LicenseRef-Public-Domain
URL:            http://byaccj.sourceforge.net/
Source0:        https://sourceforge.net/projects/byaccj/files/byaccj/1.15/byaccj1.15_src.tar.gz#/byaccj-1.15.tar.gz
Patch:        byaccj-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl-constant
BuildRequires:  perl-interpreter
# /oreon:deps
%description
BYACC/J is an extension of the Berkeley v 1.8 YACC-compatible 
parser generator. Standard YACC takes a YACC source file, and 
generates one or more C files from it, which if compiled properly, 
will produce a LALR-grammar parser. This is useful for expression 
parsing, interactive command parsing, and file reading. Many 
megabytes of YACC code have been written over the years.
This is the standard YACC tool that is in use every day to produce 
C/C++ parsers. I have added a "-J" flag which will cause BYACC to 
generate Java source code, instead. So there finally is a YACC for 
Java now! 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n byaccj1.15
%patch 0 -p1
chmod -c -x src/* docs/*
sed -i -e 's|-arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk -mmacosx-version-min=10.4|$(LDFLAGS)|g' src/Makefile

%build

pushd src
%make_build yacc CFLAGS="%{optflags} -ansi" LDFLAGS="$RPM_LD_FLAGS"
popd
%install
install -d -m 755 %{buildroot}%{_bindir}
install -p -m 755 src/yacc %{buildroot}%{_bindir}/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.15-1
- Import
