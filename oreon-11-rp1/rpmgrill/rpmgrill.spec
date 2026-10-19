%global source0_hash feb442b0de206ee172d77ac4b333d195f9aa13f53fa29cbfb6b78b736456678a
Name:           rpmgrill
Version:        0.34
Release:        1%{?dist}
Summary:        A utility for catching problems in koji builds
License:        Artistic-2.0
Source0:        https://github.com/default-to-open/%{name}/archive/%{version}.tar.gz
URL:            https://github.com/default-to-open/rpmgrill
BuildArch:      noarch
Requires:       perl(Module::Pluggable)
Requires: clamav
Requires: data(clamav)
Requires: /usr/bin/desktop-file-validate
Requires: elfutils
Requires: /usr/bin/xsltproc
Requires: git
Requires: binutils
Requires: koji
# oreon:deps
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  clamav
BuildRequires:  clamav-data
BuildRequires:  perl(CGI)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::LibMagic)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::MockModule)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(Time::ParseDate)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(YAML)
BuildRequires:  perl(YAML::Syck)
BuildRequires:  perl(boolean)
BuildRequires:  perl(open)
BuildRequires:  perl-generators
# /oreon:deps
%description
rpmgrill runs a series of tests against a set of RPMs, reporting problems
that may require a developer's attention.  For instance: unapplied patches,
multilib incompatibilities.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build

%{__perl} Build.PL --installdirs vendor
./Build
%install
./Build pure_install --destdir %{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
