%global source0_hash d49bf295cb46a1cc94ec9d2f9051171e390e560dfaea1cd06ae852194d6fc259

%global src_name GitLab-API-v4

Name:           perl-%{src_name}
Version:        0.27
Release:        9%{?dist}
Summary:        Complete GitLab API v4 client

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{src_name}

# Doesn't work.  :(
# Source0:      https://www.cpan.org/modules/by-module/GitLab/%%{src_name}-%%{version}.tar.gz
Source0:        https://cpan.metacpan.org/authors/id/B/BL/BLUEFEET/%{src_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Const::Fast)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(HTTP::Tiny::Multipart)
BuildRequires:  perl(IO::Prompter)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Log::Any::Adapter)
BuildRequires:  perl(Log::Any::Adapter::Screen)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Moo)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test2::Require::AuthorTesting)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Types::Common::Numeric)
BuildRequires:  perl(Types::Common::String)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(strictures) >= 2

%description
This module provides a one-to-one interface with the GitLab API v4.
Much is not documented here as it would just be duplicating GitLab's
own API Documentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{src_name}-%{version} -p 1

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man*/*

%changelog
%autochangelog
