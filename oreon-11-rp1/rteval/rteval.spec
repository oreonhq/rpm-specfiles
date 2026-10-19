%global source0_hash 5781ddc9de0557b60434dc903042798906ecb64a24ea8572cc152164c8e113f1
Name:		rteval
Version:	3.13
Release:        1%{?dist}
Summary:        Utility to evaluate system suitability for RT Linux
Group:		Development/Tools
License:	GPL-2.0-only AND GPL-2.0-or-later
URL:		https://git.kernel.org/pub/scm/utils/rteval/rteval.git
Source0:        https://www.kernel.org/pub/linux/utils/%{name}/%{name}-%{version}.tar.xz
Patch0:         0001-rteval-do-not-require-wheel-for-building.patch
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
Recommends:	dmidecode
BuildArch:	noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-rteval = %{version}-%{release}
# /oreon:deps
%package -n       python3-rteval+mcp
Summary:        Metapackage for python3-rteval mcp extras
Requires:       python3-rteval = %{version}-%{release}
Provides:       python3dist(rteval[mcp]) = %{version}-%{release}

%description -n python3-rteval+mcp
Metapackage for python3-rteval mcp extras.

%description
The rteval script is a utility for measuring various aspects of
realtime behavior on a system under load. The script unpacks the
kernel source, and then goes into a loop, running hackbench and
compiling a kernel tree. During that loop the cyclictest program
is run to measure event response time. After the run time completes,
a statistical analysis of the event response times is done and printed
to the screen.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
# Delete setup.py so pyproject.toml build doesn't use it
rm -f setup.py

%build

%pyproject_wheel
%install
%pyproject_install
install -D -m 0755 rteval-cmd %{buildroot}%{_bindir}/rteval
mkdir -p %{buildroot}%{_mandir}/man8
gzip -c doc/rteval.8 > %{buildroot}%{_mandir}/man8/rteval.8.gz
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 0644 rteval/rteval_*.xsl %{buildroot}%{_datadir}/%{name}/
mkdir -p %{buildroot}%{_sysconfdir}
install -m 0644 rteval.conf %{buildroot}%{_sysconfdir}/rteval.conf
%oreon_autofiles main

%files

%changelog

%autochangelog
