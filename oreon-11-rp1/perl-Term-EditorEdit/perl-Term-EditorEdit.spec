%global source0_hash 1af6774e7c686dea23eb89948469b1525ec097486b4ed1d7e8764026ae10fceb

Name:           perl-Term-EditorEdit
Version:        0.0016
Release:        34%{?dist}
Summary:        Edit a document via $EDITOR
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-EditorEdit
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROKR/Term-EditorEdit-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}

BuildRequires:  perl-generators
BuildRequires:  perl(Any::Moose)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Text::Clip)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
Term::EditorEdit is a tool for prompting the user to edit a piece of text
via $VISUAL or $EDITOR and return the result.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Term-EditorEdit-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

# Not useful to be installed
rm $RPM_BUILD_ROOT%{_bindir}/editor-edit

%check
%{__make} test

%files
%doc Changes README bin/editor-edit
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
