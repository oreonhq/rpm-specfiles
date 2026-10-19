%global source0_hash 3e6a8caccc60cc0bcfb49e4aa0f5722ee642beac4e21c8b47aac65f931910efe
%global module App-PFT
Name:           perl-%{module}
Version:        1.4.1
Release:        19%{?dist}
Summary:        Hacker friendly static blog generator
License:        GPL-3.0-or-later
URL:            https://github.com/dacav/%{module}
Source0:        https://github.com/dacav/%{module}/archive/v%{version}.tar.gz#/%{module}-%{version}.tar.gz
Patch0:         %{name}.libexec.patch
BuildArch:      noarch
Provides:       pft = %{version}-%{release}
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Escape)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(PFT)
BuildRequires:  perl(PFT::Conf)
BuildRequires:  perl(PFT::Date)
BuildRequires:  perl(PFT::Header)
BuildRequires:  perl(PFT::Text)
BuildRequires:  perl(PFT::Tree)
BuildRequires:  perl(PFT::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Find)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Template::Alloy)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(feature)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
PFT stands for *Plain F. Text*, where the meaning of *F.* is up to
personal interpretation. Like *Fancy* or *Fantastic*.

It is yet another static website generator. This means your content is
compiled once and the result can be served by a simple HTTP server,
without need of server-side dynamic content generation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{module}-%{version} -p1

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}
%install
%{__make} pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} %{buildroot}/*
%{__install} -d %{buildroot}%{_libexecdir}/%{name}
%{__install} -d %{buildroot}%{_datadir}/bash-completion/completions
%{__install} -t %{buildroot}%{_datadir}/bash-completion/completions bash_completion.d/pft
%{__mv} "%{buildroot}%{_bindir}/pft-clean"   "%{buildroot}%{_libexecdir}/%{name}"
%{__mv} "%{buildroot}%{_bindir}/pft-edit"    "%{buildroot}%{_libexecdir}/%{name}"
%{__mv} "%{buildroot}%{_bindir}/pft-gen-rss" "%{buildroot}%{_libexecdir}/%{name}"
%{__mv} "%{buildroot}%{_bindir}/pft-grab"    "%{buildroot}%{_libexecdir}/%{name}"
%{__mv} "%{buildroot}%{_bindir}/pft-init"    "%{buildroot}%{_libexecdir}/%{name}"
%{__mv} "%{buildroot}%{_bindir}/pft-ls"      "%{buildroot}%{_libexecdir}/%{name}"
%{__mv} "%{buildroot}%{_bindir}/pft-make"    "%{buildroot}%{_libexecdir}/%{name}"
%{__mv} "%{buildroot}%{_bindir}/pft-pub"     "%{buildroot}%{_libexecdir}/%{name}"
%{__mv} "%{buildroot}%{_bindir}/pft-show"    "%{buildroot}%{_libexecdir}/%{name}"
%oreon_autofiles main

%check

LC_ALL=C.UTF-8 make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
