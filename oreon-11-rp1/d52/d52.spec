%global source0_hash 784900108a4352fb439f9c9efa9458c93138ed1f05f2e41aa2faca5bc7c76e46

%global major 3
%global minor 4
%global patchlevel 1

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

# Notified upstream of incorrect FSF address on 23-NOV-2013.

Name:           d52
URL:            http://www.brouhaha.com/~eric/software/d52/
Version:        %{major}.%{minor}.%{patchlevel}
Release:        30%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Summary:        Disassemblers for 8051, 8048, and Z80 families
Source:         http://www.brouhaha.com/~eric/software/d52/%{name}v%{major}%{minor}%{patchlevel}.zip
Patch0:         d52v341-nostrip.patch
Patch1:         d52v341-format-security.patch
BuildRequires:  gcc
BuildRequires:  dos2unix
BuildRequires: make

%description
D52 is collection of disassemblers for the 8051, 8048, and Z80
families of microcontrollers and microprocessors.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n d52v%{major}%{minor}%{patchlevel}

for f in Makefile README *.{h,c,ctl,html} cyclefiles/*.{a51,cyc,ctl,d52,HEX,LST,rtf}
do
    dos2unix -k $f
done

# Fedora-specific patch to avoid stripping the executables in the build
# process, as that interferes with creation of a debuginfo RPM.
%patch -P0 -p1 -b .nostrip
%patch -P1 -p1 -b .format-security

%build
make %{_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 d52 %{buildroot}%{_bindir}
install -p -m0755 d48 %{buildroot}%{_bindir}
install -p -m0755 dz80 %{buildroot}%{_bindir}

install -d -m0755 %{buildroot}%{_datadir}/%{name}/cyclefiles
install -p -m0644 cyclefiles/*.cyc %{buildroot}%{_datadir}/%{name}/cyclefiles

install -d -m0755 %{buildroot}%{_datadir}/%{name}/examples
install -p -m0644 cyclefiles/*.{a51,d52,bin,ctl,HEX,LST,z80} %{buildroot}%{_datadir}/%{name}/examples

%files
%{_bindir}/d52
%{_bindir}/d48
%{_bindir}/dz80
%{_datadir}/%{name}
%doc COPYING README d52manual.html dz80-d48addendum.html
%doc cyclefiles/cycle_counting.{doc,htm,rtf}

%changelog
%autochangelog
