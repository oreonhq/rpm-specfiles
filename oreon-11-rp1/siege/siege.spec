%global source0_hash 78af482fc655f1cf7270fdbc3171581ed4cb3163009f7f4f056fc2b7e2d24453
Name:           siege
Version:        4.2.0
Release:        1%{?dist}
Summary:        HTTP regression testing and benchmarking utility
License:        GPL-3.0-or-later
URL:            http://www.joedog.org/JoeDog/Siege
Source0:        http://download.joedog.org/siege/%{name}-%{version}.tar.gz
Patch0:         siege-4.1.7-bindir.patch
Patch1:         siege-4.1.7-Drop-outdated-macro-definitions.patch
Patch2:         siege-4.1.7-Add-needed-macro-definitions-in-subdir.patch
Patch3:         siege-4.1.7-Remove-obsolete-stuff-from-configure.ac.patch
Patch4:         siege-4.1.7-Drop-unneeded-TIME_WITH_SYS_TIME-conditional.patch
Requires:       libjoedog >= 0.1.2
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libjoedog-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
