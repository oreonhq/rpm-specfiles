Name:		rteval
Version:	3.10
Release:	5%{?dist}
Summary:	Utility to evaluate system suitability for RT Linux

Group:		Development/Tools
License:	GPL-2.0-only AND GPL-2.0-or-later
URL:		https://git.kernel.org/pub/scm/utils/rteval/rteval.git
Source0:	https://www.kernel.org/pub/linux/utils/%{name}/%{name}-%{version}.tar.xz
# https://lore.kernel.org/linux-rt-users/20251126231223.100316-1-yselkowi@redhat.com/T/#u
Patch0:         0001-rteval-do-not-require-wheel-for-building.patch

BuildRequires:	python3-devel
Requires:	python3-libxml2
Requires:	realtime-tests
Requires:	rteval-loads >= 6.17.7-1
Requires:	sysstat
Requires:	xz bzip2 tar gzip m4 gawk
Requires:	kernel-headers
Requires:	sos
Requires:	numactl
Requires:	gcc binutils gcc-c++ flex bison bc make
Requires:	elfutils elfutils-libelf-devel
Requires:	openssl
Requires:	openssl-devel
Requires:	stress-ng
Requires:	perl-interpreter, perl-devel, perl-generators
Requires:	libmpc, libmpc-devel
Requires:	dwarves
# not available on all arches
Recommends:	dmidecode
BuildArch:	noarch

%description
The rteval script is a utility for measuring various aspects of
realtime behavior on a system under load. The script unpacks the
kernel source, and then goes into a loop, running hackbench and
compiling a kernel tree. During that loop the cyclictest program
is run to measure event response time. After the run time completes,
a statistical analysis of the event response times is done and printed
to the screen.

%prep
%autosetup -v -p1
# Delete setup.py so pyproject.toml build doesn't use it
rm -f setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files rteval

# Manually install rteval-cmd as rteval (pyproject.toml doesn't define scripts)
install -D -m 0755 rteval-cmd %{buildroot}%{_bindir}/rteval

# Manually install man page
mkdir -p %{buildroot}%{_mandir}/man8
gzip -c doc/rteval.8 > %{buildroot}%{_mandir}/man8/rteval.8.gz

# Manually install XSL files
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 0644 rteval/rteval_*.xsl %{buildroot}%{_datadir}/%{name}/

# Manually install config file
mkdir -p %{buildroot}%{_sysconfdir}
install -m 0644 rteval.conf %{buildroot}%{_sysconfdir}/rteval.conf

%files -f %{pyproject_files}
%defattr(-,root,root,-)
%doc README doc/rteval.txt
%license COPYING
%dir %{_datadir}/%{name}
%{_mandir}/man8/rteval.8.gz
%config(noreplace) %{_sysconfdir}/rteval.conf
%{_datadir}/%{name}/rteval_*.xsl
%{_bindir}/rteval

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.10-5
- Import
