%global source0_hash fe69b76899afe90b8ae5b82de2aaa7575ada908937f4485b80aaef317563e99f

Name:           perl-Apache-Session
Version:        1.94
Release:        16%{?dist}
Summary:        Persistence framework for session data
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Apache-Session
Source0:        https://cpan.metacpan.org/modules/by-module/Apache/Apache-Session-%{version}.tar.gz
# https://bugzilla.redhat.com/bugzilla/attachment.cgi?id=118577, from Chris Grau
Patch0:         Apache-Session-mp2.patch
BuildArch:      noarch
# Build
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI::Cookie)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(DB_File)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IPC::Semaphore)
BuildRequires:  perl(IPC::SysV)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
# mod_perl interaction
# mod_perl won't work properly in recent Fedora/EL releases (https://bugzilla.redhat.com/show_bug.cgi?id=2030601#c2)
%if (0%{?rhel} && 0%{?rhel} <= 8) || (0%{?fedora} && 0%{?fedora} <= 35)
BuildRequires:  perl(Apache)
BuildRequires:  perl(Apache2::RequestUtil)
%endif
# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBD::mysql)
# Not available in Fedora yet; tests skipped automatically
%if 0
BuildRequires:  perl(DBD::Oracle)
%endif
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(File::Temp)
%if 0%{?fedora}
BuildRequires:  perl(Test::Database)
%endif
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.41

%description
Apache::Session is a persistence framework that is particularly useful for
tracking session data between httpd requests. Apache::Session is designed
to work with Apache and mod_perl, but it should work under CGI and other
web servers, and it also works outside of a web server altogether.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Apache-Session-%{version}
find -type f -exec perl -pi -e 's/\r//g' {} +

# Workaround for mod_perl 2.x compatibility (CPAN RT#14504)
%patch -P0 -p1

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc CHANGES Contributing.txt README TODO
%doc eg/
%{perl_vendorlib}/Apache/
%{_mandir}/man3/Apache::Session*

%changelog
%autochangelog
