%global source0_hash ec140cedd159979383d60dbe87a0151c2c12ada78791095a8fa84ae635b93026

Name:           siege
Version:        4.1.7
Release:        5%{?dist}
Summary:        HTTP regression testing and benchmarking utility

License:        GPL-3.0-or-later
URL:            http://www.joedog.org/JoeDog/Siege
Source0:        http://download.joedog.org/siege/%{name}-%{version}.tar.gz
Patch0:         siege-4.1.7-bindir.patch

# https://github.com/JoeDog/siege/pull/242
Patch1:         siege-4.1.7-Drop-outdated-macro-definitions.patch
Patch2:         siege-4.1.7-Add-needed-macro-definitions-in-subdir.patch
Patch3:         siege-4.1.7-Remove-obsolete-stuff-from-configure.ac.patch
Patch4:         siege-4.1.7-Drop-unneeded-TIME_WITH_SYS_TIME-conditional.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  libtool
BuildRequires:  libjoedog-devel

Requires:       libjoedog >= 0.1.2

%description
Siege is an HTTP regression testing and benchmarking utility.
It was designed to let web developers measure the performance of their code
under duress, to see how it will stand up to load on the internet.
Siege supports basic authentication, cookies, HTTP and HTTPS protocols.
It allows the user hit a web server with a configurable number of concurrent
simulated users. Those users place the web-server "under siege."

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1
# Better default for log file (Bug 644631)
sed -i.orig doc/siegerc.in -e 's/^# logfile = *$/logfile = ${HOME}\/siege.log/'
rm -f *.m4
autoreconf --force --install --verbose --warnings=no-syntax

%build
export CFLAGS="-std=gnu17 %{build_cflags}"
%configure --sysconfdir=%{_sysconfdir}/siege
%make_build

%install
mkdir -p %{buildroot}%{_sysconfdir}/siege
# Create /etc/siege/urls.txt
%make_install

%files
%doc AUTHORS ChangeLog README.md
%{_bindir}/bombardment
%{_bindir}/siege
%{_bindir}/siege.config
%{_bindir}/siege2csv.pl
%{_mandir}/man1/bombardment.1.*
%{_mandir}/man1/siege.1.*
%{_mandir}/man1/siege.config.1.*
%{_mandir}/man1/siege2csv.1.*
%dir %{_sysconfdir}/siege
%config(noreplace) %{_sysconfdir}/siege/urls.txt
%config(noreplace) %{_sysconfdir}/siege/siegerc

%changelog
%autochangelog
