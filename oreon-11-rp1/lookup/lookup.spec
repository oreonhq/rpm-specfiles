%global source0_hash c2ecb4c98aef5a30b93ccca3a3d09b8bcf74a592c86ac5e69cabe21105aef723

Summary: A graphical tool to search DNS for answers
Name: lookup
Version: 2.2.3
Release: 18%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: http://www.dnssec-tools.org/
Source0: https://www.dnssec-tools.org/download/%{name}-%{version}.tar.gz
Source1: COPYING-from-dnssec-tools.txt
Source2: lookup.desktop
Patch0:  lookup-1.11.p2-dont-double-install.patch

BuildRequires: qt-devel
BuildRequires: dnssec-tools-libs-devel >= 2.2
BuildRequires: openssl-devel
BuildRequires: desktop-file-utils
BuildRequires: glibc
BuildRequires: glibc-devel
BuildRequires: libnsl2
BuildRequires: libnsl2-devel
BuildRequires: make

%description
The lookup utility allows you to query the DNS for answers.  It
displays the results in a graphical tree structure, and checks the
answers for validity and conformance with DNSSEC.  The results are
color coded based on their DNSSEC status.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 
%patch -P0 -p1

%build
%{qmake_qt4} PREFIX=/usr
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

rm -f %{buildroot}%{_datadir}/pixmap/lookup.xpm
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/
install -p -m 644 data/64x64/lookup.png %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/

rm -f %{buildroot}%{_datadir}/applications/hildon/lookup.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

mkdir -p %{buildroot}/%{_mandir}/man1
install -p -D -m 644 man/lookup.1 %{buildroot}/%{_mandir}/man1/lookup.1

%files
%doc COPYING
%doc %{_mandir}/man1/*
%{_bindir}/lookup
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/applications/lookup.desktop

%changelog
%autochangelog
