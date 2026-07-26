%global source0_hash 260afaa7000abd7ce8c980b721c5c16dc7cb218d161278ba3b8eddd0b0b018ae

%bcond tests 0

Name:           wcurl
Version:        2026.01.05
Release:        %autorelease
Summary:        A simple wrapper around curl to easily download files
License:        curl
BuildArch:      noarch
URL:            https://github.com/curl/%{name}
Source:		%{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# rhbz#1992804
# Temporarily disable the test until the PR is merged.
# https://src.fedoraproject.org/rpms/shunit2/pull-request/1
%if %{with tests}
BuildRequires:  shunit2
%endif
BuildRequires:  curl
Requires:       curl

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build

%install
install -t '%{buildroot}%{_bindir}' -D -p wcurl
install -t '%{buildroot}%{_mandir}/man1' -D -m 0644 -p wcurl.1

%check
%if %{with tests}
PATH="${PATH}:%{buildroot}%{_bindir}" ./tests/tests.sh
%endif

%files
%doc README.md
%doc CHANGELOG.md
%license LICENSE
%license AUTHORS
%{_bindir}/wcurl
%{_mandir}/man1/wcurl.1*

%changelog
%autochangelog
