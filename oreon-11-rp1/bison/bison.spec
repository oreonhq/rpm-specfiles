%global source0_hash 9bba0214ccf7f1079c5d59210045227bcf619519840ebfa80cd3849cff5a5bf2
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: bison
Version: 3.8.2
Release: 1%{?dist}
Summary: GNU Bison, a general-purpose parser generator
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/bison/
Source0: https://ftp.gnu.org/gnu/bison/bison-3.8.2.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: m4
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
GNU Bison is a general-purpose parser generator that converts an annotated context-free grammar into a deterministic LR or generalized LR (GLR) parser employing LALR(1) parser tables. Bison can also generate IELR(1) or canonical LR(1) parser tables. Once you are proficient with Bison, you can use it to develop a wide range of language parsers, from those used in simple desk calculators to complex programming languages.

Bison is upward compatible with Yacc: all properly-written Yacc grammars work with Bison with no change. Anyone familiar with Yacc should be able to use Bison with little trouble. You need to be fluent in C, C++, D or Java programming in order to use Bison.

Bison and the parsers it generates are portable, they do not require any specific compilers.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure
%oreon_make

%install
%oreon_make_install
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING
