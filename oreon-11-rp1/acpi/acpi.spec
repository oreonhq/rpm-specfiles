%global source0_hash e64c6e00b53cd797427ea32a160513425b03ed4f077733f71f1f09ff340f230b

Summary:	Command-line ACPI client
Summary(pl):	1lient ACPI działający z linii poleceń
Name:		acpi
Version:	1.8
Release:	4%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
Source0:	http://downloads.sourceforge.net/project/acpiclient/acpiclient/%{version}/%{name}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/acpiclient/

BuildRequires:  gcc
BuildRequires: make
%description
Linux ACPI client is a small command-line program that attempts to
replicate the functionality of the 'old' apm command on ACPI systems.
It includes battery and thermal information.

%description -l pl
Klient Linux ACPI to mały program działający z linii poleceń, będący
próbą zastąpienia funkcjonalności "starego" polecenia apm na systemach
opartych o ACPI. Zawiera informacje o zasilaniu i temperaturze.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS README COPYING
%{_bindir}/acpi
%{_mandir}/man1/acpi.1*

%changelog
%autochangelog
