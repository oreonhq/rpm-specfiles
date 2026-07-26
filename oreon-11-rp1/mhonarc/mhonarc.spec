%global source0_hash 8d1645b79a5c3fef8d13f7a82b3b680166794aaab7b6822a2313d9fb34d97af1

Name:           mhonarc
Version:        2.6.24
Release:        17%{?dist}
Summary:        Perl mail-to-HTML converter

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/MHonArc
Source0:        https://cpan.metacpan.org/authors/id/L/LD/LDIDRY/MHonArc-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
BuildRequires:  perl(Time::Local)
Provides:       MHonArc = %{version}-%{release}

# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(.*\.pl\\)

%description
MHonArc is a Perl mail-to-HTML converter. MHonArc provides HTML mail
archiving with index, mail thread linking, etc; plus other
capabilities including support for MIME and powerful user
customization features.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MHonArc-%{version}

%build
# Nothing to build

%install
%{__perl} install.me -batch -libpath %{buildroot}%{_datadir}/MHonArc \
  -nodoc -manpath %{buildroot}%{_mandir} -binpath %{buildroot}%{_bindir}
# Aww, remainders of buildroot and /usr/local, weed 'em out.
%{__perl} -pi -e \
  "s|%{buildroot}\b||g ; s|/usr/local/bin/perl\b|%{__perl}|g" \
  %{buildroot}%{_bindir}/* examples/mha*

%files
%license COPYING
%doc ACKNOWLG BUGS CHANGES RELNOTES TODO
%doc doc examples extras logo
%{_bindir}/mh*
%{_datadir}/MHonArc
%{_mandir}/man1/mh*.1*

%changelog
%autochangelog
