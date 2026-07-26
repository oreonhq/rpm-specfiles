%global source0_hash 2017cba285b4167fb9f148b4509d7463402820e4e7a04865cec0fe887bd5e13a

Summary: Utility to display new messages of a logfile since last run
Name: fetchlog
Version: 1.4
Release: 31%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Url: http://sourceforge.net/projects/fetchlog
Source: http://dl.sf.net/sourceforge/fetchlog/fetchlog-%{version}.tar.gz

Buildrequires: gcc
BuildRequires: make

Patch0: fetchlog-build.patch
Patch1: fetchlog-unusedvar.patch
Patch2: fetchlog-1.4-write.patch
Patch3: fetchlog-1.4-tests.patch
Patch4: fetchlog-1.4-printf.patch

%description
The fetchlog utility displays the last new messages of a logfile. It is
similar like tail (1) but offers some extra functionality for output
formatting. To show only the new messages appeared since the last call
fetchlog uses a bookmark to remember which messages have been fetched.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 
%patch -P0
%patch -P1 -p1
%patch -P2 -p0
%patch -P3 -p1
%patch -P4 -p1

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_mandir}/man1
install -m755 %{name} %{buildroot}/%{_bindir}
install -m644 %{name}.1 %{buildroot}/%{_mandir}/man1

%check
make test
make testall

%files 
%{_bindir}/%{name}
%doc CHANGES LICENSE README README.Nagios README.SNMP
%{_mandir}/*/*

%changelog
%autochangelog
