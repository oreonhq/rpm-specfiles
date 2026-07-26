%global source0_hash 3e6a8caccc60cc0bcfb49e4aa0f5722ee642beac4e21c8b47aac65f931910efe

%global module App-PFT

Name:           perl-%{module}
Version:        1.4.1
Release:        19%{?dist}
Summary:        Hacker friendly static blog generator

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/dacav/%{module}
Source0:        https://github.com/dacav/%{module}/archive/v%{version}.tar.gz#/%{module}-%{version}.tar.gz

# This software packet is composed by a toolkit of executable scripts, which
# are chain loaded by a main script named 'pft`. The position of the scripts is
# determined by using perl(FindBin). If the package is installed via CPAN it
# makes sense to seek for the scripts in the same directory as the library. For
# the Fedora package the appropriate position is /usr/libexec/%%{module}.
# The following patch makes it compliant with this requirement without breaking
# the desirable behavior in the CPAN distribution.
Patch0:         %{name}.libexec.patch

BuildArch:      noarch
Provides:       pft = %{version}-%{release}

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter

# Generated BuildRequires via the following command:
# tangerine -c Makefile.PL bin lib t | perl -nE '/^\s/ and next; s/^/BuildRequires:  perl(/; s/$/)/; print'

BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(feature)
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
BuildRequires:  perl(Pod::Find)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Template::Alloy)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

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

%check
LC_ALL=C.UTF-8 make test

%files
%{!?_licensedir:%global license %%doc}
%doc %{_mandir}/man1/*.1*
%doc README.md
%{perl_vendorlib}/*
%{_bindir}/pft
%{_libexecdir}/%{name}/pft-clean
%{_libexecdir}/%{name}/pft-edit
%{_libexecdir}/%{name}/pft-gen-rss
%{_libexecdir}/%{name}/pft-grab
%{_libexecdir}/%{name}/pft-init
%{_libexecdir}/%{name}/pft-ls
%{_libexecdir}/%{name}/pft-make
%{_libexecdir}/%{name}/pft-pub
%{_libexecdir}/%{name}/pft-show
%{_datadir}/bash-completion/completions/pft
%license COPYING

%changelog
%autochangelog
