%global source0_hash 62f72c191b2b5ee55842a926fdec8c630ee663b32f0195644c45e435699bf03b

Name:           perl-Hijk
Version:        0.28
Release:        21%{?dist}
Summary:        Specialized HTTP client
License:        MIT

URL:            https://metacpan.org/release/Hijk
Source0:        https://cpan.metacpan.org/authors/id/G/GU/GUGOD/Hijk-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build::Tiny)
# runtime requirements
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(base)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Net::Ping)
BuildRequires:  perl(Net::Server::HTTP)
BuildRequires:  perl(Plack::Runner)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)

%{?perl_default_filter}

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

%check
./Build test

%files
%doc Changes README.md examples
%license LICENSE
%{perl_vendorlib}/Hijk*
%{_mandir}/man3/Hijk*

%changelog
%autochangelog
