%global source0_hash 62f72c191b2b5ee55842a926fdec8c630ee663b32f0195644c45e435699bf03b
Name:           perl-Hijk
Version:        0.28
Release:        21%{?dist}
Summary:        Specialized HTTP client
License:        MIT
URL:            https://metacpan.org/release/Hijk
Source0:        https://cpan.metacpan.org/authors/id/G/GU/GUGOD/Hijk-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Net::Ping)
BuildRequires:  perl(Net::Server::HTTP)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Plack::Runner)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Hijk is a specialized HTTP Client that does nothing but transport the
response body back. It does not feature as a "user agent", but as a dumb
client. It is suitable for connecting to data servers transporting via HTTP
rather then web servers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Hijk-%{version}

%build

%{__perl} Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
