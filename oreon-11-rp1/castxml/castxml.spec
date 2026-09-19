%global source0_hash e70728229db5444384befcba9681a01497e9a19e35166ce1ffef3b5cbc8eeefe

%undefine __cmake_in_source_build

Name:		castxml
Version:	0.7.0
Release:	1%{?dist}
Summary:	C-family abstract syntax tree XML output tool

License:	Apache-2.0
URL:		https://github.com/CastXML/CastXML
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	llvm-devel >= 3.6.0
BuildRequires:	clang-devel >= 3.6.0
BuildRequires:	libedit-devel
BuildRequires:	zlib-devel
BuildRequires:	/usr/bin/sphinx-build

%description
Parse C-family source files and optionally write a subset of the
Abstract Syntax Tree (AST) to a representation in XML.

Source files are parsed as complete translation units using the clang
compiler. XML output is enabled by the --castxml-gccxml option and
produces a format close to that of gccxml. Future versions of castxml
may support alternative output formats.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CastXML-%{version}

%build
%cmake -DCastXML_INSTALL_DOC_DIR:STRING=share/doc/%{name} \
       -DCastXML_INSTALL_MAN_DIR:STRING=share/man \
       -DCLANG_RESOURCE_DIR:PATH=$(clang -print-file-name=include)/.. \
       -DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
       -DCLANG_LINK_CLANG_DYLIB:BOOL=ON \
       -DBUILD_TESTING:BOOL=ON \
       -DSPHINX_MAN:BOOL=ON
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_pkgdocdir}/LICENSE
rm %{buildroot}%{_pkgdocdir}/NOTICE

%check
%ctest

%files
%{_bindir}/castxml
%doc %{_mandir}/man1/castxml.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/clang
%{_datadir}/%{name}/detect_vs.c
%{_datadir}/%{name}/detect_vs.cpp
%{_datadir}/%{name}/empty.c
%{_datadir}/%{name}/empty.cpp
%license LICENSE NOTICE

%changelog
%autochangelog
