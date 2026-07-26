%global source0_hash 1b08c6613525e75e87546f4e8984ab3b33f1e922080268c749f1777d56c9d361

Name:           asciiquarium
Version:        1.1
Release:        28%{?dist}
Summary:        ASCII art aquarium/sea animation

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.robobunny.com/projects/asciiquarium/html/
Source0:        http://www.robobunny.com/projects/%{name}/%{name}_%{version}.tar.gz

BuildArch:      noarch
BuildRequires:      perl-generators

%description
Enjoy the mysteries of the sea from the safety of your own terminal!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}_%{version}

%build

%install
install -p -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc README gpl.txt
%{_bindir}/%{name}

%changelog
%autochangelog
