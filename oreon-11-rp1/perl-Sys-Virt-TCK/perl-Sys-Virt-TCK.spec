%global source0_hash de90e4efa1fe8c35653190ab0a0c810402865d7acd9924575f0a2c6a155a4526
%define appname Sys-Virt-TCK
Summary:        Sys::Virt::TCK - libvirt Technology Compatibility Kit
Name: perl-%{appname}
Version: 2.0.0
Release:        1%{?dist}
License: GPL-2.0-or-later
Source0:        http://libvirt.org/sources/tck/%{appname}-v%{version}.tar.gz
Url: http://libvirt.org/
Requires: libvirt-client
Requires: perl(TAP::Formatter::HTML)
Requires: perl(TAP::Formatter::JUnit)
Requires: perl(IO::Pty)
Requires: guestfs-tools
BuildArchitectures: noarch
# oreon:deps
BuildRequires:  perl(App::Prove)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IO::Uncompress::Bunzip2)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Sub::Uplevel)
BuildRequires:  perl(Sys::Virt)
BuildRequires:  perl(TAP::Formatter::HTML)
BuildRequires:  perl(TAP::Formatter::JUnit)
BuildRequires:  perl(TAP::Harness)
BuildRequires:  perl(TAP::Harness::Archive)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XML::Twig)
BuildRequires:  perl(XML::Writer)
BuildRequires:  perl(XML::XPath)
BuildRequires:  perl(YAML)
BuildRequires:  perl(accessors)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Sys::Virt::TCK provides an integration test suite for validating
correct operation of libvirt drivers with underlying virtualization
technology.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{appname}-v%{version}

%build

%{__perl} Build.PL installdirs=vendor
./Build
%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0 \
  --install_path conf=%{_sysconfdir}/libvirt-tck \
  --install_path pkgdata=%{_datadir}/libvirt-tck/tests
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%__install -m 0755 -d $RPM_BUILD_ROOT%{_localstatedir}/cache/libvirt-tck
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
