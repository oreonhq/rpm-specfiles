Summary: Command-line tools and library for transforming PDF files
Name:    qpdf
Version: 12.3.2
Release: 1%{?dist}
# MIT: e.g. libqpdf/sha2.c, but those are not compiled in (GNUTLS is used)
# upstream uses ASL 2.0 now, but he allowed other to distribute qpdf under
# old license (see README)
License: Apache-2.0 OR Artistic-2.0
URL:     https://qpdf.sourceforge.io/
Source0: https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1: https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}-doc.zip

# make qpdf working under FIPS, downstream patch
Patch1:  qpdf-relax.patch

# zlib/zlib-ng has different behavior for inflate/deflate errors
# on s390x
# it might be fixed upstream in qpdf once it migrates to zlib-ng...
Patch1000: qpdf-s390x-disable-tests-zlib.patch
# oreon url source checksums begin
%global source0_sha256 6cba2f9f2cd887d905faeb99e0e51a307b217920d1bbf3e9cfbb2e8178a2deda
%global source0_file qpdf-12.3.2.tar.gz
%global source1_sha256 92061b323cd1ee76fa33a052a91c7c43bc211772085c374b4135aada24fe9135
%global source1_file qpdf-12.3.2-doc.zip
# oreon url source checksums end


# gcc and gcc-c++ are no longer in buildroot by default
# gcc is needed for qpdf-ctest.c
BuildRequires: gcc
# gcc-c++ is need for everything except for qpdf-ctest
BuildRequires: gcc-c++
# uses cmake
BuildRequires: cmake

BuildRequires: zlib-devel
BuildRequires: libjpeg-turbo-devel

# for gnutls crypto
BuildRequires: gnutls-devel

# for fix-qdf and test suite
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Carp)
BuildRequires: perl(Config)
BuildRequires: perl(constant)
BuildRequires: perl(Cwd)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Digest::SHA)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Compare)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Spec)
BuildRequires: perl(FileHandle)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(IO::Select)
BuildRequires: perl(IO::Socket)
BuildRequires: perl(POSIX)
BuildRequires: perl(strict)
# perl(Term::ANSIColor) - not needed for tests
# perl(Term::ReadKey) - not needed for tests

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%package libs
Summary: QPDF library for transforming PDF files

%package devel
Summary: Development files for QPDF library
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%package doc
Summary: QPDF Manual
BuildArch: noarch
BuildRequires: unzip
Requires: %{name}-libs = %{version}-%{release}

%description
QPDF is a command-line program that does structural, content-preserving
transformations on PDF files. It could have been called something
like pdf-to-pdf. It includes support for merging and splitting PDFs
and to manipulate the list of pages in a PDF file. It is not a PDF viewer
or a program capable of converting PDF into other formats.

%description libs
QPDF is a C++ library that inspect and manipulate the structure of PDF files.
It can encrypt and linearize files, expose the internals of a PDF file,
and do many other operations useful to PDF developers.

%description devel
Header files and libraries necessary
for developing programs using the QPDF library.

%description doc
QPDF Manual

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/qpdf-12.3.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6cba2f9f2cd887d905faeb99e0e51a307b217920d1bbf3e9cfbb2e8178a2deda" || { echo "oreon: Source0 SHA256 mismatch for qpdf-12.3.2.tar.gz" >&2; exit 1; })
%(f=%{_sourcedir}/qpdf-12.3.2-doc.zip; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "92061b323cd1ee76fa33a052a91c7c43bc211772085c374b4135aada24fe9135" || { echo "oreon: Source1 SHA256 mismatch for qpdf-12.3.2-doc.zip" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%patch -P 1 -p1 -b .relax

%ifarch s390x
%patch -P 1000 -p1 -b .s390x-disable-tests-zlib
%endif

# unpack zip file with manual
unzip %{SOURCE1}


%build
%cmake -DBUILD_STATIC_LIBS=0 \
       -DREQUIRE_CRYPTO_GNUTLS=1 \
       -DUSE_IMPLICIT_CRYPTO=0 \
       -DSHOW_FAILED_TEST_OUTPUT=1

%cmake_build

%install
%cmake_install

install -m 0644 %{name}-%{version}-doc/%{name}-manual.pdf %{buildroot}/%{_pkgdocdir}/%{name}-manual.pdf

# install bash/zsh completions
mkdir -p %{buildroot}%{bash_completions_dir}
mkdir -p %{buildroot}%{zsh_completions_dir}
install -m 0644 completions/bash/qpdf %{buildroot}%{bash_completions_dir}/qpdf
install -m 0644 completions/zsh/_qpdf %{buildroot}%{zsh_completions_dir}/_qpdf

%check
%ctest

%ldconfig_scriptlets libs

%files
%{_bindir}/fix-qdf
%{_bindir}/qpdf
%{_bindir}/zlib-flate
%{_mandir}/man1/fix-qdf.1.gz
%{_mandir}/man1/qpdf.1.gz
%{_mandir}/man1/zlib-flate.1.gz
%dir %{bash_completions_dir}
%{bash_completions_dir}/qpdf
%dir %{zsh_completions_dir}
%{zsh_completions_dir}/_qpdf

%files libs
%doc README.md TODO.md ChangeLog
%license Artistic-2.0 LICENSE.txt NOTICE.md
%{_libdir}/libqpdf.so.30
%{_libdir}/libqpdf.so.30.*

%files devel
%doc examples/*.cc examples/*.c
%{_includedir}/qpdf/
%{_libdir}/libqpdf.so
%{_libdir}/pkgconfig/libqpdf.pc
%{_libdir}/cmake/qpdf/

%files doc
%{_pkgdocdir}


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 12.3.2-1
- Prepare for Oreon 11 (RP1)
