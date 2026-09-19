%global source0_hash 1e5996757f879c81f202a18ad8e982195cf51c41727d3fea4af01fdcbbb5563a

Name:           sl
Version:        5.02
Release:        25%{?dist}
Summary:        Joke command for when you type 'sl' instead of 'ls'
License:        SL
URL:            https://github.com/mtoyoda/sl
Source0:        https://github.com/mtoyoda/sl/archive/%{version}/sl-%{version}.tar.gz
BuildRequires: make
BuildRequires:  ncurses-devel, gcc

# Copyright file is taken from the Debian project
# http://packages.debian.org/changelogs/pool/main/s/sl/sl_3.03-14/sl.copyright
# and has been confirmed with the original author.

%description
The sl (Steam Locomotive) command is a joke which displays a train on your
terminal when you accidentally type 'sl' instead of 'ls'.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m0755 sl %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/man1
install -p -m644 sl.1 %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_mandir}/ja/man1
install -p -m644 sl.1.ja %{buildroot}%{_mandir}/ja/man1/

%files
%doc README.ja.md README.md LICENSE
%{_mandir}/ja/man1/*
%{_mandir}/man1/*
%{_bindir}/sl

%changelog
%autochangelog
