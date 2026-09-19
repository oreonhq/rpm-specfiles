%global source0_hash 367ec4f02dd6a3a225b4338ea7b961b87fb144f7388b2ea1eb3a5593fc53f47e

Name:           xdms
Version:        1.3.2
Release:        38%{?dist}
Summary:        Extracts Amiga DMS archives
License:        LicenseRef-Fedora-Public-Domain
URL:            http://zakalwe.fi/~shd/foss/%{name}
Source0:        http://zakalwe.fi/~shd/foss/%{name}/%{name}-%{version}.tar.bz2
Patch0:         inline.patch

BuildRequires: make
BuildRequires:  gcc
%description
Extracts Amiga DMS (Disk Masher) archives which are compressed Amiga disk
images. Xdms is particularly useful with Amiga emulators.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build
# Non standard configure script that does not support libdir for example.
CFLAGS="%{optflags}" ./configure --prefix=%{_usr}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m0644 xdms.1 %{buildroot}%{_mandir}/man1
install -p -m0755 src/xdms %{buildroot}%{_bindir}

%files
%{_bindir}/xdms
%{_mandir}/man1/xdms.1.*
%doc ChangeLog.txt %{name}.txt

%changelog
%autochangelog
