%if 0%{?rhel} > 0
# On RHEL we default to building WITHOUT documentation.
%bcond_with documentation
%else
# Default to building WITH documentation.
%bcond_without documentation
%endif

Summary: A portable x86 assembler which uses Intel-like syntax
Name: nasm
Version: 3.01
Release: 2%{?dist}
License: BSD-2-Clause
URL: http://www.nasm.us
Source0: https://www.nasm.us/pub/nasm/releasebuilds/%{version}/%{name}-%{version}.tar.xz
Source1: https://www.nasm.us/pub/nasm/releasebuilds/%{version}/%{name}-%{version}-xdoc.tar.xz

BuildRequires: perl(Env)
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: asciidoc
BuildRequires: xmlto
BuildRequires: gcc
BuildRequires: make
Obsoletes: nasm-rdoff < 2.16.01-1

%if %{with documentation}
%package doc
Summary: Documentation for NASM
BuildRequires: perl(Font::TTF::Font)
BuildRequires: perl(Sort::Versions)
BuildRequires: perl(File::Spec)
BuildRequires: perl(sort)
BuildRequires: adobe-source-sans-pro-fonts
BuildRequires: adobe-source-code-pro-fonts
BuildRequires: ghostscript
BuildArch: noarch
# For arch to noarch conversion
Obsoletes: %{name}-doc < %{version}-%{release}
%endif

%description
NASM is the Netwide Assembler, a free portable assembler for the Intel
80x86 microprocessor series, using primarily the traditional Intel
instruction mnemonics and syntax.

%if %{with documentation}
%description doc
This package contains documentation for the Netwide Assembler (NASM),
in HTML, PDF, PostScript, and text formats.
%endif

%prep
%autosetup -p1

tar xJf %{SOURCE1} --strip-components 1

%build
%configure
%if %{with documentation}
make everything %{?_smp_mflags}
gzip -9f doc/nasmdoc.{ps,txt}
%else
make all %{?_smp_mflags}
%endif

%install
%make_install

%check
make -C test golden test diff

%files
%license LICENSE
%doc AUTHORS CHANGES README.md
%{_bindir}/nasm
%{_bindir}/ndisasm
%{_mandir}/man1/nasm*
%{_mandir}/man1/ndisasm*

%if %{with documentation}
%files doc
%doc doc/html doc/nasmdoc.txt.gz doc/nasmdoc.ps.gz doc/nasmdoc.pdf
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.01-2
- Prepare for Oreon 11 (RP1)
