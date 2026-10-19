%global source0_hash a78abbdca393cd6843373d2172572380dcaa59ead27738c8a3b06009de0c3db0
Name: sparse
Version: 0.6.4
%define rcver gce1a6720f69e
%if "x%{?rcver}" != "x"
%define build_ver       %{version}-%{rcver}
%define dotrc           .%{rcver}
%else
%define build_ver       %{version}
%define dotrc           %{nil}
%endif
Release:        1%{?dist}
Summary:        A semantic parser of source files
License:    MIT
URL:        https://sparse.wiki.kernel.org
Source0:        https://www.kernel.org/pub/software/devel/%{name}/dist/%{name}-%{build_ver}.tar.xz
Patch0:	    0001-linearize.c-fix-buffer-overrun-warning-from-fortify.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  sqlite-devel
# /oreon:deps
%description
Sparse is a semantic parser of source files: it's neither a compiler
(although it could be used as a front-end for one) nor is it a
preprocessor (although it contains as a part of it a preprocessing
phase).

It is meant to be a small - and simple - library.  Scanty and meager,
and partly because of that easy to use.  It has one mission in life:
create a semantic parse tree for some arbitrary user for further
analysis.  It's not a tokenizer, nor is it some generic context-free
parser.  In fact, context (semantics) is what it's all about - figuring
out not just what the grouping of tokens are, but what the _types_ are
that the grouping implies.

Sparse is primarily used in the development and debugging of the Linux kernel.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n sparse-%{build_ver}

%build

%define make_destdir \
make DESTDIR="%{buildroot}" PREFIX="%{_prefix}" \\\
     BINDIR="%{_bindir}" LIBDIR="%{_libdir}" \\\
     INCLUDEDIR="%{_includedir}" PKGCONFIGDIR="%{_libdir}/pkgconfig"
%make_destdir %{?_smp_mflags} CFLAGS="%{optflags}" HAVE_LLVM=no
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
%make_destdir install HAVE_LLVM=no
%oreon_autofiles main

%check

make check HAVE_LLVM=no
%clean
rm -rf %{buildroot}
make clean
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
