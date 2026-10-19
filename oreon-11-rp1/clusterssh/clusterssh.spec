%global source0_hash 9018c8efea516a750605473f876dcceab5a22089e8e59fba806a366957614b5e
Name:          clusterssh
Version:       4.19
Release:        1%{?dist}
Summary:        Secure concurrent multiple server terminal control
License:       GPL-1.0-or-later OR Artistic-1.0-Perl
URL:           https://github.com/duncs/clusterssh
Source0:        https://github.com/duncs/clusterssh/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:     noarch
Requires:      xterm
Requires:      xorg-x11-fonts-75dpi xorg-x11-fonts-100dpi
# oreon:deps
BuildRequires:  fdupes
BuildRequires:  perl(CPAN::Changes)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(English)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(Locale::Maketext)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Net::hostent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Sort::Naturally)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::DistManifest)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Trap)
BuildRequires:  perl(Tk)
BuildRequires:  perl(Tk::Dialog)
BuildRequires:  perl(Tk::LabEntry)
BuildRequires:  perl(Tk::ROText)
BuildRequires:  perl(Tk::Xlib)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(X11::Keysyms)
BuildRequires:  perl(X11::Protocol)
BuildRequires:  perl(X11::Protocol::Constants)
BuildRequires:  perl(X11::Protocol::Other)
BuildRequires:  perl(X11::Protocol::WM)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perltidy
BuildRequires:  xterm
# /oreon:deps
%description
Control multiple terminals open on different servers to perform administration
tasks, for example multiple hosts requiring the same configuration within a 
cluster. Not limited to use with clusters, however.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

perl Build.PL installdirs=vendor
./Build
%check

./Build test
%install
./Build install destdir=%{buildroot} create_packlist=0
%fdupes %buildroot
%{_fixperms} %{buildroot}
mkdir -p %{buildroot}/%{_sysconfdir}/bash_completion.d
mv  %{buildroot}/%{_bindir}/clusterssh_bash_completion.dist \
    %{buildroot}/%{_sysconfdir}/bash_completion.d/clusterssh
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
