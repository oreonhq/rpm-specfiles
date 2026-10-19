%global source0_hash 87336eba53b4acfe917424ab5d500d2b0054d9f5148d35c2273ccf2cfb712f0d
%global source1_hash 7632368f9eea30bfd438f970e3a534796aecc3783b7b9c9b7a705b93dab0714f
%bcond_without documentation
Summary:        A portable x86 assembler which uses Intel-like syntax
Name: nasm
Version: 3.02
Release:        1%{?dist}
License: BSD-2-Clause
URL: http://www.nasm.us
Source0:        https://www.nasm.us/pub/nasm/releasebuilds/%{version}/%{name}-%{version}.tar.xz
Source1:        https://www.nasm.us/pub/nasm/releasebuilds/%{version}/%{name}-%{version}-xdoc.tar.xz
Obsoletes: nasm-rdoff < 2.16.01-1
%if %{with documentation}
# oreon:deps
BuildRequires:  adobe-source-code-pro-fonts
BuildRequires:  adobe-source-sans-pro-fonts
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  make
BuildRequires:  perl(Env)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Font::TTF::Font)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(sort)
BuildRequires:  xmlto
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make -C test golden test diff
%files -f %{oreon_filedir}/main.list
%files -n nasm-doc -f %{oreon_filedir}/nasm-doc.list

%changelog

%autochangelog
