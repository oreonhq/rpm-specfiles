%global source0_hash 083d80a9e6abf6cd02c29f22cf101f7e1b94a85fe1bf31dbeb152f76caca5183

Name:           perl-Devel-MAT
Version:        0.54
Release:        1%{?dist}
Summary:        Perl Memory Analysis Tool
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Devel-MAT
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Devel-MAT-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build) >= 0.4004
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Commandable::Invocation) >= 0.04
BuildRequires:  perl(Devel::MAT::Dumper) >= 0.48
BuildRequires:  perl(Feature::Compat::Try)
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Heap)
BuildRequires:  perl(List::Util) >= 1.44
BuildRequires:  perl(List::UtilsBy)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(String::Tagged) >= 0.15
BuildRequires:  perl(String::Tagged::Terminal) >= 0.03
BuildRequires:  perl(Struct::Dumb) >= 0.07
BuildRequires:  perl(Syntax::Keyword::Match)
BuildRequires:  perl(Test2::V0)

%{?perl_default_filter}

Provides:       perl(Devel::MAT)
Provides:       perl(Devel::MAT::Cmd::Terminal)
Provides:       perl(Devel::MAT::Context)
Provides:       perl(Devel::MAT::Context::EVAL)
Provides:       perl(Devel::MAT::Context::SUB)
Provides:       perl(Devel::MAT::Context::TRY)
Provides:       perl(Devel::MAT::Dumpfile)
Provides:       perl(Devel::MAT::Graph)
Provides:       perl(Devel::MAT::Graph::Node)
Provides:       perl(Devel::MAT::InternalTools)
Provides:       perl(Devel::MAT::SV)
Provides:       perl(Devel::MAT::SV::ARRAY)
Provides:       perl(Devel::MAT::SV::BOOL)
Provides:       perl(Devel::MAT::SV::CLASS)
Provides:       perl(Devel::MAT::SV::CODE)
Provides:       perl(Devel::MAT::SV::C_STRUCT)
Provides:       perl(Devel::MAT::SV::FORMAT)
Provides:       perl(Devel::MAT::SV::GLOB)
Provides:       perl(Devel::MAT::SV::HASH)
Provides:       perl(Devel::MAT::SV::INVLIST)
Provides:       perl(Devel::MAT::SV::IO)
Provides:       perl(Devel::MAT::SV::Immortal)
Provides:       perl(Devel::MAT::SV::LVALUE)
Provides:       perl(Devel::MAT::SV::NO)
Provides:       perl(Devel::MAT::SV::OBJECT)
Provides:       perl(Devel::MAT::SV::PAD)
Provides:       perl(Devel::MAT::SV::PADLIST)
Provides:       perl(Devel::MAT::SV::PADNAMES)
Provides:       perl(Devel::MAT::SV::REF)
Provides:       perl(Devel::MAT::SV::REGEXP)
Provides:       perl(Devel::MAT::SV::SCALAR)
Provides:       perl(Devel::MAT::SV::STASH)
Provides:       perl(Devel::MAT::SV::UNDEF)
Provides:       perl(Devel::MAT::SV::Unknown)
Provides:       perl(Devel::MAT::SV::YES)
Provides:       perl(Devel::MAT::Tool)
Provides:       perl(Devel::MAT::Tool::Callers)
Provides:       perl(Devel::MAT::Tool::Count)
Provides:       perl(Devel::MAT::Tool::Find)
Provides:       perl(Devel::MAT::Tool::Identify)
Provides:       perl(Devel::MAT::Tool::Inrefs)
Provides:       perl(Devel::MAT::Tool::ListDanglingPtrs)
Provides:       perl(Devel::MAT::Tool::Outrefs)
Provides:       perl(Devel::MAT::Tool::Reachability)
Provides:       perl(Devel::MAT::Tool::Roots)
Provides:       perl(Devel::MAT::Tool::Show)
Provides:       perl(Devel::MAT::Tool::Sizes)
Provides:       perl(Devel::MAT::Tool::Stack)
Provides:       perl(Devel::MAT::Tool::Strtab)
Provides:       perl(Devel::MAT::Tool::Summary)
Provides:       perl(Devel::MAT::Tool::Symbols)
Provides:       perl(Devel::MAT::Tool::Tools)
Provides:       perl(Devel::MAT::Tool::help)
Provides:       perl(Devel::MAT::Tool::more)
Provides:       perl(Devel::MAT::Tool::stop)
Provides:       perl(Devel::MAT::Tool::time)
Provides:       perl(Devel::MAT::ToolBase::GraphWalker)

%description
Perl Memory Analysis Tool for inspecting heap dump files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Devel-MAT-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
/usr/bin/find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README doc
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Devel*
%{perl_vendorlib}/Devel*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_datadir}/perl5/*

%changelog
%autochangelog
