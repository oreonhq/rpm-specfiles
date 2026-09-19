%global source0_hash 3893e11b421acdef1c42cb859a9288ed505e24d6ebf9de8b34829aa4759a1e67

Summary:          Simple tool to decode X.509 certificates
Name:             x509viewer
Version:          0.1.0
Release:          19%{?dist}
License:          GPL-2.0-or-later
URL:              https://ftp.robert-scheck.de/linux/%{name}/
Source:           https://ftp.robert-scheck.de/linux/%{name}/%{name}-%{version}.tar.gz
Requires:         %{_bindir}/openssl
BuildRequires:    make
BuildRequires:    perl-generators
BuildArch:        noarch

%description
x509viewer is a simple command line application, written in Perl, that can be
used to decode one or multiple X.509 certificates per given file, such as e.g.
SSL certificates, CSRs (certificate signing requests), but also private keys.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/%{name}

%changelog
%autochangelog
