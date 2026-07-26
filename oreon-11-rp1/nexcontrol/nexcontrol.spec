%global source0_hash c3e9cac978c58020d4b6c860e0ba5084f1479744ace029a4e315d642a301839d

Name:		nexcontrol
Version:	0.2
Release:	33%{?dist}
Summary:	Software to control your Celestron NexStar Telescope

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.mybrainhurts.com/projects/nexcontrol/
Source0:	http://www.mybrainhurts.com/projects/nexcontrol/%{name}.tar.gz

BuildArch:	noarch
BuildRequires:	perl-generators

%description
NexControl is a perl code to interface with
the NexStar series of scopes from Celestron.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 nexcontrol.pl $RPM_BUILD_ROOT%{_bindir}/nexcontrol

%files
%doc LICENSE README
%{_bindir}/nexcontrol

%changelog
%autochangelog
