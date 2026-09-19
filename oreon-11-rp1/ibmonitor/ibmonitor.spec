%global source0_hash 331dac4553b5c336d1db3d35176ecebeaf15b39ad0432372cba583324a222e28

Name:           ibmonitor
Version:        1.4
Release:        34%{?dist}

Summary:        Interactive bandwidth monitor

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://ibmonitor.sourceforge.net/
Source0:        http://dl.sf.net/ibmonitor/ibmonitor-1.4.tar.gz
BuildArch:      noarch
BuildRequires:      perl-generators

Requires:       perl(Term::ReadKey)

%description
The program ibmonitor is an interactive linux console application which shows
bandwidth consumed and total data transferred on all interfaces.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ibmonitor

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 ibmonitor $RPM_BUILD_ROOT%{_bindir}

%files
%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/ibmonitor

%changelog
%autochangelog
