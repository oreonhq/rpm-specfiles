%global source0_hash 457dc7374ee59cb75a0729e51cef2f2c52b48180f739d8fd956ea19882815f33
Name:           mhonarc
Version:        2.6.24
Release:        1%{?dist}
Summary:        Perl mail-to-HTML converter
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/MHonArc
Source0:        https://cpan.metacpan.org/authors/id/L/LD/LDIDRY/MHonArc-%{version}.tar.gz
BuildArch:      noarch
Provides:       MHonArc = %{version}-%{release}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(.*\.pl\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Config)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
MHonArc is a Perl mail-to-HTML converter. MHonArc provides HTML mail
archiving with index, mail thread linking, etc; plus other
capabilities including support for MIME and powerful user
customization features.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MHonArc-%{version}

%build

%install
%{__perl} install.me -batch -libpath %{buildroot}%{_datadir}/MHonArc \
  -nodoc -manpath %{buildroot}%{_mandir} -binpath %{buildroot}%{_bindir}
%{__perl} -pi -e \
  "s|%{buildroot}\b||g ; s|/usr/local/bin/perl\b|%{__perl}|g" \
  %{buildroot}%{_bindir}/* examples/mha*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
