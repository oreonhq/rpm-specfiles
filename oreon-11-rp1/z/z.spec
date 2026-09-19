%global source0_hash 7d8695f2f5af6805f0db231e6ed571899b8b375936a8bfca81a522b7082b574e

%global projname z

%global desc \
Tracks your most used directories, based on 'frecency'.\
\
After a short learning phase, z will take you to the most 'frecent'\
directory that matches ALL of the regexps given on the command line, in\
order.

Name:		%{projname}
Version:	1.12
Release:	6%{?dist}
Summary:	Maintains a jump-list of the directories you actually use
License:	WTFPL
Source0:	https://github.com/rupa/%{projname}/archive/v%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	gzip

%description %{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_libexecdir}
install -pm 644 z.sh %{buildroot}%{_libexecdir}/z.sh
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 644 z.1 %{buildroot}%{_mandir}/man1/z.1

%check

%files
%{_libexecdir}/z.sh
%{_mandir}/man1/z.1*

%changelog
%autochangelog
