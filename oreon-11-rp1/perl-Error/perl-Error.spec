Name:           perl-Error
Epoch:          1
Version:        0.17030
Release:        3%{?dist}
Summary:        Error/exception handling in an OO-ish way
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND X11
URL:            https://metacpan.org/release/Error
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Error-0.17030.tar.gz
# oreon url source checksums begin
%global source0_sha256 34d382276c0fb0d6b38355b94c96a30b12d834d5662eb53f088ee25e3e712924
%global source0_file Error-0.17030.tar.gz
# oreon url source checksums end

BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Dependencies
Requires:       perl(Carp)

# Avoid provides/requires from examples
%global __provides_exclude_from ^%{_docdir}
%global __requires_exclude_from ^%{_docdir}

%description
The Error package provides two interfaces. Firstly Error provides a
procedural interface to exception handling. Secondly Error is a base class
for errors/exceptions that can either be thrown, for subsequent catch, or
can simply be recorded.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Error-0.17030.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "34d382276c0fb0d6b38355b94c96a30b12d834d5662eb53f088ee25e3e712924" || { echo "oreon: Source0 SHA256 mismatch for Error-0.17030.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Error-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
# GPL-1.0-or-later OR Artistic-1.0-Perl
%doc ChangeLog Changes README examples/
%{perl_vendorlib}/Error.pm
%{_mandir}/man3/Error.3*
# X11
%{perl_vendorlib}/Error/
%{_mandir}/man3/Error::Simple.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.17030-3
- Prepare for Oreon 11 (RP1)
