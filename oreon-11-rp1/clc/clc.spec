%global source0_hash 77dcbb6e6f0a55faabf4cb2ad72ed10b3065f1aceb7a6b0c7da20cc244405ac7

Name:		clc
Version:	0.03
Release:	34%{?dist}
Summary:	Command-line client for MUDs

License:	LicenseRef-Fedora-Public-Domain
URL:		http://github.com/elanthis/clc/tree/master
Source0:	http://cloud.github.com/downloads/elanthis/clc/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires: libtelnet-devel >= 0.20
BuildRequires: ncurses-devel
BuildRequires: zlib-devel
BuildRequires: make

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
Very simplistic MUD client for command line usage.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -DHAVE_ZLIB -DCLC_VERSION='\"%{version}\"'"

%install
rm -rf "%{buildroot}"
install -m 644 -D README "%{buildroot}%{_pkgdocdir}/README"
install -m 755 -D clc "%{buildroot}%{_bindir}/clc"

%files
%doc README
%{_bindir}/clc

%changelog
%autochangelog
