%global source0_hash 10ae135a8f72d399501166bc697a3b300fb739a6614aa54408e4e08bec1e91dc

Name:       perl-Net-UPnP
Version:    1.4.6
Epoch:      1
Release:    22%{?dist}
Summary:    Perl extension for UPnP
# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
URL:        https://metacpan.org/release/Net-UPnP
Source0:    https://cpan.metacpan.org/authors/id/S/SK/SKONNO/Net-UPnP-%{version}.tar.gz
BuildArch:  noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
# Socket not used at tests
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
# Tests:
BuildRequires:  perl(Test::More)

%description
This package provides some functions to control UPnP devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-UPnP-%{version}
# Fix file attributes
find -name '*.pm' -exec chmod a-x '{}' +

# Fix shebangs
for file in examples/*.pl; do
    sed '1 s|^#!/usr/bin/env perl|%(perl -MConfig -e 'print $Config{startperl}')|g' \
        "$file" > "${file}.mod" && \
    touch -r "$file" "${file}.mod" && \
    mv "${file}.mod" "$file"
done

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc AUTHORS Changes README examples/
%{perl_vendorlib}/Net/
%{_mandir}/man3/Net::UPnP*

%changelog
%autochangelog
