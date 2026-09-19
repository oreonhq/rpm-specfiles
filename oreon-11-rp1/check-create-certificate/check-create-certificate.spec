%global source0_hash dae8c32d1d619181946ee3c1150d84214612b711ed2c05201374ed5952f963b0

%global         snapshotdate 20140409
%global         commit d0971baf5d13e06aaa600581efe3adba6631e06a
%global         shortcommit %(c=%{commit}; echo ${c:0:7})
%global         checkout %{snapshotdate}git%{shortcommit}

Name:           check-create-certificate
Version:        0.5
Release:        33.%{checkout}%{?dist}
Summary:        A non-interactive script that creates an SSL certificate if it does not exist
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
Url:            https://github.com/jdsn/check-create-certificate
Source:         https://github.com/jdsn/check-create-certificate/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildRequires:         perl-generators
Requires:       openssl-perl
BuildArch:      noarch

%description
A script that checks for the existence of an SSL certificate
or creates a new self signed one. It runs non-interactively and
uses either predefined values or automatically guesses the best values.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{commit}

%build

%install
install -Dpm 755 script/%{name} %{buildroot}%{_sbindir}/%{name}

%files
%{_sbindir}/%{name}
%doc COPYING

%changelog
%autochangelog
