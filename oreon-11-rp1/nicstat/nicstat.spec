%global source0_hash c4cc33f8838f4523f27c3d7584eedbe59f4c587f0821612f5ac2201adc18b367
Name:		nicstat	
Version:	1.95
Release:        1%{?dist}
Summary:        CLI utility that prints out network statistics for all network interface
License:	Artistic-2.0
URL:		http://sourceforge.net/projects/%{name}
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
# /oreon:deps
%description
nicstat is a Solaris and Linux command-line that prints out network statistics 
for all network interface cards (NICs), including packets, kilobytes per second,
average packet sizes and more.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{version}

%build

gcc %{optflags} %{name}.c -o %{name}
%install
install -p -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -p -D -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
