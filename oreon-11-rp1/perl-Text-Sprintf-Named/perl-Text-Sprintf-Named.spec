%global source0_hash 9b470d78ffcfc40ab3f998231b336b9d3417230fb7ce55b47cd7b05573a70ffc

Name:           perl-Text-Sprintf-Named
Version:        0.0405
Release:        15%{?dist}
Summary:        Sprintf-like function with named conversions
License:        MIT
URL:            https://metacpan.org/release/Text-Sprintf-Named
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Text-Sprintf-Named-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build) >= 0.36
BuildRequires:  perl(strict)
# Test::Run::CmdLine::Iface not used
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(parent)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings::register)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn) >= 0.21

%description
Text::Sprintf::Named provides a sprintf equivalent with named conversions.
Named conversions are sprintf field specifiers (like "%%s" or "%%4d") only
they are associated with the key of an associative array of parameters. So
for example "%%(name)s" will emit the 'name' parameter as a string, and
"%%(num)4d" will emit the 'num' parameter as a variable with a width of 4.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Sprintf-Named-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
