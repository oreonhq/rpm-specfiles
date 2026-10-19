%global source0_hash 8a58af5b6141319287c1883bec8bd1bd545b7567b7fc5e6ce5d25a1c85f36397
%global source1_hash 28c840e27a375675d756ace75fad49efeffb66e9620a271492067a8bebdbd8b2
Summary:        Command-line tools and library for transforming PDF files
Name:    qpdf
Version: 12.4.2
Release:        1%{?dist}
License: Apache-2.0 OR Artistic-2.0
URL:     https://qpdf.sourceforge.io/
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}-doc.zip
Patch1:  qpdf-relax.patch
Patch1000: qpdf-s390x-disable-tests-zlib.patch
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gnutls-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  unzip
BuildRequires:  zlib-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}%{bash_completions_dir}
mkdir -p %{buildroot}%{zsh_completions_dir}
install -m 0644 completions/bash/qpdf %{buildroot}%{bash_completions_dir}/qpdf
install -m 0644 completions/zsh/_qpdf %{buildroot}%{zsh_completions_dir}/_qpdf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n qpdf-libs -f %{oreon_filedir}/qpdf-libs.list
%files -n qpdf-devel -f %{oreon_filedir}/qpdf-devel.list
%files -n qpdf-doc -f %{oreon_filedir}/qpdf-doc.list

%changelog

%autochangelog
