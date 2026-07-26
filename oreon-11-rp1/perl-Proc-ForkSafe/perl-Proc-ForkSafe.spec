%global source0_hash b5af2b65e228d2895fdb571f8202aa8a67cdea86cdf8a35b0bc99bbd823f0217

Name:           perl-Proc-ForkSafe
Version:        0.001
Release:        7%{?dist}
Summary:        Help make objects fork safe
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Proc-ForkSafe
Source0:        https://cpan.metacpan.org/authors/id/S/SK/SKAJI/Proc-ForkSafe-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test::More)

%description
Proc::ForkSafe helps make objects fork safe.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Proc-ForkSafe-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/Proc*
%{_mandir}/man3/Proc::ForkSafe*

%changelog
%autochangelog
