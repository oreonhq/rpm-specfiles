%global source0_hash 4731efa17b0475bb88880a4be12af36154f2188468903ebd1e90310ea942b9bd

Name:           uredir
Version:        3.3
Release:        12%{?dist}
Summary:        UDP port redirector

License:        ISC
URL:            https://github.com/troglobit/uredir
Source0:        https://github.com/troglobit/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  libuev-devel
BuildRequires:  make

%description
uredir is a small Linux daemon to redirect UDP connections. 
It can be used to forward connections on small and embedded 
systems that do not have (or want to use) iptables or nftables.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
./autogen.sh
%configure
%make_build

%check
make check

%install
%make_install

# remove docs from buildroot
rm -rf %{buildroot}%{_docdir}/%{name}

%files
%license LICENSE
%doc README.md AUTHORS design.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
