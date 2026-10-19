%global source0_hash a02946b1f2cb34c1c1f971ffaa17e92b909d11a7c5c5491f412629d664e30095
%global commit 590023f6c3289810539b0994fd5c3216d81c9259
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20230714
Name:           public-inbox
Version:        2.0.0~%{?date}git%{?shortcommit}
Release:        1%{?dist}
Summary:        An archives-first approach to mailing lists
License:        AGPL-3.0-or-later
URL:            https://public-inbox.org
Source0:        https://%{name}.org/%{name}.git/snapshot/%{name}-%{commit}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl-PublicInbox = %{version}-%{release}
Requires:       perl(Search::Xapian)
%global __requires_exclude ^perl\\((highlight|IO::KQueue)\\)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  curl
BuildRequires:  e2fsprogs
BuildRequires:  git
BuildRequires:  man-db
BuildRequires:  perl
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(Email::Address::XS)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Inline::C)
BuildRequires:  perl(Mail::IMAPClient)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Plack::Middleware::ReverseProxy)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Search::Xapian)
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  sqlite
BuildRequires:  xapian-core
# /oreon:deps
%description
public-inbox implements the sharing of an email inbox via git to complement or
replace traditional mailing lists. Readers may read via NNTP, IMAP, Atom feeds
or HTML archives.

%package -n perl-PublicInbox
Summary:        Perl libraries for public-inbox
%description -n perl-PublicInbox
Perl libraries for public-inbox.

%package server
Summary:        Server-side components for public-inbox
Requires:       %{name} = %{version}-%{release}
%description server
Server-side components and daemons for public-inbox.

%package -n lei
Summary:        Local Email Interface for public-inbox
Requires:       %{name} = %{version}-%{release}
%description -n lei
The client-side component of public-inbox that allows to interact with mail
storage systems, including public-inbox servers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*
for MANS in 1 5 7 8; do
    mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man$MANS
    install -m 0644 *.$MANS $RPM_BUILD_ROOT/%{_mandir}/man$MANS/
done
mkdir -p -m 0755 $RPM_BUILD_ROOT/%{_sysconfdir}/bash_completion.d
install -m 0644 contrib/completion/* $RPM_BUILD_ROOT/%{_sysconfdir}/bash_completion.d/
%oreon_autofiles perl-PublicInbox usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles lei usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

(cd certs && %{__perl} ./create-certs.perl)
mkdir -p $RPM_BUILD_ROOT/tmp
PERL_INLINE_DIRECTORY=$RPM_BUILD_ROOT/tmp make test
rm -rf $RPM_BUILD_ROOT/tmp
%files -f %{oreon_filedir}/main.list
%files -n perl-PublicInbox -f %{oreon_filedir}/perl-PublicInbox.list
%files -n public-inbox-server -f %{oreon_filedir}/public-inbox-server.list
%files -n lei -f %{oreon_filedir}/lei.list

%changelog

%autochangelog
