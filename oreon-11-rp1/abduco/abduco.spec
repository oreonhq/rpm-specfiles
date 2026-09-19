%global source0_hash c90909e13fa95770b5afc3b59f311b3d3d2fdfae23f9569fa4f96a3e192a35f4

Name:           abduco
Version:        0.6
Release:        24%{?dist}
Summary:        Session management in a clean and simple way

License:        ISC
URL:            http://www.brain-dump.org/projects/%{name}/
Source0:        %{url}/%{name}-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make

%description
%{name} provides session management i.e. it allows programs to be run
independently from its controlling terminal. That is programs can be
detached - run in the background - and then later reattached.
Together with dvtm it provides a simpler and cleaner alternative to tmux or
screen.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# Apply applicable build flags
echo '#!/bin/sh' > ./configure
chmod +x ./configure

%build
%configure
make %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix} STRIP=:

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%changelog
%autochangelog
