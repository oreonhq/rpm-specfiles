%global source0_hash a71fb7efea5a63770d8fb71321ef6ae7afe0592f1aa7f7e2b496c26ccbb392a4

%global	pver	20260129

Name:		mawk
Version:	1.3.4
Release:	6.%{pver}%{?dist}
Epoch:		1
Summary:	Interpreter for the AWK programming language
License:	GPL-2.0-only
BuildRequires:	make byacc
BuildRequires:	gcc
URL:		https://invisible-island.net/mawk/
Source0:	https://invisible-island.net/archives/mawk/%{name}-%{version}-%{pver}.tgz

%description
mawk is an interpreter for the AWK programming language.  The AWK language is
useful for manipulation of data files, text retrieval and processing, and for
prototyping and experimenting with algorithms.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-%{pver}
chmod 644 examples/*

%build
%configure
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

%files
%doc COPYING CHANGES README examples/

%{_bindir}/mawk
%{_mandir}/man1/mawk.1*
%{_mandir}/man7/mawk-*.7*

%changelog
%autochangelog
